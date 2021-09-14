# learnGit-Github
you can use "code ." to open vs code in current directory from command prompt
Git commands

    //these two commands to set global user name and email
    git config --global user.name "FIRST_NAME LAST_NAME"
    git config --global user.email "MY_NAME@example.com"

    //to initialize a new git repository in a folder
    git init

    //to stage a file in git repository
    //this will make git to track changes in file.
    git add FILE_NAME.extension

    //to commit file in git repository
    git commit  //this command will open directory to commit file
    git commit -m "description" 
    //always provide userful description in commit message

    //to review commit history in our porject
    git log

    //to look at configuration 
    git config -l

    //to check status of our project
    git status

    //to see difference between current file and it's previous commit
    git diff fileName.extension

    //when you want to commit small changes directly without staging the file
    git commit -a -m "description"

    //to see all the patches that have made to repository
    git log -p

    //to see a specific patche
    git show ad27e6c71afdbaa133258adb82cd6c33fe7485f4 (this is patch id)

    //to see how many lines have been added to in each patch
    git log --stat

    //to see difference between current files and commited files
    git diff

    //to add changes to staging area by reviewing them
    git add -p
    //in this command git will ask you for each changes do you want to add it staged or not

    //to see difference between current files and staged files
    git diff --staged

    * you should always use extension with a file name

    //when you want to delete a file you can use
    git rm filename //after that you have to commit the changes

    //when you want to rename a file you can use
    git mv oldfilename newfilename
    //this command can also be used to move file in directory

    //if you want to ignore some file then you can use
    echo filename > gitignore
    git rm --cached filename
    git commit -m "description"
    //git will ignore any changes in this file.

    //if you have done some commit and want to change/update that commit then
     git commit --amend will help

    Rollback
    //if you want to revert the last commit because if cause some issue to the project then
    git revert HEAD  //because head is pointing to the current snapshot of repository
    //this command do not delete the last commit but add the new commit inverting the last commit
    //so all the changes in last commit will cancel but history remain there.

    git log -p -2 //will show us the last two patches

    git show 89dfda89ew (commit id)
    //this will show info about commit
    //commit id is of 40 char - so you do not have to put 40 char to see commit
    //you can use initial 4-5 char to get that commit

    git revert 89dfda89ew
    //this will revert the commit with this id
    


    //to see the current branch
    git branch

    //to create new branch
    git branch new-branch-name

    //to switch to new branch
    git checkout new-branch-name

    //to create new branch and switch to it
    git checkout -b new-branch-name
    

    //to delete a branch
    git branch -d branch-name

    //git have two type of merg
        Fast forward merge -  when there is no commit in done in any one of the branch(in case to two branch) after creating new branch
            in this case git directly add new commit on one branch to another branch
        
        Three way merge - when there is new commits ammend to branch after creating new branch, then git does three way merge.
        and in some fashion add new commit on one branch to another branch.

    //to merge two branch (one is which in you are present, and one another branch is which you want to merge to you present branch)
    git merge branch-name

    //if there is some conflict in merge you can check git status
    and do changes in you file to fix the conflict and then commit
    which will merge the branch

    git log --graph --oneline
    //you can use this command to see converging and diverging of branch
    //with oneline commit statement

    Github
    git clone url //to clone a github repo
    git push //to push the current snapshot of repo
    git pull //to pull current snapshot of remote repo

    git config --global credential.helper cache //to cache credential so you don'that
    //have to enter id and password to login to git again again while pusing and pulling repo


    git remote // List remote repository

    git remote -v  //List remote reposs  verbosely

    git remote show repo_name // describe single remote repo

    git remote update //fetches the most up-to-date data from repo without merging them
    //so you can view it later

    git fetch //fetchs all data from repo
    git fetch [<options>] [<repository> [<refspec>…​]]
    git fetch [<options>] <group>
    git fetch --multiple [<options>] [(<repository> | <group>)…​]
    git fetch --all [<options>]

    //you can also give condition what you want to fetch

    git branch -r //list remote branch


    //fix merge conflict
    if there conflict you can check what's causing issue by 
    git log -p origin/master

    then you can fix it by editing the file and then commit.

    //if you use
    git pull // then it will automatically tries to merge your repo with origin/master
    //but if it's not then use the above given command to see issue and then fix it.

    //if you want to push a new branch
    //create a new branch from you local branch
    git checkout -b branch_name
    
    //add some changes to new branch & then
    git push -u orign branch_name //to push this branch to origin 
    //-u means upstream

    //to delete remote branch
    git push --delete origin branch_name## All commands availabe in git_commmands.txt

Feel free to check commands
