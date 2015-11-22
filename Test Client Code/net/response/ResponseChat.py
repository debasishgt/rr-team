from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseChat(ServerResponse):

    def execute(self, data):

        try:
            self.user = data.getString()
            self.msg  = data.getString() 
            print "ResponseChat - ", self.user, self.msg

        except:
            self.log('Bad [' + str(Constants.SMSG_CHAT) + '] String Response')
            print_exc()
