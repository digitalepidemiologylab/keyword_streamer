#!/usr/bin/env python

import settings
import sys

from mkondo import shunter

if __name__ == '__main__':
	shunter.shunt(settings.DATA_DIRECTORY)
