from common.Constants import Constants

# from net.response.ResponseRandomInt import ResponseRandomInt
# from net.response.ResponseRandomString import ResponseRandomString
# from net.response.ResponseRandomShort import ResponseRandomShort
# from net.response.ResponseRandomFloat import ResponseRandomFloat
# from net.response.ResponseLogin import ResponseLogin
# from net.response.ResponseCreateCharacter import ResponseCreateCharacter
# from ResponseChatAll import ResponseChatAll
# from ResponseUsers import ResponseUsers
# from ResponseChatOne import ResponseChatOne

from net.response.ResponseMove import ResponseMove
from net.response.ResponsePowerUp import ResponsePowerUp
from net.response.ResponsePowerPickUp import ResponsePowerPickUp
from net.response.ResponseHealth import ResponseHealth
from net.response.ResponseResults import ResponseResults
from net.response.ResponseRankings import ResponseRankings
from net.response.ResponsePrizes import ResponsePrizes
from net.response.ResponseCollision import ResponseCollision
from net.response.ResponseDead import ResponseDead
from net.response.ResponseReady import ResponseReady
from net.response.ResponseSetPosition import ResponseSetPosition

class ServerResponseTable:
    """
    The ServerResponseTable contains a mapping of all responses for use
    with the networking component.
    """
    responseTable = {}

    def __init__(self):
        """Initialize the response table."""
        # self.add(Constants.RAND_INT, 'ResponseRandomInt')
        # self.add(Constants.RAND_STRING, 'ResponseRandomString')
        # self.add(Constants.RAND_SHORT, 'ResponseRandomShort')
        # self.add(Constants.RAND_FLOAT, 'ResponseRandomFloat')
        # self.add(Constants.CMSG_AUTH, 'ResponseLogin')
        # self.add(Constants.SMSG_CREATE_CHARACTER, 'ResponseCreateCharacter')
        # self.add(Constants.CMSG_CHAT_ALL, 'ResponseChatAll')
        # self.add(Constants.CMSG_USERS, 'ResponseUsers')
        # self.add(Constants.CMSG_CHAT_ONE, 'ResponseChatOne')

        self.add(Constants.SMSG_MOVE, 'ResponseMove')
        self.add(Constants.SMSG_POWER_UP, 'ResponsePowerUp')
        self.add(Constants.SMSG_POWER_UP_PICK_UP, 'ResponsePowerPickUp')
        self.add(Constants.SMSG_HEALTH, 'ResponseHealth')
        self.add(Constants.SMSG_RESULTS, 'ResponseResults')
        self.add(Constants.SMSG_RANKINGS, 'ResponseRankings')
        self.add(Constants.SMSG_PRIZES, 'ResponsePrizes')
        self.add(Constants.SMSG_COLLISION, 'ResponseCollision')
        self.add(Constants.SMSG_DEAD, 'ResponseDead')
        self.add(Constants.SMSG_READY, 'ResponseReady')
        self.add(Constants.SMSG_SET_POSITION, 'ResponseSetPosition')

    def add(self, constant, name):
        """Map a numeric response code with the name of an existing response module."""
        if name in globals():
            self.responseTable[constant] = name
        else:
            print 'Add Response Error: No module named ' + str(name)

    def get(self, responseCode):
        """Retrieve an instance of the corresponding response."""
        serverResponse = None

        if responseCode in self.responseTable:
            serverResponse = globals()[self.responseTable[responseCode]]()
        else:
            print 'Bad Response Code: ' + str(responseCode)

        return serverResponse
