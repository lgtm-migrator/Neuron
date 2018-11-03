"""
-----------------------------------------------------
Copyright © Arthur Guiot 2018. All rights reserved
-----------------------------------------------------

tools/subprocess_checker.py checks if a subprocess
command is available and if it's safe to spawn it.

"""

import os
import platform
import subprocess

def command(name):
	cmd = "where" if platform.system() == "Windows" else "which"
	exist = False
	try:
	    subprocess.call([cmd, your_executable_to_check_here])
		exist = True
	except:
	    exist = False
	return exist
