import sys
import os
import time

# End of imports

commands = ["Hash", "Hash.Brew/#/bin install", "Hash.Brew/#/bin uninstall", "Hash.list", ".help"]
installed_packages = []

def main():

  command = input("$ ")
  # if len(sys.argv) < 2:
  #   print("Usage: Hash <command> [args]")
  #   sys.exit(1)

  # command = sys.argv[1]

  if command in commands:
      if command == "Hash":
          print("The `Hash` command is used to install, uninstall, and manage packages.")
      elif command == "Hash.Brew/#/bin install":
          if len(sys.argv) < 3:
            print("Usage: Hash.Brew/#/bin install <package_name>")
            # sys.exit(1)
          package_name = input("please enter the package to install: ")
          installed_packages = [package_name]
          package_Language = input("Package Language (py,js,cpp ect):")
          package_code = input("Put code for the package: ")
          
          
          # package_name = sys.argv[2]
          save_installed_packages()
          print(f"Successfully installed {package_name}.")
      elif command == "Hash.Brew/#/bin uninstall":
          if len(sys.argv) < 3:
            print("Usage: Hash.Brew/#/bin uninstall <package_name>")
            sys.exit(1)

          # package_name = sys.argv[2]
          package_name = input("please enter the package to install")
          if package_name in installed_packages:
            save_installed_packages()
            print(f"Successfully uninstalled {package_name}!")
          else:
            print(f"The package Package {package_name} is not installed...")
      elif command == "Hash.list":
          list_installed_packages()
      elif command == ".help":
          print("The `Hash` command is used to install, uninstall, and manage packages.")
          print("The `Hash.Brew/#/bin install` command is used to install packages.")
          print("The `Hash.Brew/#/bin uninstall` command is used to uninstall packages.")
          print("The `Hash.list` command is used to list all installed packages.")
          print("The `.help` command is used to display help for commands.")
  else:
    print("Command not found in HashBrew.")

def save_installed_packages():
  with open("installed_packages.txt", "w") as f:
    writeable_packages = ','.join(installed_packages)
    f.write(writeable_packages)

def load_installed_packages():
  try:
    with open("installed_packages.txt", "r") as f:
      installed_packages = f.read()
  except FileNotFoundError:
    installed_packages = []

def list_installed_packages():
  if installed_packages != " ":
    print(installed_packages)
  else:
    print("You have no Packages installed in your HashBrew Ref.")

if __name__ == "__main__":
  load_installed_packages()
  while True:
    main()
