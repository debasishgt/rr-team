from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestRegistration(ServerRequest):


    def send(self, username = None):

        try:
            user_data = username.split()
            username = user_data[0]
            password = user_data[1]
            print username
            print password
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_REGISTER)
            pkg.addString(username)
            pkg.addString(password)
            self.cWriter.send(pkg, self.connection)

        except:
            self.log('Bad [' + str(Constants.CMSG_REGISTER) + '] Int Request')
            print_exc()
