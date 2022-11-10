#!/usr/bin/python3

# Copyright (c) 2022 Humanitarian OpenStreetMap Team
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import logging
from sys import argv
import os
import epdb
import argparse
import sys
from progress.bar import Bar, PixelBar
from progress.spinner import PixelSpinner
from codetiming import Timer
import concurrent.futures
from cpuinfo import get_cpu_info
from tagchecks import TagChecks
from buildingchecks import BuildingChecks

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process OSM data for quality issues')
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose output")
    parser.add_argument("-y", "--yaml", help="Alternate YAML file")
    parser.add_argument("-i", "--infile", help='The input file')
    parser.add_argument("-b", "--boundary", help='The boundary file')
    args = parser.parse_args()

    # if verbose, dump to the terminal.
    if args.verbose is not None:
        root = logging.getLogger()
        # This gets mesages from the imported modules too. More verbose, but useful
        root.setLevel(logging.DEBUG)

        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        root.addHandler(ch)

    # Needs command line arguments to actually do anything
    if len(argv) == 1:
        # parser.print_help()
        parser.print_usage()

