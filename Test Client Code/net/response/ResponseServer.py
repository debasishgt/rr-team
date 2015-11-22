from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseServer(ServerResponse):

    def execute(self,conn, data):

        try:
            self.msg = data.getString()
            print "Request from Server - ", self.msg
            conn.sendRequest(Constants.CMSG_SERVER,self.msg)

        except:
            self.log('Bad [' + str(Constants.SMSG_TIMER) + '] String Response')
            print_exc()
