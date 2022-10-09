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

import pyuvm
import typing
import typeworks

from typeworks.impl.typeinfo import TypeInfo
from uvm_dataclasses.impl.decorator_object_impl import DecoratorObjectImpl
from uvm_dataclasses.impl.method_impl_config import MethodImplConfig
from uvm_dataclasses.impl.method_impl_environment import MethodImplEnvironment

from uvm_dataclasses.impl.type_info_component import TypeInfoComponent
from uvm_dataclasses.impl.type_info_config import TypeInfoConfig
from uvm_dataclasses.impl.type_info_environment import TypeInfoEnvironment
from uvm_dataclasses.impl.type_info_object import TypeInfoObject
from uvm_dataclasses.impl.type_info_util import TypeInfoUtil, UtilKind
from ..type_kind import TypeKind

from .decorator_component_impl import DecoratorComponentImpl
from .decorator_config_impl import DecoratorConfigImpl


class DecoratorEnvironmentImpl(DecoratorComponentImpl):
    
    def get_type_category(self):
        return TypeKind.Environment
    
    def pre_decorate(self, T):
#        if not hasattr(T, "config_t"):
#            raise Exception("No 'config_t' class defined")
        TypeInfoEnvironment.get(self.get_typeinfo())
        return super().pre_decorate(T)
    
    def pre_init_annotated_fields(self):
        
        # Add a placeholder for the configuration
        self.add_field_decl("configuration", None, True, None)
        
        return super().pre_init_annotated_fields()

    def init_annotated_field(self, key, type, has_init, init):
        print("--> Environment.init_annotated_field")
        if not has_init:
            type_ti = TypeInfo.get(type, False)
            uc_kind = TypeInfoUtil.getUtilKind(type_ti)
            
            print("uc_kind: %s" % uc_kind)
            
            if uc_kind is not None:
                env_ti = TypeInfoUtil.get(self.get_typeinfo())
                type_uc_ti = TypeInfoUtil.get(type_ti)
                self.set_field_initial(key, None)
                if uc_kind == UtilKind.Env:
                    env_ti._subenvs.append((key, type_uc_ti))
                    env_ti._udc_component_fields.append((key, type_uc_ti))
                elif uc_kind == UtilKind.Agent:
                    env_ti._agents.append((key, type_uc_ti))
                    env_ti._udc_component_fields.append((key, type_uc_ti))
                pass
            else:
                print("<-- Environment.init_annotated_field")
                return super().init_annotated_field(key, type, has_init, init)
        else:
            print("<-- Environment.init_annotated_field")
            return super().init_annotated_field(key, type, has_init, init)
        print("<-- Environment.init_annotated_field")
            
    def post_init_annotated_fields(self):
        env_ti = TypeInfoEnvironment.get(self.get_typeinfo())
        print("Component: %d uvm_component fields" % len(env_ti._uvm_component_fields))
        print("Sub-Environments: %d" % len(env_ti._subenvs))
        
        config_t = typeworks.DeclRgy.pop_decl(DecoratorConfigImpl)
        
        if len(config_t) == 0:
            raise Exception("No @config class declared in environment %s" % self.T.__name__)
        elif len(config_t) > 1:
            raise Exception("Multiple @config classes declared in environment %s" % self.T.__name__)

        env_ti._config_t = config_t[0]
        print("Environment: %s ; config: %s" % (
            str(env_ti), str(env_ti._config_t)))

        # Add type hints for the config objects        
        for name,senv_ti in env_ti._subenvs:
            print("Name: %s ; Config: %s" % (name, str(senv_ti._config_t)))
            env_ti.decl_config_field("%s_config" % name, senv_ti._config_t)
        
        for name,agnt_ti in env_ti._agents:
            print("Name: %s ; Config: %s" % (name, str(agnt_ti.config_t)))
            
        # TODO: Retrieve the config class
        # TODO: Add entries for each sub-field
        # TODO: Run the object decorator on the field
        print("--> Decorate Config for %s" % str(env_ti.T))
        config_ti = TypeInfoConfig.get(TypeInfo.get(env_ti._config_t))
        print("config_ti=%s" % str(config_ti))
        config_tp = DecoratorObjectImpl([],{})(env_ti._config_t)
        setattr(config_tp, "_initialize", MethodImplConfig.initialize)
        print("<-- Decorate Config for %s" % str(env_ti.T))
        env_ti._config_t = config_tp
            
        return super().post_init_annotated_fields()
    
