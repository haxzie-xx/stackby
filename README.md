# StackBy [under development]
Simple python CLI to stack files in a directory based on type, date and extension.  
StackBy uses [Google's Fire module](https://github.com/google/python-fire) to make the command line interface. refer their docs for mode info.

### Installation
```
pip3 install -r requirements.txt
```
### Usage
```
#stack by file extension
$ python3 stackby.py ext <DIRECTORY_PATH>

#undo stacking operation
$ python3 stackby.py undo [DIRECTORY_PATH] [number of steps to undo]
$ python3 stackby.py undo ./test 2
default DIRECTORY_PATH is the present working directory and the default undo stepcount is 1.

#stack by creation date
$ python3 stackby.py created <DIRECTORY_PATH>

```

# Contributing
To contribute to the project, Please take up the tasks specified in the issues. Add a comment in the issues if you are taking up one. 
### Instructions
- Fork the repository to your account.
- Copy the clone url of your repository.
- Clone the repository to your machine `git clone https://github.com/YOUR_USER_NAME/stackby.git`
- Make sure you create a branch with the name as the issue you are working on `git checkout -b YOUR_BRANCH_NAME`, and make sure you are working on the same branch and not the `master`, run `git status` to know which branch you are working on, run `git branch`, your branch will be highlighted with an `*`. If you are not in your branch or want to move to another branch use `git checkout BRANCH_NAME`. 
a good branch name should explain what this branch is about eg. `stackby_type`, `stackby_date`, `feature_undo` etc.
- Add the upstream url of original repository, follow the instructions [here](https://help.github.com/articles/configuring-a-remote-for-a-fork/)
- Make sure your repository is in sync with the original repository's master branch. Follow the instruction [here](https://help.github.com/articles/syncing-a-fork/) to know how to keep your local repository in sync.
- Finally when you have made the changes, submit a pull request through github from the original repository, choose your branch against the master of original or create a new branch.
