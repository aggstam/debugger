# --------------------------------------------------------------------------
#
# Simplifying the proper way to debug a program. 
# Check provided README.md for usage examples.
#
# Author: Aggelos Stamatiou, July 2022
#
# This source code is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this source code. If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------------

import unittest
from __init__ import breakpoint as b

class TestBreakpoint(unittest.TestCase):

    def test_normal(self):
        print("\nNormal breakpoint:")
        b()

    def test_verbose(self):
        print("\nVerbose breakpoint:")
        b(None, True)

    def test_value(self):
        print("\nPassing object to print value:")
        x = 42
        b(x)
    
    def test_verbose_vaue(self):
        print("\nVerbose breakpoint with object value:")
        x = 42
        b(x, True)

if __name__ == '__main__':
    unittest.main()
