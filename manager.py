# coding: utf-8
# Here your code 

def id_generator(start):
    i = start
    while True:
        yield i
        i += 1

class Manager:
    def __init__(self,start):
        self.id_generator = id_generator(start)
        self.items = {}
    def add_item(self, cls, *args):
        item_id = next(id_generator)
        self.items[item_id] = cls(item_id,*args)
        return item_id
    def get_item(self, item_id):
        return self.items[item_id]

class ActionManager(Manager):
    ID_START = 1000
    def __init__(self):
        ActionManager.__init__(self,self.ID_START)
        self.latest_action_id = -1
        self.latest_buy_id = -1
        self.latest_message_id = -1
    def add_buy(self, when, who, what, how_much):
        self.latest_action_id = self.add_item(Buy, when, who, what, how_much, self.latest_buy_id)
        self.latest_buy_id = self.latest_action_id
    def add_message(self, when, who, what): 
        self.latest_action_id = self.add_item(Message, when, who, what, self.latest_message_id)
        self.latest_message_id = self.latest_action_id
    def latest_action(self):
        return self.get_item(latest_action_id)
    def all_action(self, action_id):
        while action_id != -1 :
            action = self.get_item(action_id)
            yield action
            action_id = action.get_previous_action_id()
print "test"
