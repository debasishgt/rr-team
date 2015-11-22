from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestPrizes(ServerRequest):


    def send(self, username = None):

        try:
            print username
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_PRIZES)
            pkg.addString(username)
            self.cWriter.send(pkg, self.connection)
        except:
            self.log('Bad [' + str(Constants.CMSG_PRIZES) + '] Request')
            print_exc()
