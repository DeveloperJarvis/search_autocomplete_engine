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
# logging MODULE
# --------------------------------------------------
"""
Logging utilities for the Scratch Autocomplete Engine.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
import logging
import os
from typing import Optional

from config.config import AppConfig


_LOGGERS = {}


def get_logger(
        name: str,
        config: Optional[AppConfig] = None,
    ) -> logging.Logger:
    """
    Get a configured logger instance.

    Ensures:
    - Singleton logger per name
    - File + console logging
    - Configuration via AppConfig

    Args:
        name (str): Logger name
        config (AppConfig, optional): Application config
    
    Returns:
        logging.Logger
    """
    if name in _LOGGERS:
        return _LOGGERS[name]
    
    config = config or AppConfig()

    logger = logging.getLogger(name)
    logger.setLevel(config.LOG_LEVEL)
    logger.propagate = False

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler
    log_dir = os.path.dirname(config.LOG_FILE)
    os.makedirs(log_dir, exist_ok=True)

    file_handler = logging.FileHandler(config.LOG_FILE)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    _LOGGERS[name] = logger
    return logger
