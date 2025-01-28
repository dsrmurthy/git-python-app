GIT with Python:

Install GIT
Create account in github.com
Create git-python-app folder and open it. add app.py

GIT allows source control to main as a central repo online

dsrmurthysoftare@gmail.com/boston@786
echo "# git-python-app" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/dsrmurthy/git-python-app.git
git push -u origin main

…or push an existing repository from the command line
git remote add origin https://github.com/dsrmurthy/git-python-app.git
git branch -M main
git push -u origin main

CLick Source control icon in left side panel and click Initialize repository.
U => untracked file
M => Modified

Observe bottom left, branch name is main.
You can create new branch or rename with ctrl+shift+p

To track the file, click + symbol beside app.py (stage changes)
A -> new file added to repo.

To publish add message "first commit" and click right symbol and commit in source control.

To create new branch, ctrl+shift+p - type create branch and enter branch name. try.

  