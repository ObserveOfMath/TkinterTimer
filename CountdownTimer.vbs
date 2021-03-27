Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c python C:\Users\User\Desktop\Projects\SideProjects\CountdownTimer.py"
rem strArgs = "cmd /c C:\Users\User\Desktop\Projects\SideProjects\CountdownTimer.bat"
oShell.Run strArgs, 0, false
