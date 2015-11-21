from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseDead(ServerResponse):

    def execute(self, data):

        try:
            selfusername = data.getInt32()


            # Need to have a variable checking if the character is alive
            for character in self.world.characters :
              if character.username == self.username :
                #character.dead = True
                break

            print "ResponseDead - ",self.username
            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_DEAD) + '] Dead Response')
            print_exc()
