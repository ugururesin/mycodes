#! /bin/bash

######################################################################
## LINUX BASH COMMANDS ##

## GENERAL FORMAT: command -argument ##

## BASIC COMMANDS ##
####################
cd . 		#GET THE CURRENT WD  
cd ..		#ONE WD ABOVE 	  
cd ~		#USER'S HOME DIR.  
cd /		#FILE SYSTEM ROOT   
cd -		#LAST VISITED WD   
pwd			#PRINT CURRENT WD   

ls 			#SHOW FILES & FOLDERS
-l 			#LIST FILES & FOLDERS
ls *.json	#LIST .json FILES
ls -lha 	#LIST ALL FILES
lsblk		#LIST BLOCK DEVICES

cat 				#OPEN a FILE
cp myfile /newpath/ #COPY a FILE 	  
cp *.* /newpath/	#COPY ALL FILES	  
mv myfile /newpath/	#MOVE a FILE

rm 			#REMOVE a FILE
rm *.*		#REMOVE ALL FILES   
rm *.jpeg 	#REMOVE JPEG FILES   

mkdir 		#CREATE a FOLDER   
rmdir		#REMOVE a FOLDER    

echo 'hello World!'	#PRINTS Hello World!  

## CHECKS & INFO ##
###################
du -h myfolder/		#SIZE OF A FOLDER (myfolder)


## STDIN & STDOUT ##
####################
STDIN: Inputs
STDOUT: Outputs

# |   LHS command's STDOUT -> to RHS command as STDIN
# >   LHS command's STDOUT -> overwrites to a file
# >>   LHS command's STDOUT -> appends to a file

# EXAMPLES:
echo 'hello world' | wc -w 		#returns 2!
ls - l > mylist.txt
date >> mydate.txt


# EXITING #
###########
@ Bash:		CTRL+c 	q 	exit
@Python:	quit()	CTRL+d
@Nano:		CTRL+x
@Vim:		:q!


## CONNECTING TO REMOTE MACHINE (EXAMPLE: DGX-S 10.45.80.12 & ~11 for DGX-1)
ssh uuresin@10.45.80.12
######################################################################


## COMMON PLACES
DGX-S: /mnt/dgx1_data/data
DGX-1: /raid/data
######################################################################


######################################################################
## SCP (SECURE COPY) EXAMPLES
# LOCAL --> REMOTE
$ scp /localpath/file.txt username@to_host:/remote/directory/
$ scp -r /local/directory/ username@to_host:/remote/directory/

# REMOTE --> LOCAL
$ scp username@from_host:file.txt /local/directory/
$ scp -r username@from_host:/remote/directory/  /local/directory/
 
# REMOTE --> REMOTE
$ scp username@from_host:/remote/directory/file.txt username@to_host:/remote/directory/
######################################################################

## MOVE ALL FILES INTO THE PARENT FOLDER (NOT FOR HIDDEN FILES)
mv * ../

## MOVE FILES WHOSE NAME LENGTH GREATER THAN 14 INTO DIR a/
for f in *; do if [ ${#f} -gt 14 ]; then mv $f a/; fi; done

## FIND NUMBER OF FILES (in the parent folder)
find . -type f | wc -l

## FIND ALL FILES IN THIS DIRECTORY AND ITS SUB-DIRECTORIES AND EXECUTE MV WITH TARGET DIRECTORY .
## FOR EACH FILE FOUND TO MOVE THEM TO CURRENT DIRECTORY.
find . -mindepth 2 -type f -print -exec mv {} . \;

## MOVE/COPY FIRST 10000 FILES INTO A FOLDER
mv `ls | head -10000` /media/uuresin/b1792e39-fd40-4c3e-8feb-24c592d30037/processed_data/2020_04_13/


## BASIC FUNCTIONS
print_something() {
	echo Enter the path where the input file is located!
	read input_path
}


echo The given input_path is $input_path
######################################################################