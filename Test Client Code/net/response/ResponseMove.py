from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseMove(ServerResponse):

    def execute(self, data):

        try:
            print "\nResponseMove - "
            self.user = data.getString()
            self.x = data.getFloat32()
            self.y = data.getFloat32()
            self.z = data.getFloat32()
            self.h = data.getFloat32()
            self.p = data.getFloat32()
            self.r = data.getFloat32()
            self.keys = data.getString()

            print self.user
            print self.x
            print self.y
            print self.z
            print self.h
            print self.p
            print self.r
            print self.keys
            
        except:
            self.log('Bad [' + str(Constants.SMSG_MOVE) + '] String Response')
            print_exc()
