from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseDead(ServerResponse):

    def execute(self, data):

        try:
            self.username = data.getString()
            print "ResponseDead - ", self.username

        except:
            self.log('Bad [' + str(Constants.SMSG_AUTH) + '] String Response')
            print_exc()
