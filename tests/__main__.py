#!/usr/bin/env python3

### IMPORTS ###
import argparse
import logging
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
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    # Generate the test suite
    my_test_suite = tests.generate_test_suite()

    # Run the test suite
    runner = unittest.TextTestRunner()
    runner.run(my_test_suite)

if __name__ == '__main__':
    main()
