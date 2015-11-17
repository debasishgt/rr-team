from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestReady(ServerRequest):


    def send(self, ready = None):

        try:
            print ready
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_READY)
            pkg.addInt32(ready)
            self.cWriter.send(pkg, self.connection)
        except:
            self.log('Bad [' + str(Constants.CMSG_READY) + '] Request')
            print_exc()
