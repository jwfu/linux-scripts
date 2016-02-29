#!/usr/bin/env python

import os
import re
f = os.popen('xinput')
xinput = f.read()
regex = re.compile('TrackPoint                   	id=([0-9]*)')
idnumber=regex.findall(xinput)
os.system('xinput --set-prop "%s" "Device Accel Constant Deceleration" 0.2' % int(idnumber[0]))