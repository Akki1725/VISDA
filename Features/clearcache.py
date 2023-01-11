import os

path_init = ("e:")
path = ("cd E:\Docs\Projects\Projects\VISDA")
cmd = ('find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf')


def clear_cache():
        
    os.system(path_init)
    os.system(path)
    os.system(cmd)
