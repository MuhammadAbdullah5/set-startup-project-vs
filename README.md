# set-startup-project-vs
##### Overview

A python script to automate *'set as startup project'* option in *Visual Studio IDE* before building the project.

##### Description :

This code piece is for all those developers who are tired of first build failed problem in Visual studio. Particularly, if visual studio project files are built using **cmake**, it automatically sets the *ALL BUILD* project as start up project and subsequently first build fails. This is undesirable since it would force developers to open the IDE and manually set startup project. So, this python script may come handy on such ocassions. Also, this script can be used in conjunction with windows build utilitied like msbuild or devenv to check build success or failure without having to manually update the start up project option in IDE.

##### Usage : 

Install python on your Windows machine. Open command prompt in directory where this script is placed. Issue the following command in given format

_*<python directory>\python.exe startupProjectPatch.py <disk location>\<solution file name>.sln*_

for example, I have sim.sln file for the project sim which I would like to be set as start up project and it's located in C:\users\anonymous\desktop\sim.sln and python installation directory is C:\python27 then I would issue following command from command prompt

_*C:\python27\python.exe .\startupProjectPatch.py C:\users\anonymous\desktop\sim.sln*_
