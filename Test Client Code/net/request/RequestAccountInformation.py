from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestAccountInformation(ServerRequest):


    def send(self, username = None):

        try:
            user_data = username.split()
            username = user_data[0]
            email = user_data[1]
            print username
            print email
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_FORGOT_PASSWORD)
            pkg.addString(username)
            pkg.addString(email)
            self.cWriter.send(pkg, self.connection)

            #self.log('Sent [' + str(Constants.RAND_STRING) + '] Int Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_FORGOT_PASSWORD) + '] Request')
            print_exc()
