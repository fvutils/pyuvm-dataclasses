
from .analysis_port_t import AnalysisPortKind, AnalysisPortT

class AnalysisExportMetaT(type):
    
    def __init__(self, name, bases, dct):
        self.type_m = {}

    def __getitem__(self, item):
        if item in self.type_m.keys():
            return self.type_m[item]
        else:
            ret = AnalysisPortT()
            ret.T = item
            ret.Kind = AnalysisPortKind.Export
            self.type_m[item] = ret
            return ret