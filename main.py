# SPDX-License-Identifier: GPL-3.0
# /// script
# dependencies = [
#   "pygame-ce",
#   "pygame-menu-ce",
#   "pyscroll",
#   "pytmx",
#   "pyyaml",
#   "natsort",
#   "packaging",
# ]
# ///
"""
Web (pygbag/Emscripten) entry point for Tuxemon.

pygbag requires a top-level ``main.py`` in the project root containing an
async ``asyncio.run(...)`` call. This simply reuses the same launch path
as the desktop CLI (``run_tuxemon.py``), which is now asyncio-based so
that it works identically on native platforms and in the browser.

Do not rename or move this file -- pygbag looks for it by this exact
name at the project root by default.
"""
from __future__ import annotations

import asyncio

from run_tuxemon import launch_game

asyncio.run(launch_game())
