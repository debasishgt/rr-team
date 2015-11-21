from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseLogin(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getString()

            print "ResponseLogin - ", self.msg

        except:
            self.log('Bad [' + str(Constants.SMSG_LOGIN) + '] Login Response')
            print_exc()
