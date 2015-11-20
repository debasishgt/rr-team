from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseMove(ServerResponse):

    def execute(self, data):

        try:
            self.playerId = data.getInt32()
            self.x = data.getFloat32()
            self.y = data.getFloat32()
            self.z = data.getFloat32()
            self.h = data.getFloat32()
            self.keys = data.getString()


            # Need to set Heading and use keys
            for character in self.world.characters :
              if character.playerId == self.playerId :
                moving_vector = character.actor.getPos()
                character.actor.setPos( moving_vector.getX() + self.x, moving_vector.getY() + self.y, moving_vector.getZ() + self.z)
                break

            print "ResponseMove - ",self.playerId," moved ", self.x, " ", self.y, " ", self.z, " ", self.h

            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.RAND_STRING) + '] String Response')
            print_exc()
