from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseEnterLobby(ServerResponse):

    def execute(self, data):

        try:
            print "\nResponseEnterLobby - "
            self.username = data.getString()
            self.validate = data.getInt32()
            print self.username
            print self.validate

        except:
            self.log('Bad [' + str(Constants.SMSG_ENTER_LOBBY) + '] String Response')
            print_exc()
