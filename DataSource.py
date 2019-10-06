from Builder import Builder
from Exceptions import BuilderException

class DataSource:
    def __init__(self):
        self.builder = Builder()

    def low_level_error_handling(self):
        return self.builder.low_level_error_handling()

    def server_caught_error(self, arg):
        print(f" Datasource: calling builder with value {arg}")
        return self.builder.server_caught_error(arg)                           # still didn't catch it

    def bar_raises_drive_not_initialized(self):
        return self.builder.bar_raises_drive_not_initialized()

    def builder_catches_random_exception(self):
        try:
            return self.builder.builder_catches_random_exception()
        except BuilderException as ex:
            print(f" Datasource got exception from builder: {ex}")
        except Exception as ex:
            print(f" Unknown generic exception caught in datasource {ex}")

    def generate_keyrror_exception(self):
        d = dict()
        print(d['unknown_key'])

    def uncaught_exception(self):
        raise Exception(" That didnt work out well... ")