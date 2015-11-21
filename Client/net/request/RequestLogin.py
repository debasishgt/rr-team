from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestLogin(ServerRequest):


    def send(self, username = None, password = None):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_LOGIN)
            pkg.addString(username)
            pkg.addString(password)

            self.cWriter.send(pkg, self.connection)
            
        except:
            self.log('Bad [' + str(Constants.CMSG_LOGIN) + '] Login Request')
            print_exc()
