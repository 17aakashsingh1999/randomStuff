# this module provides a way to modify the way rooms are managed
# can be modified to support sql when multiple relay server are running

roomsDict={}

def get(roomName):
    return roomsDict[roomName]

def exists(roomName):
    if roomName in roomsDict.keys():
        return True
    return False

def add(roomName,ip):
    if exists(roomName):
        return False
    roomsDict[roomName]=ip
    return True

def remove(roomName,ip):
    if exists(roomName):
        if roomsDict[roomName]==ip:
            del roomsDict[roomName]

# this module is fully functional