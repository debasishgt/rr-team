# define Constants

class Constants:
    RAND_INT = 1
    RAND_STRING = 2
    RAND_SHORT = 3
    RAND_FLOAT = 4

    SERVER_IP = 'csproject.calstatela.edu'
    SERVER_PORT = 9252

    DEBUG = True
    MSG_NONE = 1000

    CMSG_AUTH = 101
    CMSG_DISCONNECT = 102
    CMSG_REGISTER = 103
    CMSG_FORGOT_PASSWORD = 104
    CMSG_CREATE_CHARACTER = 105
    CMSG_CHAT = 106
    CMSG_MOVE = 107
    CMSG_POWER_UP = 108
    CMSG_POWER_PICKUP = 109
    CMSG_HEALTH = 110

    CMSG_ENTER_LOBBY = 111
    CMSG_ENTER_GAME_LOBBY = 112
    CMSG_CREATE_LOBBY = 114

    CMSG_RESULTS = 122
    CMSG_RANKINGS = 123
    CMSG_PRIZES = 124
    CMSG_COLLISION = 125
    CMSG_DEAD = 126
    CMSG_READY = 127
    CMSG_SET_POSITION = 128
    CMSG_SET_RANK = 130
    CMSG_SERVER = 0

    SMSG_AUTH = 201
    SMSG_DISCONNECT = 202
    SMSG_REGISTER = 203
    SMSG_FORGOT_PASSWORD = 204
    SMSG_CREATE_CHARACTER = 205
    SMSG_CHAT = 206
    SMSG_MOVE = 207
    SMSG_POWER_UP = 208
    SMSG_POWER_PICKUP = 209
    SMSG_HEALTH = 210

    SMSG_ENTER_LOBBY = 211
    SMSG_ENTER_GAME_LOBBY = 212
    SMSG_CREATE_LOBBY = 214

    SMSG_RESULTS = 222
    SMSG_RANKINGS = 223
    SMSG_PRIZES = 224
    SMSG_COLLISION = 225
    SMSG_DEAD = 226
    SMSG_READY = 227
    SMSG_SET_POSITION = 228
    SMSG_TIME = 229
    SMSG_SET_RANK = 230
    SMSG_SET_READY = 231
    SMSG_RENDER_CHARACTER = 310
    SMSG_REMOVE_CHARACTER = 311

    SMSG_SERVER = 0

#    CMSG_AUTH                           = 101
#    CMSG_DISCONNECT                     = 102
#    CMSG_REGISTER                       = 103
#    CMSG_CREATE_CHARACTER               = 104
#    CMSG_CHAT                           = 105
#    CMSG_MOVE                           = 106
#    CMSG_ATTACK                         = 107
#    CMSG_HEALTH                         = 108
#    CMSG_CONTROL_POINT_STATE            = 111
#    CMSG_CONTROL_POINT_CAP              = 112
#    REQ_HEARTBEAT                       = 301
    
#    SMSG_AUTH                           = 201
#    SMSG_DISCONNECT                     = 202
#    SMSG_REGISTER                       = 203
#    SMSG_CREATE_CHARACTER               = 204
#    SMSG_CHAT                           = 205
#    SMSG_MOVE                           = 206
#    SMSG_ATTACK                         = 207
#    SMSG_HEALTH                         = 208
#    SMSG_RESOURCE                       = 209
#    SMSG_CONTROL_POINT_STATE            = 211
#    SMSG_CONTROL_POINT_CAP              = 212
#    SMSG_RENDER_CHARACTER               = 310
#    SMSG_REMOVE_CHARACTER               = 311
#    SMSG_SPAWN_GUARDS                   = 312
#    SMSG_DESTROY_NPC                    = 313
#    SMSG_SPAWN_GOLEMCP                  = 321
#    SMSG_DESTROY_GOLEMCP                = 322
#    SMSG_SPAWN_GOLEM_NPC                = 323
#    SMSG_GOLEM_PIECE                    = 324
