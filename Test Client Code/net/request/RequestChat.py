from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestChat(ServerRequest):


    def send(self, message = None):

        try:
            print message
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_CHAT)
            pkg.addString(message)
            self.cWriter.send(pkg, self.connection)

            #self.log('Sent [' + str(Constants.RAND_STRING) + '] Int Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_CHAT) + '] Request')
            print_exc()
