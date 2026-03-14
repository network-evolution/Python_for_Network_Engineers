import platform
import sys
import importlib.metadata

##############################################
print(f"\n###### Installed Libraries ############")
for dist in importlib.metadata.distributions():
    print(f"{dist.metadata['Name']}=={dist.version}")

# Print the Python version and other details
print(f"\n###### Python Environment Details ######")
print(f"Python Version       : {platform.python_version()}")
print(f"Python Implementation: {platform.python_implementation()}")
print(f"Executable Path      : {sys.executable}")
print(f"Platform             : {platform.system()} {platform.release()}\n\n")
##############################################

import getpass

password = getpass.getpass("Enter password: ")
print("Password received (hidden)")
