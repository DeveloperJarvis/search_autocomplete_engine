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
# trie MODULE
# --------------------------------------------------
"""
Trie implementation for prefix-based indexing.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from search_autocomplete_engine.models.trie_node import TrieNode
from search_autocomplete_engine.exceptions.errors import TrieError


# --------------------------------------------------
# trie
# --------------------------------------------------
class Trie:
    """
    Trie data structure for storing query prefixes.
    """

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, query: str) -> None:
        """
        Insert a query into the table.
        """
        if not query:
            raise TrieError("Cannot insert empty query")
        
        node = self.root
        for char in query:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.queries.add(query)
        
        node.is_end = True
    
    def get_queries_with_prefix(self, prefix: str) -> set[str]:
        """
        Retrieve all queries matching a prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return set()
            node = node.children[char]
        
        return set(node.queries)
