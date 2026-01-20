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
# autocomplete MODULE
# --------------------------------------------------
"""
Autocomplete engine implementation
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from search_autocomplete_engine.config.engine_config import EngineConfig
from search_autocomplete_engine.core.trie import Trie
from search_autocomplete_engine.core.ranker import Ranker
from search_autocomplete_engine.storage.frequency_store import FrequencyStore
from search_autocomplete_engine.utils.normalizer import normalize_query
from search_autocomplete_engine.utils.validators import (
    validate_query,
    validate_prefix,
)
from search_autocomplete_engine.utils.logging import get_logger


# --------------------------------------------------
# autocomplete engine
# --------------------------------------------------
class AutocompleteEngine:
    """
    Trie-based search autocomplete engine.
    """

    def __init__(self, config: EngineConfig) -> None:
        self.config = config
        self._trie = Trie()
        self._frequency_store = FrequencyStore()
        self._ranker = Ranker(self._frequency_store)
        self._logger = get_logger(self.__class__.__name__)
    
    def add_query(self, query: str) -> None:
        """
        Add a query to the engine and update its frequency.
        """
        validate_query(query)
        normalized = normalize_query(query)
        if not normalized:
            return

        self._frequency_store.increment(normalized)
        self._trie.insert(normalized)

        self._logger.debug("Add query: %s", normalized)
    
    def suggest(self, prefix: str) -> list[str]:
        """
        Return ranked autocomplete suggestions for a prefix.
        """
        validate_prefix(prefix)
        normalized = normalize_query(prefix)
        if not normalized:
            return

        queries = self._trie.get_queries_with_prefix(normalized)
        suggestions = self._ranker.rank(
            queries,
            top_k=self.config.top_k,
        )

        self._logger.debug(
            "Suggestions for '%s': %s", normalized, suggestions
        )
        return suggestions
