import sys 
##Provide various functions and variables are used to manipulate different parts of the python runtime enviorment
import logging 
def error_message_details(error, error_detail: sys):
    """
    Function to extract error details from an exception
    """
    _, _, exc_tb = error_detail.exc_info()  # Execution info: get traceback details
    file_name = exc_tb.tb_frame.f_code.co_filename  # File name where the error occurred
    error_message = 'Error occurred in Python script name [{0}] line number [{1}] error message [{2}]'.format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        Custom exception class for detailed error reporting
        """
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
