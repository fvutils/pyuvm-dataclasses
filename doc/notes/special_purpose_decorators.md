
Top-level methodology elements require a decorator in order to be discovered.
Examples include environment, bench, agent. In addition to attribute creation,
these elements require special handling.

Top-level 

- Only intervene with special-type fields
- Leave '__init__' as-is
- Override '__postinit__' to create special-purpose fields, etc (?)
  - Does this mess with inheritance?