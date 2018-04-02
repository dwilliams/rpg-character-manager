#!/usr/bin/env python3

### IMPORTS ###
import argparse
import logging
import secrets

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class DieInvalidNumberOfSidesException(Exception):
    pass

class DieNotRolledException(Exception):
    pass

class DieToRoll:
    def __init__(self, num_sides = 6, success_above = 4):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing Die with %d sides and success above %d", num_sides, success_above)

        self.last_roll = None
        if num_sides < 2:
            raise DieInvalidNumberOfSidesException()
        self.num_sides = num_sides
        self.success_above = success_above

    def get_last_roll(self):
        if self.last_roll is None:
            raise DieNotRolledException()
        return self.last_roll

    def get_is_success(self):
        if self.last_roll is None:
            raise DieNotRolledException()
        if self.last_roll > self.success_above:
            return True
        return False

    def roll(self):
        self.last_roll = secrets.randbelow(self.num_sides) + 1
        return self.get_last_roll(), self.get_is_success()

### MAIN ###
def main():
    # Init Logging
    logging.basicConfig(level=logging.INFO)

    # ArgParse
    parser = argparse.ArgumentParser(description = "Roll some dice")
    parser.add_argument('--count_success', action='store_const', const=True, help="Whether to count the number of successes", default=False)
    parser.add_argument('--success_above', type=int, help="The number above which each die is counted a success (default: 4)", default=4)
    parser.add_argument('--num_sides', type=int, help="Number of sides for the dice (default: 6)", default=6)
    parser.add_argument('num_dice', type=int, help="Number of dice to roll")
    args = parser.parse_args()

    logging.debug("Args: %s", str(args))

    # Create the dice
    dice_list = []
    for i in range(args.num_dice):
        logging.debug("Creating die %d", i)
        dice_list.append(DieToRoll(args.num_sides, args.success_above))

    # Roll the dice
    for tmp_die in dice_list:
        logging.debug("Rolling die %s", str(tmp_die))
        tmp_number, tmp_success = tmp_die.roll()
        logging.debug("Result: %d, %s", tmp_number, str(tmp_success))

    # Display the result
    result_string = ""
    success_count = 0
    if args.count_success:
        for tmp_die in dice_list:
            if tmp_die.get_is_success():
                success_count = success_count + 1
                result_string = "{}\033[1;32m{}\033[0m ".format(result_string, tmp_die.get_last_roll())
            else:
                result_string = "{}{} ".format(result_string, tmp_die.get_last_roll())
        result_string = "{} Success Count: {}".format(result_string, success_count)
    else:
        result_string = " ".join([str(d.get_last_roll()) for d in dice_list])
    logging.info("Rolls: %s", result_string)

if __name__ == '__main__':
    main()
