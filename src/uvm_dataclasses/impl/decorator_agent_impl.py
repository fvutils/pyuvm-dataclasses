'''
Created on Jul 4, 2022

@author: mballance
'''


class DecoratorAgentImpl(object):
    
    def __init__(self, kwargs):
        pass
    
    def __call__(self, T):

        self._validate_ports(T)
        self._validate_transaction(T)
        self._validate_vlnv(T)
        pass

    def _validate_ports(self, T):
        import uvm_dataclasses as udc
        if not hasattr(T, "ports"):
            raise Exception("Agent class %s doesn't define 'ports'" % (
                type(T).__qualname__,))
        ports = getattr(T, "ports")

        if isinstance(ports, udc.types.ports):
            pass
        elif isinstance(ports, tuple):
            # Convert to udc.ports
            setattr(T, "ports", udc.types.ports(*ports))
        else:
            raise Exception("Expect ports to be of type tuple or udc.ports")
        pass

    def _validate_transaction(self, T):
        if not hasattr(T, "transaction_t"):
            raise Exception("Agent class %s does not declare a 'transaction' class" % (
                type(T).__qualname__,))

    def _validate_vlnv(self, T):
        if not hasattr(T, "vlnv"):
            raise Exception("Agent class %s does not declare a 'vlnv' field" % (
                type(T).__qualname__,))
