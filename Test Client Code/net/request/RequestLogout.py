from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestLogout(ServerRequest):


    def send(self, username = None):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_DISCONNECT)
            self.cWriter.send(pkg, self.connection)

        except:
            self.log('Bad [' + str(Constants.CMSG_DISCONNECT) + '] Int Request')
            print_exc()
