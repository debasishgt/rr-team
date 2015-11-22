from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseChangeHealth(ServerResponse):

    def execute(self, data):

        try:
            username = data.getInt32()
            healthChange = data.getInt32()


            # Need to set Heading and use keys
            for character in self.world.characters :
              if character.playerId == self.playerId :
                # character.setHealth(self.healthChange)
                break

            print "ResponseChangeHealth - ",username, " ", healthChange

        except:
            self.log('Bad [' + str(Constants.RAND_STRING) + '] String Response')
            print_exc()
