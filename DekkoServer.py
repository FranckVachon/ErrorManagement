from DataSource import DataSource
from Exceptions import *
import time

class DekkoServer:
    def __init__(self):
        self.datasource = DataSource()

    def low_level_error_handling(self):
        resp = self.datasource.low_level_error_handling()
        print(resp)

    def server_caught_error(self, arg):
        """ Calls a method that generates a DriveException"""
        print(f" Calling DS with value {arg}")

        try:
            if self.datasource.server_caught_error(arg):
                """ do_stuff(), we know the command succeeded since it returned true """



        except Exception as ex:
            print(f" Server caught an unexpected error with value {arg}. Exception raised: {ex}")

    def builder_catches_random_exception(self):
        resp =  self.datasource.builder_catches_random_exception()
        print(resp)

    def generate_straight_exception(self, arg):
        self.datasource.uncaught_exception()

    def generate_uncaught_exception(self, arg):
        self.datasource.uncaught_exception()


if __name__ == '__main__':
    import sys

    srv = DekkoServer()

    """ The error is handled at a low-level. Maybe corrective action can be taken to correct the error.
    Notice how nothing in the output shows anything. We could still log the error separetely in the logs if
    desired, but the user need not know anything happened. """
    print("")
    srv.low_level_error_handling()
    print("-----------------------")

    """ Bubbled up error. Some error happens low, and bubbles all the way up. We didn't have anything in place 
     at a lower level to catch it - something unexpected happened. We can do anything about, but catching it 
     prevents the server from stopping/crashing. So maybe the acquisition didn't start, but the server still runs,
      so the user could still re-try to start the acquistion. """
    print("")
    srv.server_caught_error(" 50 000rpm ")
    print("-----------------------")


    """ The builder will get a random exception from the drive"""
    print("")
    srv.builder_catches_random_exception()
    print("-----------------------")


