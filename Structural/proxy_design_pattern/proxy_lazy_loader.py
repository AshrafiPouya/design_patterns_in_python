import time
from time import sleep

class LazyHandler:
    def __init__(self, cls) -> None:
        self.cls = cls
        self.object = None


    def __getattr__(self, item) -> None:
        if self.object == None:
            self.object = self.cls()

        return getattr(self.object, item)

class DataBaseHandler:
    def __init__(self, port = None) -> None:
        self.port = port if port else 5432
        sleep(2)

    def check_connection(self):
        return f"connected to database on port {self.port}"
    
    
    def change_port(self, port):
        self.port = port

        return self.port


class RedisHandler:
    def __init__(self) -> None:
        sleep(5)

    def check_connection(self):
        return f"connected to Redis"
    
class OthersHandler:
    def __init__(self) -> None:
        sleep(20)

    def check_connection(self):
        return f"connected to others"


if __name__ == "__main__":

    # dont take time to connect until use one these
    dlh1 = LazyHandler(DataBaseHandler)
    dlh2 = LazyHandler(DataBaseHandler)
    dlh3 = LazyHandler(DataBaseHandler)
    rlh2 = LazyHandler(RedisHandler)
    olh3 = LazyHandler(OthersHandler)

    # takes time to connect
    print(dlh1.check_connection())
    # no time need to connect for these two
    print(dlh1.check_connection())
    print(dlh1.check_connection())

    print(dlh1.change_port(4444))
    print(dlh1.check_connection())




