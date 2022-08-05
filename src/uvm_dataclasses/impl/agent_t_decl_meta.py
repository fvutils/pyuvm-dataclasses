'''
Created on Jul 4, 2022

@author: mballance
'''
import types
from uvm_dataclasses.impl.agent_t import AgentT
from uvm_dataclasses.impl.agent_t_def_meta import AgentTDefMeta
from uvm_dataclasses.impl.params import Params


class AgentTDeclMeta(type):
    """Meta-class for the declaration of an agent_t class"""
    
    def __init__(self, name, bases, dct):
        print("AgentTDeclMeta: name=%s bases=%s dct=%s" % (
            str(name), str(bases), str(dct)))
        pass

    def __getitem__(self, *args, **kwargs):
        params = Params()
        def populate(cls):
            nonlocal params
            print("populate")
            cls["parameters"] = params
            pass
        print("__getitem__: %s %s" % (str(args), str(kwargs)))
        return types.new_class("agent_t", (AgentT,), 
            {"metaclass": AgentTDefMeta}, populate)
