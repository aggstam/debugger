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

import inspect

def breakpoint(obj=None, verbose=False):
    # Invoking inspect to retrieve stack info.
    # 1 represents caller line
    callerframerecord = inspect.stack()[1]
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)

    # Printing the breakpoint
    print("------Breakpoint------")
    if verbose:
        print("File: ", info.filename)
        print("Function: ", info.function)
    print("Line: ", info.lineno)
    if obj is not None:
        print("Value: ", obj)
    print("----------------------")

