
class AgentTDefMeta(type):

    def __init__(self, name, bases, dct):
        pass

    def __getitem__(self, *args, **kwargs):
        print("Type: %s" % str(type(self)))
        print("AgentTDefMeta: parameters=%s" % str(self.parameters))
        pass