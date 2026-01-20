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
# validators MODULE
# --------------------------------------------------
"""
Validation helpers for inputs.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from search_autocomplete_engine.exceptions.errors import (
    InvalidQueryError,
    InvalidPrefixError,
    InvalidTopKError,
)


def validate_query(query: str) -> None:
    """
    Validate a full search query.

    Raises:
        InvalidQueryError
    """
    if not isinstance(query, str):
        raise InvalidQueryError("Query must be a string")

    if not query.strip():
        raise InvalidQueryError("Query cannot be empty")


def validate_prefix(prefix: str) -> None:
    """
    Validate autocomplete prefix.

    Raises:
        InvalidPrefixError
    """
    if not isinstance(prefix, str):
        raise InvalidPrefixError("Prefix must be a string")

    if not prefix.strip():
        raise InvalidPrefixError("Prefix cannot be empty")


def validate_top_k(top_k: int) -> None:
    """
    Validate top-k parameter.

    Raises:
        InvalidTopKError
    """
    if not isinstance(top_k, int):
        raise InvalidTopKError("top_k must be an integer")

    if top_k <= 0:
        raise InvalidTopKError(
            "top_k must be greater than zero"
        )
