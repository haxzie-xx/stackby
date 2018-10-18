import re
from os import listdir, getcwd, makedirs
from os.path import isfile, isdir
from scripts import sb_date, sb_type, sb_ext, sb_multiple

# Recursive function to execute all categories after 0th category
def executeNextCategories(categories, start_index, dir):
    if start_index == len(categories):
        return
    else:
        folders = listdir(dir)
        for folder in folders:
            # Avoiding hidden folders
            result = re.match(r'^[^.]+$', folder)
            if not result:
              continue

            # Executing currCategory in this folder
            if categories[start_index]=="date":
                sb_date.stackby_date(dir+"/"+folder)
            elif categories[start_index]=="type":
                sb_type.stackby_type(dir+"/"+folder)
            else:
                sb_ext.stackby_extension(dir+"/"+folder)
            # Doing recursion
            executeNextCategories(categories, start_index+1, dir+"/"+folder)



def stackby_multiple_categories(categories,dir):
    #check if the directory is valid
    if not isdir(dir):
        print('Invalid Directory')
        return

    # Validating inputted categories
    if len(categories) == 0:
        print('No categories entered')
        return

    validCategories = ['type','date','ext']
    for category in categories:
        if not category in validCategories:
            print('Invalid category inputted')
            return

    # Executing 0th category
    if categories[0]=="date":
        sb_date.stackby_date(dir)
    elif categories[0]=="type":
        sb_type.stackby_type(dir)
    else:
        sb_ext.stackby_extension(dir)

    # Now calling recursive function for executing categories starting from 1st index
    executeNextCategories(categories,1,dir)
