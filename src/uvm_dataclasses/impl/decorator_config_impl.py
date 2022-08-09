'''
Created on Jul 4, 2022

@author: mballance
'''

import typeworks

class DecoratorConfigImpl(typeworks.RegistrationDecoratorBase):
    
    def __init__(self, args, kwargs):
        super().__init__(DecoratorConfigImpl, args, kwargs)
