import os
import shutil
from subprocess import Popen, PIPE
# When we move to a proper rez build, this file will be deprecated

if __name__ == "__main__":

    print("=== Build Package ===")
    src = os.environ["REZ_BUILD_SOURCE_PATH"]
    dst = os.environ["REZ_BUILD_INSTALL_PATH"]
    excludes = [".git", ".gitattributes", ".gitignore", "rez_build.py", "_rez_build", "package.py"]
    ld = os.listdir(src)
    print("ld:", ld)
    dirs = [d for d in ld if d not in excludes and os.path.isdir(src + "/" + d)]
    print ("dirs:", dirs)
    for d in dirs:
        try:
            shutil.copytree(src + "/" + d, dst + "/" + d)
            print(" - Copying: {0} : {1}".format(src + "/" + d, dst + "/" + d))
        except Exception as e:
            print(" - " + str(e))
            pass

    files = [f for f in ld if f not in excludes and os.path.isfile(src + "/" + f)]
    print ("files:", files)
    for f in files:
        try:
            shutil.copy(src + "/" + f, dst + "/" + f)
            print(" - Copying: {0} : {1}".format(src + "/" + f, dst + "/" + f))
        except Exception as e:
            print(" - " + str(e))
            pass

    print("=== Complete! ===")
    
