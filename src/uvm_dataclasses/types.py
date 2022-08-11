
from pyuvm import uvm_component
from uvm_dataclasses.impl.agent_t_decl_meta import AgentTDeclMeta
from uvm_dataclasses.impl.analysis_export_meta_t import AnalysisExportMetaT
from uvm_dataclasses.impl.analysis_port_meta_t import AnalysisPortMetaT
from uvm_dataclasses.impl.analysis_port_t import AnalysisPortT
from uvm_dataclasses.impl.analysis_imp_meta_t import AnalysisImpMetaT
from uvm_dataclasses.impl.component_param_decl_meta import ComponentParamDeclMeta


class analysis_port(metaclass=AnalysisPortMetaT):
    pass

class analysis_imp(metaclass=AnalysisImpMetaT):
    pass

class analysis_export(metaclass=AnalysisExportMetaT):
    pass

class component_param(metaclass=ComponentParamDeclMeta):
    pass

class param_base(metaclass=AgentTDeclMeta):
    pass

class agent_t(metaclass=AgentTDeclMeta):
    pass

class ports(object):

    def __init__(self, *args, **kwargs):
        self.ports = []
        
        for p in args:
            if not isinstance(p, (input,output)):
                raise Exception("Port %s is of type %s, not of input or output type" % (
                    str(p), type(p).__qualname__))
            self.ports.append(p)

    pass

class output(object):
    def __init__(self, name, width="1", **kwargs):
        pass
    pass

class input(object):
    def __init__(self, name, width="1", **kwargs):
        pass
    pass