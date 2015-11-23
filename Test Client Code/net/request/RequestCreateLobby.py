from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestCreateLobby(ServerRequest):


    def send(self, data = None):

        try:
            user_data = data.split()
            groupName = user_data[0]
            gamemodeid = int(user_data[1])
            status = int(user_data[2])
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_CREATE_LOBBY)
            pkg.addString(groupName)
            pkg.addInt32(gamemodeid)
            pkg.addInt32(status)
            self.cWriter.send(pkg, self.connection)

        except:
            self.log('Bad [' + str(Constants.CMSG_CREATE_LOBBY) + '] Request')
            print_exc()
