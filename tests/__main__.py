#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

import tests

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###

### MAIN ###
def main():
    # Init Logging
    logging.basicConfig(level=logging.DEBUG)

    # Generate the test suite
    my_test_suite = tests.generate_test_suite()

    # Run the test suite
    runner = unittest.TextTestRunner()
    runner.run(my_test_suite)

if __name__ == '__main__':
    main()
