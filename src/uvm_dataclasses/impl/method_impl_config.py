
import typeworks
from .type_info_config import TypeInfoConfig

class MethodImplConfig(object):
    
    @staticmethod
    def initialize(self):
        config_ti = TypeInfoConfig.get(typeworks.TypeInfo.get(type(self)))
        config_ti.initialize(self)
        