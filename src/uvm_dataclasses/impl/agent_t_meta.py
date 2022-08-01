'''
Created on Jul 4, 2022

@author: mballance
'''

from uvm_dataclasses.impl.agent_t import AgentT


class AgentTMeta(type):
    
    def __init__(self, name, bases, dct):
        pass

    def __getitem__(self, *args, **kwargs):
        print("__getitem__: %s %s" % (str(args), str(kwargs)))
        return AgentT