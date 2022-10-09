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
from .type_info_object import TypeInfoObject
from .type_info_util import TypeInfoUtil, UtilKind

class TypeInfoConfig(TypeInfoObject):
    
    def __init__(self, info):
        super().__init__(info)
        
    def init(self, obj):
        print("TypeInfoConfig.init")
        super().init(obj)
        
        if hasattr(obj, "configure"):
            obj.configure()
            
    def initialize(self, obj):
        if hasattr(obj, "initialize"):
            obj.initialize()
            
        for name,ti in self._udc_object_fields:
            field = getattr(obj, name)
            if hasattr(field, "_initialize"):
                field._initialize()
        pass
        
    @staticmethod
    def get(info):
        if not hasattr(info, TypeInfoObject.ATTR_NAME):
            setattr(info, TypeInfoObject.ATTR_NAME, TypeInfoConfig(info))
        return getattr(info, TypeInfoObject.ATTR_NAME)
