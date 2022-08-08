'''
Created on Jul 4, 2022

@author: mballance
'''

import pyuvm
import typing

from typeworks.cls_decorator_base import ClsDecoratorBase


class DecoratorEnvironmentImpl(ClsDecoratorBase):
    
    IS_SUBCLASS_TYPES = ClsDecoratorBase.IS_SUBCLASS_TYPES + \
        [(pyuvm.uvm_component, "abc") ]
    
    TYPE_PROCESSING_HOOKS = \
        ClsDecoratorBase.TYPE_PROCESSING_HOOKS + \
            [lambda self, T : DecoratorEnvironmentImpl.process(self, T)]
    
    def __init__(self, kwargs):
        pass
    
    def process(self, T):
        print("process")
        pass
    
    def __call__(self, T):
        if hasattr(T, "__init__"):
            print("Has __init__ with %d parameters" % getattr(T, "__init__").__code__.co_argcount)
        Tp = super().__call__(T)
        print("decorator: %s" % str(getattr(T, "__annotations__", {})))
        for key,value in getattr(T, "__annotations__", {}).items():
#        for key,value in typing.get_type_hints(T).items():
            print("key=%s value=%s" % (str(key), str(value)))
            if not hasattr(T, key):
                print("  No initial value for %s" % str(key))

        return Tp