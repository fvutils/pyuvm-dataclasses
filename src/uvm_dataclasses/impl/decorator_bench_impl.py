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
#
# Created on Jul 4, 2022
#
# @author: mballance
#****************************************************************************


import typeworks
from uvm_dataclasses.impl.type_info_bench import TypeInfoBench
from uvm_dataclasses.impl.type_info_environment import TypeInfoEnvironment
from uvm_dataclasses.impl.type_info_util import TypeInfoUtil, UtilKind
from ..type_kind import TypeKind
from .decorator_component_impl import DecoratorComponentImpl

class DecoratorBenchImpl(DecoratorComponentImpl):
    
    def get_type_category(self):
        return TypeKind.Bench
    
    def pre_decorate(self, T):
        TypeInfoBench.get(self.get_typeinfo())
        super().pre_decorate(T)
    
    def post_init_annotated_fields(self):
        bench_ti = TypeInfoBench.get(self.get_typeinfo())
        
        # Add a placeholder for the configuration
        self.add_field_decl("configuration", None, True, None)
        
        if len(bench_ti._udc_component_fields) == 0:
            raise Exception("No environment class specified")
        elif len(bench_ti._udc_component_fields) > 1:
            raise Exception("Expect a single environment class ; %d specified" % (
                len(bench_ti._udc_component_fields),))

        top_env_ti = bench_ti._udc_component_fields[0][1]
        
        if not isinstance(top_env_ti, TypeInfoUtil):
            raise Exception("Top component %s is not a UVM Dataclasses Environment" % (
                str(bench_ti._udc_component_fields[0][0]),))
        elif top_env_ti.kind != UtilKind.Env:
            raise Exception("Top component %s is a %s, not a UVM Dataclasses Environment" % (
                str(bench_ti._udc_component_fields[0][0]),
                top_env_ti.kind))
        
        bench_ti._top_env_ti = top_env_ti
        bench_ti._top_env_name = bench_ti._udc_component_fields[0][0]
        print("Bench top_env_ti: %s ; config_t: %s" % (
            str(bench_ti._top_env_ti), str(bench_ti._top_env_ti._config_t)))
        
        super().post_init_annotated_fields()
    
    pass

    # def post_decorate(self, T, Tp):
    #     bench_ti = TypeInfoBench.get(self.get_typeinfo())
        
    #     super().post_decorate(T, Tp)
        
    #     Tp.__init__ = MethodImplBench.init
    #     Tp.build_phase = MethodImplBench.build_phase
        
