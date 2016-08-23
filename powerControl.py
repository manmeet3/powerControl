#!"c:\Users\Manmeet Singh\AppData\Local\Programs\Python\Python35-32\python.exe"
import cgi
import os

form = cgi.FieldStorage()
action = form['action'].value
time = form['time'].value



print("Content-Type: text/html")
print("")
print(""" <TITLE> Windows Remote Shutdown Utility </TITLE>
		<H1> Welcome to Power Control</H1>
""")


if (action=="shutdown"):
  os.system("shutdown /t %s " % time)
  print (" Executing : "+action + " in " + time + " seconds.")
elif (action=="sleep"):
  os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
  print (" Executing : "+action + " in " + time + " seconds.")
elif (action=="hibernate"):
  os.system(r'%windir%\system32\rundll32.exepowrprof.dll,SetSuspendState Hibernate')
  print (" Executing : "+action + " in " + time + " seconds.")
  
else:
  print (""" Invalid command : """+action)

