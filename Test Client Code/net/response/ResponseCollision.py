from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseCollision(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getString()
            print "ResponseCollision - ", self.msg

        except:
            self.log('Bad [' + str(Constants.SMSG_COLLISION) + '] String Response')
            print_exc()
