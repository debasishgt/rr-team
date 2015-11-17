from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestMove(ServerRequest):


    def send(self, username = None):

        try:
            user_data = username.split()
            x = float(user_data[0])
            y = float(user_data[1])
            z = float(user_data[2])
            h = float(user_data[3])
            keys = str(user_data[4])
            print x
            print y
            print z
            print h
            print keys
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_MOVE)
            pkg.addFloat32(x)
            pkg.addFloat32(y)
            pkg.addFloat32(z)
            pkg.addFloat32(h)
            pkg.addString(keys)
            self.cWriter.send(pkg, self.connection)
        except:
            self.log('Bad [' + str(Constants.CMSG_MOVE) + '] Request')
            print_exc()
