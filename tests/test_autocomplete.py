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
# test_autocomplete MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import pytest
from search_autocomplete_engine.core.autocomplete import AutocompleteEngine
from search_autocomplete_engine.config.engine_config import EngineConfig
from search_autocomplete_engine.exceptions.errors import InvalidQueryError, InvalidPrefixError


@pytest.fixture
def engine():
    config = EngineConfig(top_k=3)
    return AutocompleteEngine(config=config)


def test_add_and_suggest(engine):
    engine.add_query("apple")
    engine.add_query("app")
    engine.add_query("application")
    suggestions = engine.suggest("app")
    assert set(suggestions) == {"app", "apple", "application"}


def test_invalid_query_raises(engine):
    with pytest.raises(InvalidQueryError):
        engine.add_query("")    # empty query
    with pytest.raises(InvalidQueryError):
        engine.add_query(None)


def test_invalid_prefix_raises(engine):
    engine.add_query("apple")
    with pytest.raises(InvalidPrefixError):
        engine.suggest("")  # empty prefix
    with pytest.raises(InvalidPrefixError):
        engine.suggest(None)
