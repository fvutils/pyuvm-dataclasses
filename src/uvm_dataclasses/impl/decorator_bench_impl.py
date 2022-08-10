'''
Created on Jul 4, 2022

@author: mballance
'''

import typeworks
from uvm_dataclasses.impl.type_info_bench import TypeInfoBench
from uvm_dataclasses.impl.type_info_environment import TypeInfoEnvironment
from uvm_dataclasses.impl.type_info_util import TypeInfoUtil, UtilKind
from .decorator_component_impl import DecoratorComponentImpl

class DecoratorBenchImpl(DecoratorComponentImpl):
    
    def pre_decorate(self, T):
        TypeInfoBench.get(self.get_typeinfo())
        super().pre_decorate(T)
    
    def post_init_annotated_fields(self):
        bench_ti = TypeInfoBench.get(self.get_typeinfo())
        
        # Add a placeholder for the configuration
        self.add_field_decl("configuration", None, True, None)
        
        if len(bench_ti._uvm_component_fields) == 0:
            raise Exception("No environment class specified")
        elif len(bench_ti._uvm_component_fields) > 1:
            raise Exception("Expect a single environment class ; %d specified" % (
                len(bench_ti._uvm_component_fields),))

        top_env_ti = typeworks.TypeInfo.get(bench_ti._uvm_component_fields[0][1])
        uc_type = TypeInfoUtil.getUtilKind(top_env_ti)
        
        if uc_type is None:
            raise Exception("Top component %s is not a UVM Dataclasses Environment" % (
                str(bench_ti._uvm_component_fields[0][0]),))
        elif uc_type != UtilKind.Env:
            raise Exception("Top component %s is a %s, not a UVM Dataclasses Environment" % (
                str(bench_ti._uvm_component_fields[0][0]),
                uc_type))
        
        bench_ti._top_env_ti = TypeInfoEnvironment.get(top_env_ti)
        
        print("uc_type=%s" % uc_type)
        super().post_init_annotated_fields()
    
    pass

    # def post_decorate(self, T, Tp):
    #     bench_ti = TypeInfoBench.get(self.get_typeinfo())
        
    #     super().post_decorate(T, Tp)
        
    #     Tp.__init__ = MethodImplBench.init
    #     Tp.build_phase = MethodImplBench.build_phase
        
