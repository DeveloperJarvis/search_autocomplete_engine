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
# setup MODULE
# --------------------------------------------------
"""
Search Autocomplete Engine
Setup Script
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from setuptools import setup, find_packages
from pathlib import Path

ROOT = Path(__file__).parent


setup(
    name="search-autocomplete-engine",
    version="0.1.0",
    description="Trie-based search autocomplete engine with frequency ranking",
    long_description=(ROOT / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    author="Developer Jarvis",
    author_email="developerjarvis@github.com",
    url="https://github.com/DeveloperJarvis/search_autocomplete_engine",
    license="GPL-3.0-or-later",
    packages=find_packages(
        exclude=["tests*", "examples*", "logs*"]
    ),
    python_requires=">=3.9",
    install_requires=[
        "typing-extensions>=4.0.0"
    ],
    extras_require={
        "dev": [
            "pytest",
            "black",
            "flake8",
            "mypy",
        ]
    },
    entry_points={
        "console_scripts": [
            # "example1=examples.basic_autocomplete:main",
            # "example2=examples.frequency_demo:main",
            # "example3=examples.interactive_cli:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Education",
    ],
    include_package_data=True,
    zip_safe=False,
)
