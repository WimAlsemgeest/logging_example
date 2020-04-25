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

    logger.critical("This is a critical message from a function.")
    logger.error("This is a error message from a function.")
    logger.warning("This is a warning message from a function.")
    logger.info("This is a info message from a function.")
    logger.debug("This is a debug message from a function.")


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

    logger.critical("This is a critical message.")
    logger.error("This is a error message.")
    logger.warning("This is a warning message.")
    logger.info("This is a info message.")
    logger.debug("This is a debug message.")

    example_function()
    myfunctions.some_function()


if __name__ == "__main__":
    main()
