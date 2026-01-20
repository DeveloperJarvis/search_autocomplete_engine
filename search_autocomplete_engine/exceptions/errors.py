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
# errors MODULE
# --------------------------------------------------
"""
Custom exceptions for the Search Autocomplete Engine.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------


# ---------------------------
# autocomplete engine error
# ---------------------------
class AutocompleteEngineError(Exception):
    """
    Base exception for all autocomplete engine errors.
    """
    pass


# ---------------------------
# validation errors
# ---------------------------
class InvalidQueryError(AutocompleteEngineError):
    """Raised when a search query is invalid."""
    pass


class InvalidPrefixError(AutocompleteEngineError):
    """Raised when an autocomplete prefix is invalid."""
    pass


class InvalidTopKError(AutocompleteEngineError):
    """Raised when top_k pararmeter is invalid."""
    pass


# ---------------------------
# core / storage errors
# ---------------------------
class TrieError(AutocompleteEngineError):
    """Raised for trie-related errors."""
    pass


class StorageError(AutocompleteEngineError):
    """Raised for frequency/ storage-related errors."""
    pass
