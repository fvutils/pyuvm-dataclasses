
from uvm_dataclasses.impl.type_info_object import TypeInfoObject
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
