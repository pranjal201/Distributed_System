# TabNine::sem

import rpyc
import math
from rpyc.utils.server import OneShotServer


class MyService(rpyc.Service):
    def exposed_square(self, a):
        return a**2

    def exposed_squareroot(self, a):
        return math.sqrt(a)


if __name__ == "__main__":
    server = OneShotServer(MyService, port=5555)
    server.start()
    server.accept()
    server.close()
