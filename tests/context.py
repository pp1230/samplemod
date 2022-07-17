# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sample import core, decoration
print(os.path.dirname(__file__))
print(os.path.join(os.path.dirname(__file__), '..'))
print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))