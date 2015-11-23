from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestEnterGameLobby(ServerRequest):


    def send(self, data = None):

        try:
            user_data = data.split()
            #username = user_data[0]
            gamelobby = user_data[1]
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_ENTER_GAME_NAME)
            #pkg.addString(username)
            pkg.addString(gamelobby)
            self.cWriter.send(pkg, self.connection)

        except:
            self.log('Bad [' + str(Constants.CMSG_ENTER_GAME_NAME) + '] Request')
            print_exc()
