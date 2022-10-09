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


from ..type_kind import TypeKind
from .decorator_component_impl import DecoratorComponentImpl


class DecoratorAgentImpl(DecoratorComponentImpl):
    
    def get_type_category(self):
        return TypeKind.Agent
    
    def pre_decorate(self, T):
        self._validate_ports(T)
        self._validate_transaction(T)
        self._validate_vlnv(T)
        
        super().pre_decorate(T)

    def _validate_ports(self, T):
        import uvm_dataclasses as udc
        if not hasattr(T, "ports"):
            raise Exception("Agent class %s doesn't define 'ports'" % T.__qualname__)
        ports = getattr(T, "ports")

        if isinstance(ports, udc.types.ports):
            pass
        elif isinstance(ports, tuple):
            # Convert to udc.ports
            setattr(T, "ports", udc.types.ports(*ports))
        else:
            raise Exception("Expect ports to be of type tuple or udc.ports")
        pass

    def _validate_transaction(self, T):
        if not hasattr(T, "transaction"):
            raise Exception("Agent class %s does not declare a 'transaction' class" % (
                T.__qualname__,))

    def _validate_vlnv(self, T):
        if not hasattr(T, "vlnv"):
            raise Exception("Agent class %s does not declare a 'vlnv' field" % (
                T.__qualname__,))
