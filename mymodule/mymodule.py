"""A function for example an external file logging"""
import logging.config

def some_function() -> None:
    """Create some logging texts."""
    logger = logging.getLogger(__name__)

    print("This are messages from a function in a module.ls")
    logging.critical("This is a critical message from a external function.")
    logging.error("This is a error message from a external function.")
    logging.warning("This is a warning message from a external function.")
    logging.info("This is a info message from a external function.")
    logging.debug("This is a debug message from a external function.")
    