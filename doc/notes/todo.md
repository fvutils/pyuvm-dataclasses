
- Add sequencer/virtual sequencer to agent/env
  - Add sequencer handle to the config
  - Support referncing elements of interest from the sequencer
    - driver : uvm_driver = udc.ref("abc.def.ghi")
- Add sequence support
  - For now, can rely on generic udc.sequence that knows how 
    to obtain config from sequencer

- Register model
  - Annotations

@udc.reg
class my_reg(uvm_reg):
  field (non-volatile)
  volatile[]
  f1 : udc.field = udc.field[3,10]("rw", is_volatile=True, reset=True)
