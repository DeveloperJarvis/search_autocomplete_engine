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
# interactive_cli MODULE
# --------------------------------------------------
"""
Interactive CLI for the Search Autocomplete Engine.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from search_autocomplete_engine import (
    AutocompleteEngine, EngineConfig,
)


def main() -> None:
    config = EngineConfig(top_k=5)
    engine = AutocompleteEngine(config)

    print("🔍 Search Autocomplete Engine")
    print("Type queries to add them.")
    print("Type '/suggest <prefix>' to get suggestions.")
    print("Type '/exit' to quit.\n")

    while True:
        user_input = input("> ").strip()

        if user_input == "/exit":
            print("Goodbye 👋🏻")
            break

        if user_input.startswith("/suggest"):
            parts = user_input.split(maxsplit=1)
            if len(parts) != 2:
                print("Usage: /suggest <prefix>")
                continue

            prefix = parts[1]
            suggestions = engine.suggest(prefix)

            print("Suggestions:")
            for s in suggestions:
                print(f" - {s}")
        else:
            engine.add_query(user_input)
            print(f"Added query: '{user_input}'")


if __name__ == "__main__":
    main()
