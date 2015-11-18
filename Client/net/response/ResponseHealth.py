from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseHealth(ServerResponse):

    def execute(self, data):

        try:
            self.playerId = data.getInt32()
            self.healthChange = data.getInt32()


            # Need to set Heading and use keys
            for character in self.world.characters :
              if character.playerId == self.playerId :
                # character.setHealth(self.healthChange)
                break

            print "ResponseMove - ",self.playerId," moved ", self.x, " ", self.y, " ", self.z, " ", self.h

            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.RAND_STRING) + '] String Response')
            print_exc()
