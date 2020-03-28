import os
import sys
import logging
import logging.config
import yaml

import mymodule.mymodule as myfunctions


def example_function() -> None:
    """Example of logging from a function."""
    logger = logging.getLogger(__name__)
    print("This are messages from a function.")

    logging.critical("This is a critical message from a function.")
    logging.error("This is a error message from a function.")
    logging.warning("This is a warning message from a function.")
    logging.info("This is a info message from a function.")
    logging.debug("This is a debug message from a function.")
    

def main() -> None:
    """Example of logging with yaml file."""

    # ------------------------------------------------------------------------
    #   Loading the yaml file for logging.
    try:
        if os.path.exists('logging.yaml'):
            with open('logging.yaml', 'r') as f:
                config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=logging.INFO)
    except ValueError:
        sys.exit("Error in configuration file detected")

    # ------------------------------------------------------------------------
    #   Doing some tests.
    print("Doing some logging tests.")
    logger = logging.getLogger(__name__)

    logging.critical("This is a critical message.")
    logging.error("This is a error message.")
    logging.warning("This is a warning message.")
    logging.info("This is a info message.")
    logging.debug("This is a debug message.")

    example_function()
    myfunctions.some_function()
    


if __name__ == "__main__":
    main()
