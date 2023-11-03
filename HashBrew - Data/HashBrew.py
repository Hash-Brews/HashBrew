import sys
import os

# End of imports
package_amount = 0
package_name = " "

commands = ["Hash", "Hash.Brew/#/bin install", "Hash.Brew/#/bin uninstall", "Hash.list", ".help", "Hash.ext"]
global installed_packages
installed_packages= []

def main():
  
  command = input("$ ")

  if command in commands:
      if command == "Hash":
          print("The `Hash` command is used to install, uninstall, and manage packages.")
      elif command == "Hash.Brew/#/bin install":
          package_name = input("please enter the package to install: ")
          # package_amount += 1
          installed_packages.append(package_name)
          package_code = input("Put code for the package: ")
          if package_name!="":
              save_installed_packages(package_name)
              print(f"Successfully installed {package_name}!")
          else:
              print(f"The package Package {package_name} is not installed...")

          print("Usage: Hash.Brew/#/bin install <package_name>")
      elif command == "Hash.ext":
          exit()
      elif command == "Hash.list":
          list_installed_packages()
      elif command == ".help":
          print("The `Hash` command is used to install, uninstall, and manage packages.")
          print("The `Hash.Brew/#/bin install` command is used to install packages.")
          print("The `Hash.Brew/#/bin uninstall` command is used to uninstall packages.")
          print("The `Hash.list` command is used to list all installed packages.")
          print("The `.help` command is used to display help for commands.")
      elif command == 'Hash.Brew/#/bin uninstall':
        print('Yet to implement code')
        #TODO
      else:
        print("Command not found in HashBrew.")

def save_installed_packages(package_name):
  with open(package_name +".py", "w") as f:
    writeable_packages = ','.join(installed_packages)
    f.write(writeable_packages)

def load_installed_packages(package_name):
  try:
    with open(package_name +".py", "r") as f:
      installed_packages = f.read()
  except FileNotFoundError:
    installed_packages = []

def list_installed_packages(package_name):
  try:
    with open('installed_packages.txt','r') as f:
      installed_packages = f.read()
  except:
    installed_packages =""
  if installed_packages != "":
    print(installed_packages)
  else:
    print("You have no Packages installed in your HashBrew Ref.")
    
def exit():
  print("Ending Session...")
  time.sleep(2)
  exit()

if __name__ == "__main__":
  while True:
    package_amount += 1
    main()
