

class DecoratorKnobsImpl(object):

    def __init__(self, kwargs):
        if "prefix" in kwargs.keys():
            if kwargs["prefix"] == "":
                self.prefix = None
            else:
                self.prefix = kwargs["prefix"]
        else:
            self.prefix = "knob"

        self.kwargs = kwargs

    def __call__(self, T):
        return T
