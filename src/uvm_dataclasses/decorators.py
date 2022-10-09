#****************************************************************************
# Copyright 2022 Matthew Ballance and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Created on Jul 4, 2022
#
# @author: mballance
#****************************************************************************
from uvm_dataclasses.impl.decorator_agent_impl import DecoratorAgentImpl
from uvm_dataclasses.impl.decorator_component_impl import DecoratorComponentImpl
from uvm_dataclasses.impl.decorator_config_impl import DecoratorConfigImpl
from uvm_dataclasses.impl.decorator_knobs_impl import DecoratorKnobsImpl
from uvm_dataclasses.impl.decorator_environment_impl import DecoratorEnvironmentImpl
from uvm_dataclasses.impl.decorator_object_impl import DecoratorObjectImpl
from uvm_dataclasses.impl.decorator_transaction_impl import DecoratorTransactionImpl

pyobject = object

def component(*args, **kwargs):
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        return DecoratorComponentImpl([], {})(args[0])
    else:
        return DecoratorComponentImpl(args, kwargs)

def object(*args, **kwargs):
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        return DecoratorObjectImpl([], {})(args[0])
    else:
        return DecoratorObjectImpl(args, kwargs)
    
def sequence_item(*args, **kwargs):
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        return DecoratorObjectImpl([], {})(args[0])
    else:
        return DecoratorObjectImpl(args, kwargs)
    
def transaction(*args, **kwargs):
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        return DecoratorObjectImpl([], {})(args[0])
    else:
        return DecoratorObjectImpl(args, kwargs)

def agent(*args, **kwargs):
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        return DecoratorAgentImpl([], {})(args[0])
    else:
        return DecoratorAgentImpl(args, kwargs)
    
def bench(*args, **kwargs):
    from uvm_dataclasses.impl.decorator_bench_impl import DecoratorBenchImpl
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        return DecoratorBenchImpl([], {})(args[0])
    else:
        return DecoratorBenchImpl(args, kwargs)

def config(*args, **kwargs):
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        return DecoratorConfigImpl([], {})(args[0])
    else:
        return DecoratorConfigImpl(args, kwargs)

#def knobs(*args, **kwargs):
#    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
#        return DecoratorKnobsImpl({})(args[0])
#    else:
#        return DecoratorKnobsImpl(kwargs)

def environment(*args, **kwargs):
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        return DecoratorEnvironmentImpl([], {})(args[0])
    else:
        return DecoratorEnvironmentImpl(args, kwargs)
    
#def transaction(*args, **kwargs):
#    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
#        return DecoratorTransactionImpl({})(args[0])
#    else:
#        return DecoratorTransactionImpl(kwargs)

# Marker type 
class create(pyobject):
    pass
