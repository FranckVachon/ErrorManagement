from DataSource import DataSource
import time

class DekkoServer:
    def __init__(self):
        self.datasource = DataSource()

    def low_level_error_handling(self):
        resp = self.datasource.low_level_error_handling()
        print(resp)

    def server_caught_error(self, arg):
        print(f" Calling DS with value {arg}")

        try:
            if self.datasource.server_caught_error(arg):
                """ do_stuff(), we know the command succeeded since it returned true """
        except Exception as ex:
            print(f" Server caught an unexpected error with value {arg}. Exception raised: {ex}")

    def server_burried_the_exception(self):
        try:
            self.datasource.generate_keyrror_exception()
        except:
            print("I burried the exception so you have no clue what went wrong. Don't thank me.")

    def builder_catches_random_exception(self):
        resp =  self.datasource.builder_catches_random_exception()
        print(f"Response from datasource: {resp}")

    def generate_straight_exception(self, arg):
        self.datasource.uncaught_exception()


    def server_uncaught_error(self):
        time.sleep(1)                                       # just so we don't mess up all the display from previous caught exceptions
        self.datasource.bar_raises_drive_not_initialized()

if __name__ == '__main__':

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

    """ DO NOT burry exception - this way the cause of the error won't bubble up."""
    print("")
    srv.server_burried_the_exception()
    print("-----------------------")


    """ And an uncaught exception to finish things nicely."""
    print("")
    srv.server_uncaught_error()
    print("-----------------------")

