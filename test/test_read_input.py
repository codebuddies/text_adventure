#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Insert `text_adventure` package to the sys.path so we don't need to
# install the package for testing.
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest

from text_adventure.player_input import read_input

def test_read_input_move_to(monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', lambda x: "Move to some location")
    # For the moment we can only `go to` some location.
    command, *args = read_input()

    assert command == "move_to"
    assert args == ("some location",)

def test_read_input_move_to_all_caps(monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', lambda x: "MOVE TO some location")
    command, *args = read_input()

    assert command == "move_to"
    assert args == ("some location",)

def test_read_input_unknown_commant(monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', lambda x: "unknown command")
    command, *args = read_input()

    assert commant == "unknown"
    assert args == tuple()
