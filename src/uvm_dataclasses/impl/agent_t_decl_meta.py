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
