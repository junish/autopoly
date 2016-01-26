# coding: utf-8
# Here your code !

from info import Info

def event_id(start):
    i = start
    while True:
        yield i
        i += 1

class LogInfo(Info):
    def __init__(self, event_id, name, message):
        Info.__init__(self, event_id, name)
        self.message = message

class LogManager:
    def __init__(self,start):
        self.event_id = event_id
        self.logs = []
    def write(self,name,message):
        self.logs.append(LogInfo(next(self.event_id),name,message))
