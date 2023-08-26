class FormatException(Exception):
    def __init__(self, msg):
        self.__msg = msg
        
    def __repr__(self):
        return self.__msg