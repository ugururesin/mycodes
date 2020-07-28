#! bin/bash

## CONNECTING TO DGX-S
ssh uuresin@10.45.80.12
cd /mnt/dgx1_data/data

## CONNECTING TO DGX-1
ssh uuresin@10.45.80.11
cd /raid/data
#####################################################################################################

## SCP (SECURE COPY) EXAMPLES
#############################
# LOCAL --> REMOTE
$ scp /localpath/file.txt username@to_host:/remote/directory/
$ scp -r /local/directory/ username@to_host:/remote/directory/

# REMOTE --> LOCAL
$ scp username@from_host:file.txt /local/directory/
$ scp -r username@from_host:/remote/directory/  /local/directory/
 
# REMOTE --> REMOTE
$ scp username@from_host:/remote/directory/file.txt username@to_host:/remote/directory/
#####################################################################################################

## FIND NUMBER OF FILES (in the parent folder)
find . -type f | wc -l
#####################################################################################################
