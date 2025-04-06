#!/bin/bash

#creates 3 folders
mkdir Folder1
mkdir Folder2
mkdir Folder3

#navigate into folder 1
cd Folder1
#creates 3 subfolders in Folder1
mkdir Folder1/Subfolder1
mkdir Folder1/Subfolder2
mkdir Folder1/Subfolder3
#navigate into the subfolder 
cd Subfolder1

#removes folders 2 and 3 
rm -r Folder2 
rm -r Folder3
