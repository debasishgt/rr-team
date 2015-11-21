from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponsePowerPickUp(ServerResponse):

    def execute(self, data):

        try:
            self.validate = data.getInt32()


            # If returns 1 Gives the player the Item based on what they hit

            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_POWER_UP_PICK_UP) + '] Power Pick Up Response')
            print_exc()
