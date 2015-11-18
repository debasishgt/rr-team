from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseMove(ServerResponse):

    def execute(self, data):

        try:
            self.damage = data.getInt32()

            # I think we are going to have 1 returned to the user, after the Server
            # Registers that they took damage.

            print "ResponseMove - ", damage

            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.RAND_STRING) + '] String Response')
            print_exc()
