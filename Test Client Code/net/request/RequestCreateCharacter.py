from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestCreateCharacter(ServerRequest):


    def send(self, username = None):

        try:
            user_data = username.split()
            charName = user_data[0]
            classType = int(user_data[1])
            print charName
            print classType
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_CREATE_CHARACTER)
            pkg.addString(charName)
            pkg.addInt32(classType)
            self.cWriter.send(pkg, self.connection)

            #self.log('Sent [' + str(Constants.RAND_STRING) + '] Int Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_CREATE_CHARACTER) + '] Request')
            print_exc()
