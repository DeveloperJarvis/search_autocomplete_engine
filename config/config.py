# --------------------------------------------------
# -*- Python -*- Compatibility Header
#
# Copyright (C) 2023 Developer Jarvis (Pen Name)
#
# This file is part of the Search Autocomplete Engine Library. This library is free
# software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Search Autocomplete Engine - Autocomplete queries using Trie and frequency ranking
#                   Skills: Tries, string algorithms, data indexing
#
# Author: Developer Jarvis (Pen Name)
# Contact: https://github.com/DeveloperJarvis
#
# --------------------------------------------------

# --------------------------------------------------
# config MODULE
# --------------------------------------------------
"""
Top-level application configuration.

This module wires application configuration with
the core search autocomplete engine configuration.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
import os
from dataclasses import dataclass
from search_autocomplete_engine.config.engine_config import EngineConfig


# --------------------------------------------------
# app config
# --------------------------------------------------
@dataclass(frozen=True)
class AppConfig:
    """
    Root configuration object for the application.
    """
    engine: EngineConfig = EngineConfig()

    # Logging
    LOG_LEVEL: str = "INFO"
    PARENT_DIR: str = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
    LOG_FILE: str = os.path.join(
        os.path.dirname(PARENT_DIR), "logs", "autocomplete.log"
    )



