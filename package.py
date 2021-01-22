# -*- coding: utf-8 -*-

name = "shotgun_python_api"

version = "3.2.6-ta.0.1.0"

authors = [
    "Shotgun"
]

description = \
    """
    Shotgun python api.
    """
    
# Release this as an internal package
with scope("config") as c:
    import sys
    if "win" in str(sys.platform):
        c.release_packages_path = "R:/ext"
    else:
        c.release_packages_path = "/r/ext"
        

requires = [
    "python",
]

variants = [
]

build_command = "python {root}/rez_build.py"

def commands():
    env.SHOTGUN_PYTHON_API_ROOT.set("{root}")
    env.PYTHONPATH.append("{0}".format(env.SHOTGUN_PYTHON_API_ROOT)
