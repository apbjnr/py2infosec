#!/usr/bin/python

#from modules import Scientific
#ins = Scientific(5,6)

import modules


## call function call quickadd from the module file
print 'Quick Add a+b: %d' %modules.quickAdd(10,20)

ins = modules.Scientific(5,6)

print '%d'%ins.power()
