'''
Created on Jul 4, 2022

@author: mballance
'''
from uvm_dataclasses.impl.decorator_agent_impl import DecoratorAgentImpl
from uvm_dataclasses.impl.decorator_bench_impl import DecoratorBenchImpl
from uvm_dataclasses.impl.decorator_config_impl import DecoratorConfigImpl
from uvm_dataclasses.impl.decorator_knobs_impl import DecoratorKnobsImpl
from uvm_dataclasses.impl.decorator_environment_impl import DecoratorEnvironmentImpl
from uvm_dataclasses.impl.decorator_transaction_impl import DecoratorTransactionImpl

def component(*args, **kwargs):
    pass


def agent(*args, **kwargs):
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        return DecoratorAgentImpl({})(args[0])
    else:
        return DecoratorAgentImpl(kwargs)
    
def bench(*args, **kwargs):
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        return DecoratorBenchImpl({})(args[0])
    else:
        return DecoratorBenchImpl(kwargs)

#def config(*args, **kwargs):
#    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
#        return DecoratorConfigImpl({})(args[0])
#    else:
#        return DecoratorConfigImpl(kwargs)

#def knobs(*args, **kwargs):
#    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
#        return DecoratorKnobsImpl({})(args[0])
#    else:
#        return DecoratorKnobsImpl(kwargs)

def environment(*args, **kwargs):
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        return DecoratorEnvironmentImpl({})(args[0])
    else:
        return DecoratorEnvironmentImpl(kwargs)
    
#def transaction(*args, **kwargs):
#    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
#        return DecoratorTransactionImpl({})(args[0])
#    else:
#        return DecoratorTransactionImpl(kwargs)

# Marker type 
class create(object):
    pass
