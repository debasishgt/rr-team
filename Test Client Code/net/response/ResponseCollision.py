from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseCollision(ServerResponse):

    def execute(self, data):

        try:
            self.validate = data.getInt32()
            print "\nResponseCollision - ", self.validate

        except:
            self.log('Bad [' + str(Constants.SMSG_COLLISION) + '] String Response')
            print_exc()
