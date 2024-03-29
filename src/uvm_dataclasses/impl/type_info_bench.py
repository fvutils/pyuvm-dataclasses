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

from .type_info_environment import TypeInfoEnvironment
from .type_info_object import TypeInfoObject
from .type_info_util import TypeInfoUtil, UtilKind

class TypeInfoBench(TypeInfoUtil):
    
    def __init__(self, info):
        super().__init__(info, UtilKind.Bench)
        self._top_env_ti : TypeInfoEnvironment = None
        self._top_env_name = None
        
    def init(self, obj, name, parent):
        print("TypeInfoBench.init configuration=%s" % str(obj.configuration))
        super().init(obj, name, parent)
        
    def build_phase(self, parent):
        print("TypeInfoBench.build_phase")
        print("top_env_ti=%s" % str(self._top_env_ti))
        print("top_env_ti._config_t=%s" % str(self._top_env_ti._config_t))
        self.pre_build_phase(parent)

        self.core_build_phase(parent)

        print("top_env_ti.config_t=%s" % str(self._top_env_ti._config_t))
        print("--> Create Configuration")
        setattr(parent, "configuration",
                self._top_env_ti._config_t())        
        print("<-- Create Configuration")
        root_comp = parent.get_child(self._top_env_name)
        root_comp.configuration = parent.configuration
        
        print("configuration: %s" % str(parent.configuration))
        
        super().post_build_phase(parent)
        
        # for agent in self._agents:
        #     print("TODO: initialize agent")
            
        # for subenv in self._subenvs:
        #     print("TODO: initialize sub-env")        
        
    @staticmethod
    def get(info):
        if not hasattr(info, TypeInfoObject.ATTR_NAME):
            print("TypeInfoBench.get()")
            setattr(info, TypeInfoObject.ATTR_NAME, TypeInfoBench(info))
        return getattr(info, TypeInfoObject.ATTR_NAME)
    