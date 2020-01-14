#!/usr/bin/python

import signal

# signal handler
def ctrlc_handler(signum, frm) :

	print "haha! you cannot kill me!"

# when running the script, you would normally use the keystroke of ctrl +c to kill the process. This will not be possible now. 
print "installing signal handler ...."
signal.signal(signal.SIGINT, ctrlc_handler)

print "done!"

while True :
	pass
