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
# ranker MODULE
# --------------------------------------------------
"""
Ranking logic for autocomplete suggestions.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from typing import List

from search_autocomplete_engine.storage.frequency_store import FrequencyStore


# --------------------------------------------------
# ranker
# --------------------------------------------------
class Ranker:
    """
    Ranks queries based on frequency and lexicographical order.
    """

    def __init__(self, frquency_store: FrequencyStore) -> None:
        self._frquency_store = frquency_store

    def rank(self, queries: set[str], top_k: int) -> List[str]:
        """
        Rank queries by:
        1. Frequency (descending)
        2. Lexicographical order (ascending)
        """
        sorted_queries = sorted(
            queries,
            key=lambda q: (-self._frquency_store.get(q), q),
        )
        return sorted_queries[:top_k]
