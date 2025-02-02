import py_compile
py_compile.compile('app.py')
print("Compilation done. Created app.cpython-39.pyc file in __pychache__ folder")

#python compile.py

'''
using compile all module
Sometimes you may need to compile all the python script within a given directory. 
Then this method is good rather than compiling each file independently.
It will not compile if permission is not there

$ python -m compileall
'''