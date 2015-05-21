#!/usr/bin/python
import time

ISOTIMEFORMAT=’%Y-%m-%d %X’
print time.time()
print time.localtime()
print time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )


