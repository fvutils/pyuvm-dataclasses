
from uvm_dataclasses.impl.agent_t_meta import AgentTMeta
from uvm_dataclasses.impl.analysis_export_meta_t import AnalysisExportMetaT
from uvm_dataclasses.impl.analysis_port_meta_t import AnalysisPortMetaT
from uvm_dataclasses.impl.analysis_port_t import AnalysisPortT
from uvm_dataclasses.impl.analysis_imp_meta_t import AnalysisImpMetaT


class analysis_port(metaclass=AnalysisPortMetaT):
    pass

class analysis_imp(metaclass=AnalysisImpMetaT):
    pass

class analysis_export(metaclass=AnalysisExportMetaT):
    pass

class param_base(metaclass=AgentTMeta):
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