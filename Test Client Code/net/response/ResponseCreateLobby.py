from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseCreateLobby(ServerResponse):

    def execute(self, data):

        try:
            print data
            print "\nResponseCreateLobby - "
            self.username = data.getString()
            self.validate = data.getInt32()
            print self.username
            print self.validate

        except:
            self.log('Bad [' + str(Constants.SMSG_CREATE_LOBBY) + '] String Response')
            print_exc()
