###########################
##  _ANchangeeDirName.py
##
##  2019.10.28
###########################

import sys
import os
dir_lst = sys.argv[1:] # the first argument is the script itself
for d in dir_lst:
	if os.path.isdir(d):
		file_lst =  os.listdir(d)


	else :
		print (p+"is not directory")


[lindex [split [lindex [split [knob [topnode].file] /] end] .] 0]

nuke.toNode()['antialiasing']
[value [value Dot_checkQTinput.input].file]

nuke.toNode('Write_DPX_Template2')['file'].getValue()