import sys
from networksecurity.logging import logger


class NetworkSecurityException(Exception):
    """Custom exception class for the Network Security project.

    Captures and formats error details including the filename and line number
    where the exception occurred, providing richer context for debugging.
    """

    def __init__(self, error_message, error_details: sys):
        """Initialize the exception with a message and system error details.

        Args:
            error_message: The original error message or exception instance.
            error_details: The ``sys`` module, used to extract traceback info.
        """
        self.error_message = error_message
        # Extract traceback object to get file name and line number
        _, _, exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        """Return a formatted string with file name, line number, and error message."""
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message))


if __name__ == '__main__':
    # Simple self-test: trigger a ZeroDivisionError and wrap it
    try:
        logger.logging.info("Enter the try block")
        a = 1 / 0
        print("This will not be printed", a)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
