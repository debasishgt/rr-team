from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestDead(ServerRequest):


    def send(self, dead = None):

        try:
            print dead
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_DEAD)
            #pkg.addInt32(dead)
            self.cWriter.send(pkg, self.connection)
        except:
            self.log('Bad [' + str(Constants.CMSG_DEAD) + '] Request')
            print_exc()
