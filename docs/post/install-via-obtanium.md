---
title: Install via Obtainium
description: Install and auto-update FGA Preview with Obtainium using the GitHub Releases feed, including Android 8+ requirements and update tips.
tags:
  - installation
  - updates
  - obtanium
---

# Install via Obtainium
Install FGA Preview from GitHub Releases and let Obtainium keep it updated for you.

## Overview
Obtainium is an Android app that can install and update apps directly from their official release pages (like GitHub Releases).

This guide helps you:

- Install **FGA Preview** from the official GitHub releases
- Get update notifications and upgrade with one tap
- Avoid manually downloading APKs each time

You should use this if you want **easy updates** and you’re comfortable installing apps from outside the Play Store.

---

## Key Features

- **One-time setup**: Add the FGA Preview release page once.
- **Update checks**: Obtainium can notify you when a new version is posted.
- **Safer source**: Updates come from the same GitHub Releases page every time.

---

## How to Start

### 1) Make sure your device meets requirements
FGA Preview requires **Android 8.0 or higher**.

---

### 2) Install Obtainium

1. Open the Obtainium releases page: `https://github.com/ImranR98/Obtainium/releases`
2. Download the latest APK asset.
3. Install it on your phone.

!!! tip
    If Android blocks the install, it will offer a shortcut to enable **Allow from this source** for your browser or file manager.

---

### 3) Add FGA Preview to Obtainium

1. Open **Obtainium**.
2. Tap **Add App**.
3. In the URL field, paste the FGA Preview releases URL:
   - `https://github.com/ArthurKun21/FGA-Preview-Build/releases`
4. Confirm the source (it should detect **GitHub**).
5. Tap **Add** / **Import** to finish.

---

## Installing and Updating FGA Preview

### Install (first time)

1. In **Obtainium**, open the newly added **FGA Preview** entry.
2. Tap **Install**.
3. When Android asks for permission, approve the install prompt.

### Update (when a new release is available)

1. Open **Obtainium**.
2. Tap **Check for Updates** (or pull to refresh, depending on your layout).
3. If an update is found, tap **Update**.

!!! info
    The latest preview build is published on the GitHub Releases page and often uses a tag like `pre-XXXX`.

---

## Alternative Video setup guide

You can watch this Youtube walkthrough for installing with Obtainium:

[![Obtainium Walkthrough](https://i.ytimg.com/vi/0MF_v2OBncw/mqdefault.jpg)](https://youtu.be/0MF_v2OBncw)

---

## Common Setup Notes

| Item | What it means |
| ---- | ------------ |
| **Source URL** | Use `https://github.com/ArthurKun21/FGA-Preview-Build/releases` so Obtainium can find new releases. |
| **Android install permission** | Android requires you to allow installs from your browser/file manager/Obtainium when sideloading. |

---

## Tips for Best Results

1. **Enable notifications**: Turn on **Obtainium** notifications so you don’t miss new releases.
2. **Keep one source of truth**: Avoid installing the same app from multiple updaters (e.g., another store) to reduce update conflicts.
3. **Confirm Android version first**: Check you’re on **Android 8+** to avoid failed installs.
4. **Update on Wi‑Fi**: APK downloads can be large; updating on Wi‑Fi is more reliable.

---

## Troubleshooting

| Problem | Solution |
| ------- | -------- |
| Install button is disabled or install fails immediately | Check that your phone is **Android 8.0+**. If not, you’ll need a compatible device or the stable app (if it supports your Android version). |
| Android says “For your security, your phone isn’t allowed to install unknown apps” | Open the prompt and enable **Allow from this source** for the app you used to download (browser/file manager) or for **Obtainium**, then try again. |
| Obtainium can’t find updates for FGA Preview | Confirm the app entry is using the **Releases page URL**: `https://github.com/ArthurKun21/FGA-Preview-Build/releases`. If it’s a specific release/tag URL, edit it to the releases list page. |
| Update downloads but won’t install | Make sure **Obtainium** has permission to install apps. Also close FGA Preview during the update, then retry. |
| You installed the wrong app (stable vs preview) | In **Obtainium**, remove the wrong entry, then add the correct releases page and reinstall. |

---

## Related Documentation

- [Requirements](../app/requirements.md)
