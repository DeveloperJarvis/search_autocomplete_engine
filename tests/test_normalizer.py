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
# test_normalizer MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import pytest
from search_autocomplete_engine.utils.normalizer import normalize_query


def test_normalize_basic():
    assert normalize_query("  APPle ") == "apple"
    assert normalize_query("PyTest") == "pytest"


def test_normalize_empty_and_none():
    assert normalize_query("") == ""
    assert normalize_query(None) == ""


def test_normalize_invalid_type_raises():
    with pytest.raises(TypeError):
        normalize_query(123)
