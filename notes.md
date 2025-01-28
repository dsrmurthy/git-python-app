GIT with Python:

Install GIT
Create account in github.com
Create git-python-app folder and open it. add app.py and write code

add gitignore file to root of the app and write rules


//manually to add to github
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
-------------------------------------


CLick Source control icon in left side panel and click Initialize repository.
U => untracked file
M => Modified

Observe bottom left, branch name is main.
You can create new branch or rename with ctrl+shift+p

To track the file, click + symbol beside app.py (stage changes)
A -> new file added to repo.

To commit add message "first commit" and click right symbol and commit in source control.

To create new branch, ctrl+shift+p - type create branch and enter branch name. try.

From visual studio code, to publish new changes 
Goto github.com, create new repo: git-python-app
click create repo
add test.py file and write code
save all
enter commit message: test file added
click commit buttton or right symbol.
click sync changes - select Yes
Open github.com and see changes (files added)

To Delete a repo, click settings button,  select repo name  and go to last section ,click delete repo and confirm by entering password.
-------------------------------------------------------