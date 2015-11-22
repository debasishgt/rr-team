from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseTime(ServerResponse):

    def execute(self, data):

        try:
            time = data.getInt64()

            # I think we are going to have 1 returned to the user, after the Server
            # Registers that they took damage.

        except:
            self.log('Bad [' + str(Constants.SMSG_SET_RANK) + '] Time Response')
            print_exc()
