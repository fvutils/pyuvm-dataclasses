'''
Created on Jul 4, 2022

@author: mballance
'''

import typing


class DecoratorEnvironmentImpl(object):
    
    def __init__(self, kwargs):
        pass
    
    def __call__(self, T):
        print("decorator: %s" % str(getattr(T, "__annotations__", {})))
        for key,value in getattr(T, "__annotations__", {}).items():
#        for key,value in typing.get_type_hints(T).items():
            print("key=%s value=%s" % (str(key), str(value)))
            if not hasattr(T, key):
                print("  No initial value for %s" % str(key))
        return T