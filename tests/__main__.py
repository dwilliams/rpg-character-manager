#!/usr/bin/env python3

### IMPORTS ###
import argparse
import logging
import sys
import unittest

import tests

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###

### MAIN ###
def main():
    # Parse Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_const', const=True, default=False, help="Enable debug logging.")
    args = parser.parse_args()

    # Init Logging
    if args.verbose:
        log_format = "%(asctime)s:%(levelname)s:%(name)s.%(funcName)s: %(message)s"
        logging.basicConfig(format=log_format, level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    # Generate the test suite
    my_test_suite = tests.generate_test_suite()

    # Run the test suite
    runner = unittest.TextTestRunner()
    result = runner.run(my_test_suite)
    sys.exit(not result.wasSuccessful())

if __name__ == '__main__':
    main()
