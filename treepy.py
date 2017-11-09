# -*- coding: utf-8 -*-
# treepy - makes a directory tree. With Python.
# Reads a file called EXCLUDE.txt which can tell it to exclude certain folders
# writes the same tree it outputs to a file called TREE.txt
# ... because for some reason just like... piping it through into a file doesn't work.
# text encoding issues, lmao
import os, os.path, sys

def listdir(path="."):
    '''
    Returns a list of subdirectories in the current directory, sorted alphabetically
    Each entry in the list is another list, with the first element the name of the
    directory, and the second its path relative to the current one.
    If there are only files in the directory, an empty list is returned, natch.
    '''
    list = []
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_dir():
                list.append([entry.name, entry.path])
    list.sort(key=lambda element: element[0].lower()) # sorts by the directory name only
    return list

excludepath = os.path.join(".","EXCLUDE.txt")
if os.path.exists(excludepath):
    excludefile = open(excludepath)
    excludelist = excludefile.read().splitlines() # list of directory names to be excluded

treefilepath = os.path.join(".", "TREE.txt")
treefile = open(treefilepath, "w", encoding="utf8")

def treeloop(cwd, offset, treefile):
    heading = "|- "
    for dir in cwd:
        if os.path.exists(excludepath):
            if not (dir[0] in excludelist):
                print("".join([" "*offset,heading,dir[0]]))
                treefile.write("".join([" "*offset,heading,dir[0],"\n"]))
                subdir = listdir(dir[1])
                if subdir != []:
                    treeloop(subdir, offset + 1, treefile)
        else:
            print("".join([" "*offset,heading,dir[0]]))
            treefile.write("".join([" "*offset,heading,dir[0],"\n"]))
            subdir = listdir(dir[1])
            if subdir != []:
                treeloop(subdir, offset + 1, treefile)

#topdir @
if len(sys.argv) == 1:
    topdir = listdir(os.path.abspath("."))
else:
    topdir = listdir(sys.argv[1])
offset = 0 # this will offset the heading

#print("printing sys.argv 0 and 1")
#print(sys.argv[0], sys.argv[1])
treeloop(topdir, offset, treefile)
