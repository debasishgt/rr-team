from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestEnterGameLobby(ServerRequest):


    def send(self, data = None):

        try:
            user_data = data.split()
            username = user_data[0]
            gameid = int(user_data[1])
            lobbyid = int(user_data[2])
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_ENTER_GAME_LOBBY)
            pkg.addString(username)
            pkg.addInt32(gameid)
            pkg.addInt32(lobbyid)
            self.cWriter.send(pkg, self.connection)

        except:
            self.log('Bad [' + str(Constants.CMSG_ENTER_GAME_LOBBY) + '] Request')
            print_exc()
