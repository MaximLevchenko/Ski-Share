class ControllerException(Exception):
    """
    Custom exception for the controller level of the application.

    This exception is intended to be raised when there is a problem at the controller level, typically when
    certain conditions or validation checks fail.

    :ivar message: A human-readable error message that describes the reason for the exception.
    :type message: str

    :ivar http_code: The associated HTTP status code for the exception.
    :type http_code: int
    """

    def __init__(self, message, http_code):
        """
        Initialize a new instance of the ControllerException class.

        :param message: A human-readable error message that describes the reason for the exception.
        :type message: str

        :param http_code: The associated HTTP status code for the exception.
        :type http_code: int
        """
        super().__init__(message)
        self.message = message
        self.http_code = http_code
