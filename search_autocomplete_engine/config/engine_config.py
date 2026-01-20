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
# engine_config MODULE
# --------------------------------------------------
"""
Engine configuration module.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from dataclasses import dataclass

from search_autocomplete_engine.config.defaults import (
    DEFAULT_TOP_K,
    DEFAULT_CASE_SENSITIVE,
)
from search_autocomplete_engine.exceptions.errors import InvalidTopKError


# --------------------------------------------------
# engine config
# --------------------------------------------------
@dataclass(frozen=True)
class EngineConfig:
    """
    Configuration object for the autocomplete engine.

    Attributes:
        top_k (int): Number of suggestions to return
        case_sensitive (bool): Case sensitivity flag
    """

    top_k: int = DEFAULT_TOP_K
    case_sensitive: bool = DEFAULT_CASE_SENSITIVE

    def __post_init__(self) -> None:
        if self.top_k <= 0:
            raise InvalidTopKError(
                "top_k must be greater than zero"
            )
