from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestChangeHealth(ServerRequest):


    def send(self, data = None):

        try:
            #user_data = data.split()
            #username = user_data[0]
            #healthchange = int(user_data[1])
            #print username
            print data
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_HEALTH)
            #pkg.addString(username)
            #pkg.addInt32(healthchange)
            pkg.addInt32(data)
            self.cWriter.send(pkg, self.connection)
        except:
            self.log('Bad [' + str(Constants.CMSG_HEALTH) + '] Request')
            print_exc()
