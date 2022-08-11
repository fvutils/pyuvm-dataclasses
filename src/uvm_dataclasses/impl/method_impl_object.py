
from uvm_dataclasses.impl.type_info_object import TypeInfoObject


class MethodImplObject(object):
    
    @staticmethod
    def init(self):
        obj_ti = TypeInfoObject.get(type(self)._typeinfo)
        print("MethodImplObject.init: obj_ti=%s" % str(obj_ti))
        obj_ti.init(self)
        