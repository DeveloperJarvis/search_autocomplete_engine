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
# test_frequency_store MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import pytest
from search_autocomplete_engine.storage.frequency_store import FrequencyStore
from search_autocomplete_engine.exceptions.errors import StorageError


def test_increment_and_get():
    store = FrequencyStore()
    assert store.increment("apple") == 1
    assert store.increment("apple") == 2
    assert store.get("apple") == 2
    assert store.get("banana") == 0


def test_all_returns_dict():
    store = FrequencyStore()
    store.increment("apple")
    store.increment("banana")
    store.increment("banana")
    data = store.all()
    assert data == {"apple": 1, "banana": 2}


def test_increment_empty_query_raises():
    store = FrequencyStore()
    with pytest.raises(StorageError):
        store.increment("")
