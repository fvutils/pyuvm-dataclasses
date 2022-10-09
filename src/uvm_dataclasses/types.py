#****************************************************************************
# Copyright 2022 Matthew Ballance and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#****************************************************************************

from pyuvm import uvm_component
from .impl.agent_t_decl_meta import AgentTDeclMeta
from .impl.analysis_export_meta_t import AnalysisExportMetaT
from .impl.analysis_port_meta_t import AnalysisPortMetaT
from .impl.analysis_port_t import AnalysisPortT
from .impl.analysis_imp_meta_t import AnalysisImpMetaT
from .impl.component_param_decl_meta import ComponentParamDeclMeta


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