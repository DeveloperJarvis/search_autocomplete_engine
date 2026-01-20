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
# basic_autocomplete MODULE
# --------------------------------------------------
"""
Basic autocomplete example.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from search_autocomplete_engine import (
    AutocompleteEngine, EngineConfig
)


def main() -> None:
    config = EngineConfig(top_k=3)
    engine = AutocompleteEngine(config)

    engine.add_query("apple")
    engine.add_query("app")
    engine.add_query("application")
    engine.add_query("banana")

    prefix = "top"
    suggestions = engine.suggest(prefix)

    print(f"Suggestons for '{prefix}':")
    for s in suggestions:
        print(f" - {s}")
    

if __name__ == "__main__":
    main()
