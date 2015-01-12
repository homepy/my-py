'''
1,usercustomize: *.py in usersitepackages will affect every invocation of Python, 
unless it is started with the -s option to disable the automatic import.
2,sitecustomize: works in the same way, 
but is typically created by an administrator of the computer in the global site-packages directory, 
and is imported before usercustomize.

'''
import site
print('site.getusersitepackages() == ', site.getusersitepackages())
print('site.getsitepackages() == ', site.getsitepackages())
