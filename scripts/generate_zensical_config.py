from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

ROOT_DIR = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT_DIR / "docs"
CONFIG_PATH = ROOT_DIR / "zensical.toml"
ROOT_NAV_PATH = DOCS_DIR / ".nav.yml"
START_MARKER = "# BEGIN GENERATED NAV"
END_MARKER = "# END GENERATED NAV"
IGNORED_NAV_FILES = {".DS_Store", ".meta.yml", ".nav.yml"}


def read_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if data is None:
        return {}
    if not isinstance(data, dict):
        raise ValueError(f"Expected a mapping in {path}")
    return data


def get_folder_sort_direction(directory: Path) -> str:
    nav_path = directory / ".nav.yml"
    if not nav_path.exists():
        return "asc"

    config = read_yaml(nav_path)
    sort = config.get("sort", {})
    if not isinstance(sort, dict):
        return "asc"

    direction = sort.get("direction", "asc")
    if direction not in {"asc", "desc"}:
        raise ValueError(f"Unsupported sort direction in {nav_path}: {direction}")
    return direction


def expand_folder(path: str) -> list[str]:
    directory = DOCS_DIR / path
    if not directory.is_dir():
        raise FileNotFoundError(f"Navigation folder does not exist: {directory}")

    entries = [
        child.name
        for child in directory.iterdir()
        if child.is_file() and child.suffix == ".md" and child.name not in IGNORED_NAV_FILES
    ]
    entries.sort(reverse=get_folder_sort_direction(directory) == "desc")
    return [f"{path}{name}" for name in entries]


def normalize_nav(node: object) -> object:
    if isinstance(node, str):
        return expand_folder(node) if node.endswith("/") else node

    if isinstance(node, list):
        return [normalize_nav(item) for item in node]

    if isinstance(node, dict):
        return {key: normalize_nav(value) for key, value in node.items()}

    raise TypeError(f"Unsupported navigation node: {node!r}")


def render_nav_value(node: object) -> str:
    if isinstance(node, str):
        return json.dumps(node)

    if isinstance(node, list):
        return "[" + ", ".join(render_nav_value(item) for item in node) + "]"

    if isinstance(node, dict):
        if len(node) != 1:
            raise ValueError(f"Navigation mapping must contain exactly one key: {node!r}")
        key, value = next(iter(node.items()))
        return "{ " + json.dumps(str(key)) + " = " + render_nav_value(value) + " }"

    raise TypeError(f"Unsupported rendered navigation node: {node!r}")


def render_nav_block(nav_items: list[object]) -> str:
    lines = ["nav = ["]
    lines.extend(f"  {render_nav_value(item)}," for item in nav_items)
    lines.append("]")
    return "\n".join(lines)


def update_config(nav_block: str) -> None:
    pattern = re.compile(
        rf"(?ms)^{re.escape(START_MARKER)}\n.*?^{re.escape(END_MARKER)}$"
    )
    content = CONFIG_PATH.read_text(encoding="utf-8")
    replacement = f"{START_MARKER}\n{nav_block}\n{END_MARKER}"
    updated_content, replacements = pattern.subn(replacement, content, count=1)
    if replacements != 1:
        raise ValueError(f"Could not locate generated nav markers in {CONFIG_PATH}")
    CONFIG_PATH.write_text(updated_content + ("" if updated_content.endswith("\n") else "\n"), encoding="utf-8")


def main() -> int:
    root_nav = read_yaml(ROOT_NAV_PATH).get("nav")
    if not isinstance(root_nav, list):
        raise ValueError(f"Expected a nav list in {ROOT_NAV_PATH}")

    normalized_nav = normalize_nav(root_nav)
    if not isinstance(normalized_nav, list):
        raise ValueError("Normalized root navigation must be a list")

    update_config(render_nav_block(normalized_nav))
    print(f"Updated {CONFIG_PATH.relative_to(ROOT_DIR)} from {ROOT_NAV_PATH.relative_to(ROOT_DIR)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())