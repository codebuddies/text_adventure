#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Insert `text_adventure` package to the sys.path so we don't need to
# install the package for testing.
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest

from text_adventure.game import game_loop

def test_game_loop_exit_on_game_end():
    # We test 10 loops before exiting
    count = 0
    def is_game_over():
        nonlocal count
        count += 1
        return count == 10

    game_loop(is_game_over)
    assert count == 10