import time
import os
import random
from github import Github
from git import Repo

inp = ""
interg = ""
original_repo_url = "https://github.com/PuppyStudios1/HashBrew-Cloud.git"
branchname = ""
name = ""
email = ""
pkgname = ""
pkgcontent = ""
locate = ""
download_url = ""
filename = ""
github = Github()
repo = github.get_repo(original_repo_url)

# Before Defines
def find_and_clone_file(original_repo_url, pkg, filename):
    
    """
    Searches a GitHub repository for a specific file within a given folder and clones it.

    Args:
        repo_url: The URL of the GitHub repository.
        pkg: The name of the folder to search within.
        filename: The name of the file to download.
    """
    repo = github.get_repo(original_repo_url)

    def recursive_search(pkgname):
        contents = repo.get_contents(pkgname)
        for content in contents:
            if content.type == "dir":
                recursive_search(repo.get_contents(content.path))
            elif content.name == filename:
                download_url = content.download_url
                os.system(f"curl -L {download_url} -o {filename}")
                print(f"File '{filename}' downloaded from folder '{pkg}' successfully.")
                return  # Exit the search once the file is found

        recursive_search(repo.get_contents(""))
        return
    # If the file is not found, raise an error.
    raise FileNotFoundError(f"File '{filename}' not found in repository.")

# Program starts here!
print("\n Welcome to HashBrew! v1.1 \n")
print("HashBrew Package Enviroment (HPE)")
print("Loading enviroment... \n")
time.sleep(3)

if __name__ == "__main__":          # <- Hash engine
    while True:
        inp = input("HashBrew@pkg:~$ ")

        if inp == "Hash":
            print("`Hash` command used externaly.")

        # if inp == "Hash Intergrate":
        #     interg = input("Enter Intergration ID: ")     <-- beta
        if inp == "Hash.Brewer":
            pkgname = input("Enter Package name: ")
            
            pkglanguage = input("package programming language: ")
            txtinf = input("Use nano or vim to make file? (call file main.[language name]): ")
            
            repo = "https://github.com/PuppyStudios1/HashBrew-Cloud.git"

            # Create the package directory
            os.makedirs(pkgname)

            # Create the main file
            with open(os.path.join(pkgname, f"main.{pkglanguage}"), "w") as f:
                # Write some initial code to the file (if desired)
                pass  # You can add initial code here if needed

            # Allow the user to edit the file using their preferred editor
            if txtinf == "nano":
                os.system(f"nano {pkgname}/main.{pkglanguage}")
            elif txtinf == "vim":
                os.system(f"vi {pkgname}/main.{pkglanguage}")

            # Add the package directory to the git repository
            os.chdir(pkgname)
            os.system("git init")
            os.system("git add .")
            os.system(f"git commit -m 'Initial commit'")
            os.system(f"git remote add origin {repo}")
            os.system("git push -u origin master")

            print(f"Package '{pkgname}' created and pushed to HashBrew Cloud")
            print(f"Package pushed to hashbrew cloud to get verified.")

        if inp == "clear":
            os.system("clear")

        if inp == "Hash install pkgutil":
            locate = input ("input cloud pkg directory: ")
            os.system("git clone https://github.com/PuppyStudios1/HashBrew-Cloud.git "+ locate)

        if inp == "Hash install":
            try:
                pkgname = input("Folder name? (package name): ")
                find_and_clone_file(original_repo_url, filename, download_url)
            except FileNotFoundError as e:
                print(e)

        if inp == "Hash --Update":
            os.system("python Update.py")
