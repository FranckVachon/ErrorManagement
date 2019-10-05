from Drive import Drive
from Exceptions import *

class Builder:
    def __init__(self):
        self.drive = Drive()

    def low_level_error_handling(self):
        try:
            return self.drive.foo_raises_drivevalue_exception(42)                  # exception is raised if value is too high
        except DriveValueException as ex:
            try:
                return self.drive.foo_raises_drivevalue_exception(0)               # catching the exception & trying something else if we can
            except Exception as ex:
                raise BuilderException(f" Couldn't performe action {ex}")   # the last exception should be generic to catch everything

    def server_caught_error(self, arg):
        return self.drive.server_caught_error(arg)                                 # we didn't expect error here so we didn't catch it

    def bar_raises_drive_not_initialized(self):
        return self.drive.use_drive()

    def builder_catches_random_exception(self):
        try:
            self.drive.drive_raise_random_exception()
            print(" BUILDER created more science... ")
            return True
        except DriveNotRespondingException as ex:
            raise BuilderException(ex)
        except DriveNotInitializedException as ex:
            self.drive.init_drive()
            return self.drive.use_drive()
        except DriveException as ex:
            print(f" Generic exception raised by Drive - cause unknown ")
            raise BuilderException(ex)




