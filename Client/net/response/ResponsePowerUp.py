from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponsePowerUp(ServerResponse):

    def execute(self, data):

        try:
            username = data.getInt32()
            powerId = data.getInt32()


            # Need to set Heading and use keys
            for character in self.world.characters :
              if character.username == username :
                # Sends a visual effect from the character model
                # Also hides the powerId from the map until it respawns.
                break

            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

            print "ResponsePowerUp - ", username, " ", powerId

        except:
            self.log('Bad [' + str(Constants.SMSG_POWER_UP) + '] Power Up Response')
            print_exc()
