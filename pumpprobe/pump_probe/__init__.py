# -*- coding: utf-8 -*-
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# pylint: disable=wrong-import-order
# pylint: disable=wrong-import-position
"""Pump probe Metal"""
__version__ = '1.0.1'
__license__ = "Apache 2.0"
__author__ = 'Zixiao Wang'
__status__ = "Development"

###########################################################################
### Windows OS catch for library geopandas not installed with setup.py

from . import filedata
from . import filesort

