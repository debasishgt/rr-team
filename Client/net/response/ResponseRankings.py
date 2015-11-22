from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseRankings(ServerResponse):

    def execute(self, data):

        try:
            playerCount = data.getInt32()
            rankings = {data.getString() : data.getInt32()}

            # for x in range(0, self.playerCount-1)
            #     self.rankings[data.getString()] = data.getInt32()

            print "ResponseRankings - ", playerCount

            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_RANKINGS) + '] Rankings Response')
            print_exc()
