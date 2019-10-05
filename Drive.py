from Exceptions import *
from utils import *
import random

class Drive:
    def __init__(self):
        self.is_initialized = False

    def init_drive(self):
        self.is_initialized = True

    def foo_raises_drivevalue_exception(self, arg):
        """ Raises a drive Exception"""
        print(f".... DRIVE attempting to create science .... value {arg}")
        if arg >= 42:
            raise DriveValueException(" ... low level drive exception details ...", DriveEnum.KOLLMORGAN, arg)
        else:
            print(f"... DRIVE created more science .... value {arg}")
            return True                                                                         # at low-level, ideally return True for succesfull commands


    def server_caught_error(self, arg):
        raise DriveException(f" Drive can't do that {arg}", DriveEnum.KOLLMORGAN)

    def drive_raise_random_exception(self):
        err = random.randint(0,4)
        if err == 0:
            raise DriveNotInitializedException(" Random drive exception ", DriveEnum.THORLABS)
        elif err == 1:
            raise DriveNotRespondingException( " Random drive exception ", DriveEnum.KOLLMORGAN )
        elif err == 2:
            raise DriveException (" Random drive exception ", DriveEnum.FPGA)
        else:
            return True                                                                                        # succeeded this time


    def use_drive(self):
        if self.is_initialized:
            print(" ... DRIVE created more science ... ")
            return True
        else:
            raise DriveNotInitializedException (" Please initialize drive before use", DriveEnum.THORLABS)