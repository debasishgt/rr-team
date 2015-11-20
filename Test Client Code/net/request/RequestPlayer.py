from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestPlayer(ServerRequest):


    def send(self, playerCount = None):

        try:
            print "PlayerCount", playerCount
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_PLAYER)
            pkg.addInt32(playerCount)
            self.cWriter.send(pkg, self.connection)

        except:
            self.log('Bad [' + str(Constants.CMSG_PLAYER) + '] Int Request')
            print_exc()
