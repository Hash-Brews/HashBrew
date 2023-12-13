import time
import os
print("Updating... please wait...")
time.sleep(6)
os.system("https://github.com/Hash-Brews/HashBrew-Updater.git")
os.system("rm -rf ./HashBrew.py")
os.system(f"python HashBrew.py")
