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
            email = user_data[2]
            print username
            print password
            print email
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_AUTH)
            pkg.addString(username)
            pkg.addString(password)
            pkg.addString(email)
            self.cWriter.send(pkg, self.connection)

        except:
            self.log('Bad [' + str(Constants.CMSG_REGISTER) + '] Int Request')
            print_exc()
