## CONDA CODES

#Check & version		
conda info
#Update conda itself	
conda update conda
#Install a package		
conda install PACKAGENAME
#Update a package 		
conda update PACKAGENAME

#Command help		
conda COMMANDNAME --help (eg. conda install --help)
#Create an env 	
conda crate --name ENVNAME python=3.5

#List all environments 					
conda env list
#List all packages in the active env 	
conda list
#Make a copy of an environment 			
conda create --clone ENV1 --name ENV2
#Delete an env and all in it 			
conda env remove --name ENVNAME
