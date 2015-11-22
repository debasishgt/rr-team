from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseSetRank(ServerResponse):

    def execute(self, data):

        try:
            self.rank = data.getInt32()
            print "\nResponseSetRank - ", self.rank

        except:
            self.log('Bad [' + str(Constants.SMSG_SET_RANK) + '] String Response')
            print_exc()
