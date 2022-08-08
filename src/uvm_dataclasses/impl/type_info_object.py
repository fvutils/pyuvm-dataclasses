
from typeworks.impl.typeinfo import TypeInfo


class TypeInfoObject(object):
    
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
        
    @staticmethod
    def get(info):
        if not hasattr(info, "_udc_info"):
            setattr(info, "_udc_info", TypeInfoObject(info))
        return info._udc_info