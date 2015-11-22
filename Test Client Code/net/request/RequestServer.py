from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestServer(ServerRequest):


    def send(self, timeStamp = None):

        try:
            #print "PlayerCount", playerCount
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_PLAYER)
            if str(timeStamp).isdigit():
                pkg.addInt32(timeStamp)
            else:
                pkg.addString(timeStamp)
            self.cWriter.send(pkg, self.connection)

        except:
            self.log('Bad [' + str(Constants.CMSG_SERVER) + '] Int Request')
            print_exc()
