from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseSetPosition(ServerResponse):

    def execute(self, data):

        try:
        	print "\nResponseSetPosition - "
        	self.numberOfUsers = data.getInt32()
        	self.username = data.getString()
        	self.x = data.getFloat32()
        	self.y = data.getFloat32()
        	self.z = data.getFloat32()
        	self.h = data.getFloat32()
        	print self.numberOfUsers
        	print self.username
        	print self.x
        	print self.y
        	print self.z
        	print self.h
            #self.msg = data.getString()

        except:
            self.log('Bad [' + str(Constants.SMSG_SET_POSITION) + '] String Response')
            print_exc()
