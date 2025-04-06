#!bin/bash/

#checks if the folder new_folder exists
# if it does, it will create a folder called if_folder
if [new_folder]
then
    echo "Folder already exists"
    mkdir if_folder
else
    mkdir new_folder
fi


#checks if the folder if_folder exists
# if it does, it will create a folder called hyperionDev
# if it does not, it will create a folder called new_projects
if [ -d if_folder ]
then
    echo "Folder exists. Creating hyperionDev folder"
    mkdir hyperionDev
else
    mkdir new_projects 
fi