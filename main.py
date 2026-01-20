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
# search_autocomple_engine MODULE
# --------------------------------------------------
"""
CLI Entry point for Search Autocomplete Engine
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
import argparse
from search_autocomplete_engine.core.autocomplete import AutocompleteEngine
from search_autocomplete_engine.config.engine_config import EngineConfig


def parse_args():
    parser = argparse.ArgumentParser(
        description="Search Autocomplete Engine CLI"
    )
    parser.add_argument(
        "--query",
        type=str,
        required=True,
        help="Input prefix for autocomplete",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=5,
        help="Number of suggestions to return",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    print(f"Args: {args}\n")

    config = EngineConfig(top_k=args.top_k)
    engine = AutocompleteEngine(config=config)

    # Seed sample data (could be added by file or db)
    engine.add_query("apple")
    engine.add_query("app")
    engine.add_query("application")
    engine.add_query("banana")
    engine.add_query("band")
    engine.add_query("bandana")

    suggestions = engine.suggest(args.query)

    print("\n🔍 Autocomplete Suggestions:")
    for s in suggestions:
        print(f" - {s}")


if __name__ == "__main__":
    main()
