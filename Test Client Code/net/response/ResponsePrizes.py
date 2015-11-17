from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponsePrizes(ServerResponse):

    def execute(self, data):
    	
        try:
            self.msg = data.getString()
            print "ResponsePrizes - ", self.msg

        except:
            self.log('Bad [' + str(Constants.SMSG_PRIZES) + '] String Response')
            print_exc()
