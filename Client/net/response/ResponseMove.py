from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseMove(ServerResponse):

    def execute(self, data):

        try:
            username = data.getInt32()
            x = data.getFloat32()
            y = data.getFloat32()
            z = data.getFloat32()
            h = data.getFloat32()
            p = data.getFloat32()
            r = data.getFloat32()
            keys = data.getString()


            # Need to set Heading and use keys
            for character in self.world.characters :
              if character.username == username :
                moving_vector = character.actor.getPos()
                character.actor.setPos( moving_vector.getX() + self.x, moving_vector.getY() + self.y, moving_vector.getZ() + self.z)
                break

            print "ResponseMove - ",username," moved ", x, " ", y, " ", z, " ", h, " ", p, " ", r

            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_MOVE) + '] Move Response')
            print_exc()
