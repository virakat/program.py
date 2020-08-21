import pyttsx3
import os

pyttsx3.speak("Hello" "Welcome to my program")


while True:
	print("which program do you wanna run : "  , end='')
	p = input()

	if ("do not" in p) or ("dont" in p) :
		pass
	
	elif (("run" in p)  or ("execute" in p) or ("launch" in p)) and (("editor" in p) or ("notepad" in p)):
	  pyttsx3.speak("opening notepad")
	  os.system("notepad")

	elif (("run" in p)  or ("execute" in p) or ("launch" in p)) and (("chrome" in p) or ("browser" in p)):
	  pyttsx3.speak("opening chrome browser")
	  os.system("chrome https://www.youtube.com/watch?v=2PjfpSgtuE8 https://twitter.com/vimaldaga13")

	elif (("run" in p) or ("launch" in p) or ("execute" in p))  and (("player" in p) or ("media" in p) or ("music" in p)):
	  pyttsx3.speak("opening window media player")
	  os.system("wmplayer")
	
	elif (("run" in p) or ("launch" in p) or ("execute" in p))  and (("vmware" in p) or ("workstation" in p) or ("virtual machine" in p)):
	  pyttsx3.speak("opening virtual machine")
	  os.system("VBoxManage startvm Kali")

	elif (("run" in p) or ("launch" in p) or ("execute" in p))  and (("recovery" in p) or ("data recovery" in p)):
	  pyttsx3.speak("opening Data Recovery Software")
	  os.system("drw")  

	elif (("run" in p) or ("launch" in p) or ("execute" in p))  and (("3utools" in p) or ("itools" in p)):
	  pyttsx3.speak("opening 3 u tools")
	  os.system("3utools")    
	  
	elif  ("exit" in p)  or ("quit" in p):
	  pyttsx3.speak("good bye")
	  break

	else:
	  print("dont support" "try with something else")
