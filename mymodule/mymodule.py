"""A function for example an external file logging"""
import logging.config


def some_function() -> None:
    """Create some logging texts."""
    logger = logging.getLogger(__name__)

    print("This are messages from a function in a module.ls")
    logger.critical("This is a critical message from a external function.")
    logger.error("This is a error message from a external function.")
    logger.warning("This is a warning message from a external function.")
    logger.info("This is a info message from a external function.")
    logger.debug("This is a debug message from a external function.")
