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

from uvm_dataclasses.impl.method_impl_component import MethodImplComponent
from uvm_dataclasses.impl.type_info_environment import TypeInfoEnvironment


class MethodImplEnvironment(object):
    pass
    
    # @staticmethod
    # def init(self, name, parent):
    #     env_ti = TypeInfoEnvironment.get(type(self)._typeinfo)
    #     MethodImplComponent.init(self, name, parent)
        
    #     print("TODO: create config %s" % str(env_ti.config_t))
    #     setattr(self, "configuration", env_ti.config_t())
        
    # @staticmethod
    # def build_phase(self):
    #     print("MethodImplEnvironment.build_phase")
    #     MethodImplComponent.build_phase(self)
    #     pass
        
        