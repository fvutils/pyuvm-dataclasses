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
import vsc_dataclasses as vdc
from typing import List, Tuple
from typeworks.impl.typeinfo import TypeInfo


class TypeInfoObject(vdc.impl.TypeInfoRandClass):
    
    ATTR_NAME = vdc.impl.TypeInfoRandClass.ATTR_NAME
    
    def __init__(self, ti):
        super().__init__(ti)
        self._ti = ti
        self._uvm_object_fields : List[Tuple[str,type]] = []
        self._udc_object_fields : List[Tuple[str,TypeInfoObject]] = []
        
    def init(self, obj):
        super().init(obj, [], {})

        # Create UDC object fields
        for name,obj_ti in self._udc_object_fields:
            f = obj_ti.T()
            setattr(obj, name, f)
        
        # Create non-UDC object fields
        for name,type in self._uvm_object_fields:
            f = type()
            setattr(obj, name, f)

    @property
    def T(self):
        return self._ti.T

    @staticmethod
    def isUdcType(info):
        return info is not None and hasattr(info, TypeInfoObject.ATTR_NAME)
        
    @staticmethod
    def get(info, create=True):
        if not hasattr(info, TypeInfoObject.ATTR_NAME):
            if create:
                setattr(info, TypeInfoObject.ATTR_NAME, TypeInfoObject(info))
            else:
                return None
        return getattr(info, TypeInfoObject.ATTR_NAME)