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
# test_trie MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import pytest
from search_autocomplete_engine.core.trie import Trie
from search_autocomplete_engine.exceptions.errors import TrieError


def test_trie_insert_and_retrieve():
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("application")

    results = trie.get_queries_with_prefix("app")
    assert results == {"app", "apple", "application"}


def test_trie_empty_insert_raises():
    trie = Trie()
    with pytest.raises(TrieError):
        trie.insert("")


def test_trie_prefix_not_found():
    trie = Trie()
    trie.insert("apple")
    assert trie.get_queries_with_prefix("banana") == set()
