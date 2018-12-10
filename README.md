# StackBy [![forthebadge](https://forthebadge.com/images/badges/contains-technical-debt.svg)](https://forthebadge.com)
Python CLI to stack files in a directory based on type, date and extension.  
StackBy uses [Google's Fire module](https://github.com/google/python-fire) to make the command line interface. Refer their docs for mode info.

### Installing requirement (libmagic)
**For OSX users**  
Using Homebrew: ```  brew install libmagic ```  
Using macports: ``` port install file ```   

### Installation
Install the package from PyPI
```
$ pip3 install stackby
```
If you encounter any permission error, use
```
$ sudo -H pip3 install stackby
```
### Usage

StackBy is a handy CLI tool to make your life easier to clean up your folder with random files. StackBy can create separate subdirectories for files based on their extension, type or created date.

#### Stack files by their extension  
CD into the directory to clean up.
```
$ stackby ext
```
or simply specify the directory path to clean up.
```
$ stackby ext DIRECTORY_PATH
```

#### stack by creation date
```
$ stackby date
```
or simply specify the directory path to clean up.
```
$ stackby date DIRECTORY_PATH
```  

#### stack by predefined type
```
$ stackby type
```
or simply specify the directory path to clean up.
```
$ stackby type DIRECTORY_PATH
```  

#### stack by multiple categories
```
$ stackby multiple --categories=[LIST_OF_CATEGORIES_SEPARATED_BY_COMMAS] DIRECTORY_PATH
```
**Example to clean current directory by extension, then by date.**
```
$ stackby multiple --categories=[ext,date]
```  

#### Undo stacking in a directory  
You can undo the last stacking inside a directory. CD into the directory where files has been stacked from. Make sure there exists the `.stackby` file.
```
$ stackby undo
```
or simply supply the DIRECTORY_PATH where the `.stackby` file resides
```
$ stackby undo DIRECTORY_PATH
```
_Default DIRECTORY_PATH is the present working directory and by default it reverts all the stacked files in the directory._

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
