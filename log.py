# coding: utf-8
# Here your code !

from info import Info

def id_generator(start):
    i = start
    while True:
        yield i
        i += 1

class LogInfo(Info):
    def __init__(self, event_id, log_level, when, who, do_what, what, how_much, with_whom):
        Info.__init__(self, event_id, self.__class__.__name__)
        self.log_level = log_level
        self.when = when
        self.who = who
        self.do_what = do_what
        self.what = what
        self.how_much = how_much
        self.with_whom = with_whom
    def message(self):
        ret = "%s [%s] %s: In %s, %s %s %s" % (self.get_name(), self.get_log_level(), self.get_id(),self.get_when(), self.get_who(), self.get_do_what(), self.get_what())
        if self.get_how_much():
            ret += " by %s" % self.get_how_much()
        if self.get_with_whom():
            ret+ "with %s" % self.get_with_whom()
        return ret
    def get_log_level(self):
        return self.log_level
    def get_when(self):
        return self.when
    def get_who(self):
        return self.who
    def get_do_what(self):
        return self.do_what
    def get_what(self):
        return self.what
    def get_how_much(self):
        return self.how_much
    def get_with_whom(self):
        return self.with_whom

class BuyLog(LogInfo):
    def __init__(self, event_id, when, who, what, how_much):
        LogInfo.__init__(self, event_id, 'INFO', when, who, 'bought', what, how_much, '')

class MessageLog(LogInfo):
    def __init__(self, event_id, when, who, what):    
        LogInfo.__init__(self, event_id, 'INFO', when, who, 'sent message', '"%s"' % what, '', '')

class OfferLog(LogInfo):
    def __init__(self, event_id, when, who, what, how_much, with_whom):    
        LogInfo.__init__(self, event_id, 'DEBUG', when, who, 'offered',  what, how_much, with_whom)
   


class LogManager:
    def __init__(self,start):
        self.event_id_generator = id_generator(start)
        self.logs = []
    def add_buylog(self, when, who, what, how_much):
        self.logs.append(BuyLog(next(self.event_id_generator), when, who, what, how_much))
    def add_messagelog(self, when, who, what): 
        self.logs.append(MessageLog(next(self.event_id_generator), when, who, what))
    def latest_log(self):
        return self.logs[-1].message()
    def all_log(self):
        for loginfo in self.logs:
            yield loginfo.message()

lm = LogManager(1000)
for i in range(10):
    lm.add_buylog( i, "player-%s" % i , 2*i, 200*i)
    lm.add_messagelog( i, "player-%s" % i, "HAHAHA, I've already won") 
for loginfo in lm.all_log():
    print loginfo
