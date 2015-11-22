from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestCollision(ServerRequest):


    def send(self, data = None):

        try:
            user_data = data.split()
            playerid = int(user_data[0])
            damage = int(user_data[1])
            print playerid
            print damage
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_COLLISION)
            pkg.addInt32(playerid)
            pkg.addInt32(damage)
            self.cWriter.send(pkg, self.connection)
        except:
            self.log('Bad [' + str(Constants.CMSG_COLLISION) + '] Request')
            print_exc()
