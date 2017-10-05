#!/usr/bin/env python2.7
from bGeigie import *
import sys


#f="test.log"
f=sys.argv[1]


geigie=bGeigie(f)
geigie.gisData(sys.argv[2])
