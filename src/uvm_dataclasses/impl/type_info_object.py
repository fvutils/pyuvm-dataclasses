
import vsc
from typing import List, Tuple
from typeworks.impl.typeinfo import TypeInfo


class TypeInfoObject(vsc.impl.typeinfo_randclass.TypeInfoRandClass):
    
    ATTR_NAME = vsc.impl.typeinfo_randclass.TypeInfoRandClass.ATTR_NAME
    
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