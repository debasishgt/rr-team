from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseCreateCharacter(ServerResponse):
    def execute(self, data):
        try:
            self.msg = data.getInt32()
            print "ResponseCreateCharacter - ", self.msg

        except:
            self.log('Bad [' + str(Constants.RAND_STRING) + '] String Response')
            print_exc()
