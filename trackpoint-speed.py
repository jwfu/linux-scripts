#!/usr/bin/env python
#figures out which input device ID is the trackpoint, and makes the trackpoint faster

import os
import re
f = os.popen('xinput')
xinput = f.read()
idnumber=re.findall(r"TrackPoint                   	id=([0-9]*)", xinput)[0]
os.system('xinput --set-prop "' + idnumber +  '" "Device Accel Constant Deceleration" 0.2')
