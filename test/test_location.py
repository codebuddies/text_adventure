#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Insert `text_adventure` package to the sys.path so we don't need to
# install the package for testing.
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest

from text_adventure.location import Location

def test_location_instance():
    location = Location(
        id="Dummy",
        description="Dummy location.",
        neighbours={"Other Dummy"}
        )
    assert location.id == "Dummy"
    assert location.description == "Dummy location."
    assert location.neighbours == {"Other Dummy"}

