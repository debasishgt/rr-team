from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestPowerUpPickUp(ServerRequest):


    def send(self, powerId = None):

        try:
            print powerId
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_POWER_PICKUP)
            pkg.addInt32(powerId)
            self.cWriter.send(pkg, self.connection)
        except:
            self.log('Bad [' + str(Constants.CMSG_POWER_PICKUP) + '] Request')
            print_exc()
