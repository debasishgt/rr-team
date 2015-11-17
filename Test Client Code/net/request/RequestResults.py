from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestResults(ServerRequest):


    def send(self, gameId = None):

        try:
            print gameId
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_RESULTS)
            pkg.addInt32(gameId)
            self.cWriter.send(pkg, self.connection)
        except:
            self.log('Bad [' + str(Constants.CMSG_RESULTS) + '] Request')
            print_exc()
