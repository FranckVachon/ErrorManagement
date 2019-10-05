
class DriveException(Exception):
    """ Raised when we have a drive-specific problem """
    def __init__(self, message, drive, *args):
        self.message = message
        self.drive = drive
        super().__init__(message, drive, *args)

class DriveValueException(Exception):
    """ Wrong value is given to the drive """

class DriveNotInitializedException(DriveException):
    """ Exception for when a unitialized drive causes an error """

class DriveNotRespondingException(DriveException):
    """ When a drive times out on a requests or doesn't respond """

class BuilderException(Exception):
    """ Errors class for builder - could subclass that as well as we do for Drives"""