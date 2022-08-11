
import types

from uvm_dataclasses.impl.component_param_decl_t import ComponentParamDeclT


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