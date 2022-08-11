

from uvm_dataclasses.impl.component_param_t import ComponentParamT


class ComponentParamDefMeta(type):
    
    def __init__(self, name, bases, dct):
        pass
    
    def __getitem__(self, *args, **kwargs):
        print("ComponentParamDefMeta: %s %s" % (str(args), str(kwargs)))
        
        return type("component_t", (ComponentParamT,), {})
    
        
        