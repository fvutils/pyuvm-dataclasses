
from uvm_dataclasses.impl.analysis_port_t import AnalysisPortKind, AnalysisPortT


class AnalysisImpMetaT(type):

    def __init__(self, name, bases, dct):
        self.type_m = {}

    def __getitem__(self, item):
        if item in self.type_m.keys():
            return self.type_m[item]
        else:
            ret = type("analysis_imp[%s]" % str(item), (AnalysisPortT,), {})
            ret.T = item
            ret.Kind = AnalysisPortKind.Impl
            self.type_m[item] = ret
            return ret