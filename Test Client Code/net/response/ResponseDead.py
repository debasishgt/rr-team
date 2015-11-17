from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseDead(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getString()
            print "ResponseDead - ", self.msg

        except:
            self.log('Bad [' + str(Constants.SMSG_AUTH) + '] String Response')
            print_exc()
