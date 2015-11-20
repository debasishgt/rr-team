from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseDead(ServerResponse):

    def execute(self, data):

        try:
            self.playerId = data.getInt32()


            # Need to have a variable checking if the character is alive
            for character in self.world.characters :
              if character.playerId == self.playerId :
                #character.dead = True
                break

            print "ResponseMove - ",self.playerId
            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.RAND_STRING) + '] String Response')
            print_exc()
