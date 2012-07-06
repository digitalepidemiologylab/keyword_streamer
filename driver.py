#!/usr/bin/env python

''' Restart the keywords program if it is not running '''

import commands
import os
import settings

output = commands.getoutput('ps -ax')
if 'collector.py' not in output:
	exefile = settings.APP_DIRECTORY + 'collector.py'
	os.execl(exefile, 'collector.py')
