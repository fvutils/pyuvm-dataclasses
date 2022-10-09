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
#****************************************************************************
from enum import Enum, auto
from uvm_dataclasses.impl.type_info_object import TypeInfoObject
from .type_info_component import TypeInfoComponent

class UtilKind(Enum):
    Agent = auto()
    Bench = auto()
    Config = auto()
    Env = auto()

class TypeInfoUtil(TypeInfoComponent):
    
    def __init__(self, info, kind):
        print("TypeInfoUtil()")
        super().__init__(info)
        self.kind = kind
        self._config_t = None
        
    def decl_config_field(self, key, type):
        if not hasattr(self._config_t, "__annotations__"):
            setattr(self._config_t, "__annotations__", dict())
        self._config_t.__annotations__[key] = type
    
    @staticmethod
    def getUtilKind(info):
        if info is None:
            return None

        udc_info = TypeInfoObject.get(info, False)
        if isinstance(udc_info, TypeInfoUtil):
            return udc_info.kind
        else:
            return None
    
            
