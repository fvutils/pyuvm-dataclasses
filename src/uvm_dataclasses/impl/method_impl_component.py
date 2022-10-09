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
from .type_info_component import TypeInfoComponent


class MethodImplComponent(object):

    @staticmethod    
    def init(self, name=None, parent=None):
        """Implements dataclass initialization for uvm_component

        Args:
            name (_type_): _description_
            parent (_type_): _description_
        """
        print("--> uvm_comp_init %s \"%s\"" % (name, str(parent)))
        comp_ti = TypeInfoComponent.get(type(self)._typeinfo)
        print("--> comp_ti.init", flush=True)
        comp_ti.init(self, name, parent)
        print("<-- comp_ti.init", flush=True)
        print("<-- uvm_comp_init")
        
    @staticmethod
    def build_phase(self):
        """
        Implements uvm_component build_phase for dataclasses
        """
        comp_ti : TypeInfoComponent = TypeInfoComponent.get(type(self)._typeinfo)
        comp_ti.build_phase(self)


