from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseLogin(ServerResponse):

    def execute(self, data):

        try:
            print data
            self.msg = data.getInt32()
            print "ResponseLogin - ", self.msg

        except:
            self.log('Bad [' + str(Constants.SMSG_AUTH) + '] String Response')
            print_exc()
