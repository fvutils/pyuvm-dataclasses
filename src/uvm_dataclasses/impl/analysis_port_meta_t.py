
from .analysis_port_t import AnalysisPortKind, AnalysisPortT

class AnalysisPortMetaT(type):

    def __init__(self, name, bases, dct):
        self.type_m = {}
        pass

    def __getitem__(self, item):
        if item in self.type_m.keys():
            return self.type_m[item]
        else:
            ret = type("analysis_port[%s]" % str(item), (AnalysisPortT,), {})
            ret.T = item
            ret.Kind = AnalysisPortKind.Port
            self.type_m[item] = ret
            return ret

