from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseEnterGameLobby(ServerResponse):

    def execute(self, data):

        try:
            print "\nResponseEnterGameName - "
            self.username = data.getString()
            self.validate = data.getInt32()
            print self.username
            print self.validate

        except:
            self.log('Bad [' + str(Constants.SMSG_ENTER_GAME_NAME) + '] String Response')
            print_exc()
