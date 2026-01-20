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
# test_ranker MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from search_autocomplete_engine.core.ranker import Ranker
from search_autocomplete_engine.storage.frequency_store import FrequencyStore


def test_ranker_orders_by_frequency_and_lex():
    store = FrequencyStore()
    store.increment("banana")
    store.increment("apple")
    store.increment("apple")
    store.increment("application")
    ranker = Ranker(store)

    results = ranker.rank(
        {"apple", "banana", "application"}, top_k=3
    )
    # frequency apple=2, banana=1, application=1
    assert results == ["apple", "application", "banana"]


def test_ranker_top_k_limit():
    store = FrequencyStore()
    for q in ["a", "b", "c", "d"]:
        store.increment(q)
    ranker = Ranker(store)
    results = ranker.rank({"a", "b", "c", "d"}, top_k=2)
    assert len(results) == 2
