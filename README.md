# treepy
A clone of tree, in python  

----
I made this because I wanted to be able to quickly compare the music directories on my desktop and my phone. I planned on doing so by outputting a tree by using the same script on both devices, and then using a diff tool to see what folders I didn't have on my phone.

The script outputs simultaneously to the terminal and to a file called TREE.txt. While doing `python treepy.py > TREE.txt` would have been possible, I found that it caused encoding errors - at least it does on Windows, which is significant for me since it's where I keep my music on my desktop. If you don't want that functionality you can easily comment it out.

Certain folders can be ignored by placing a text file named EXCLUDE.txt into the same directory the script is run from. Folder names should be separated by new lines.
