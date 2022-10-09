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
import types

from .component_param_decl_t import ComponentParamDeclT


from .params import Params

class ComponentParamDeclMeta(type):
    
    def __init__(self, name, bases, dct):
        pass
    
    def __getitem__(self, *args, **kwargs):
        from .component_param_def_meta import ComponentParamDefMeta
        
        params = Params()
        def populate(cls):
            nonlocal params
            print("populate")
            cls["Parameters"] = params
        
        return types.new_class("uvm_component[%s]" % "tmp", (ComponentParamDeclT,),
                            {"metaclass": ComponentParamDefMeta}, populate)