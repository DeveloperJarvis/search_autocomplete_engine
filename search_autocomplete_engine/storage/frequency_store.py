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
# frequency_store MODULE
# --------------------------------------------------
"""
Frequency storage for search queries.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from typing import Dict

from search_autocomplete_engine.exceptions.errors import StorageError


# --------------------------------------------------
# frequency store
# --------------------------------------------------
class FrequencyStore:
    """
    In-memory store for query frequencies.
    """

    def __init__(self) -> None:
        self._frequencies: Dict[str, int] = {}
    
    def increment(self, query: str) -> int:
        """
        Increment frquency count for a query.

        Returns:
            int: Updated frequency
        """
        if not query:
            raise StorageError("Query cannot be empty")
        
        self._frequencies[query] = self._frequencies.get(
                                                query, 0
                                            ) + 1
        return self._frequencies[query]
    
    def get(self, query: str) -> int:
        """
        Get frequemcy for a query.
        """
        return self._frequencies.get(query, 0)
    
    def all(self) -> Dict[str, int]:
        """
        Get all stored frequencies.
        """
        return dict(self._frequencies)
