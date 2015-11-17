from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseRankings(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getString()
            print "ResponseRankings - ", self.msg

        except:
            self.log('Bad [' + str(Constants.SMSG_RANKINGS) + '] String Response')
            print_exc()
