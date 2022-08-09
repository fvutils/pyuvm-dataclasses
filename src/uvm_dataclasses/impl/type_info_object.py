
from typeworks.impl.typeinfo import TypeInfo


class TypeInfoObject(object):
    
    ATTR_NAME = "_udc_info"
    
    def __init__(self, ti):
        self._ti = ti
        self._uvm_object_fields = []
        
    def init(self, obj):
        self._ti.init(obj, [], {})
        print("TypeInfoObject.init")
        for name,type in self._uvm_object_fields:
            print("  Create field %s" % name)
            f = type(name)
            print("    f=%s obj=%s" % (str(f), str(obj)))
            setattr(obj, name, f)
            print("    f=%s obj=%s" % (str(f), str(obj)))

    @property
    def T(self):
        return self._ti.T
        
            
    @staticmethod
    def isUdcType(info):
        return info is not None and hasattr(info, TypeInfoObject.ATTR_NAME)
        
    @staticmethod
    def get(info, create=True):
        if not hasattr(info, "_udc_info"):
            if create:
                setattr(info, "_udc_info", TypeInfoObject(info))
            else:
                return None
        return info._udc_info