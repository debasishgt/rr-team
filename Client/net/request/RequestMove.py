from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestMove(ServerRequest):

  #args stores the x y z h and keys components of the moving
    def send(self, args = []):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_MOVE)
            pkg.addFloat32(args[0])
            pkg.addFloat32(args[1])
            pkg.addFloat32(args[2])
            pkg.addFloat32(args[3])
            pkg.addString(args[4])

            self.cWriter.send(pkg, self.connection)

        except:
            self.log('Bad [' + str(Constants.CMSG_MOVE) + '] Move Request')
