#################################################################
## Amelie 2015
## For each file in SoundDir : open the wav file and associated textgrid in TextDir  with the same name + an extension
#################################################################

# brings up form that prompts the user to enter directory name
# creates variable

soundDir$	= "D:\GitHub\experiment1\data\010101_REPSWITCH1_version1_list1_2023-11-10_13h54.48.695_micRespv1l1_recorded"
textDir$	= soundDir$

pattern$ 	= ""

ext$		= ""

# Makes list of files to be labelled, creates a variable with basename of file
# opens loop 



Create Strings as file list... list 'soundDir$'/*speak*.wav

numberOfFiles = Get number of strings

ifile = 1

# Deal file by file
while ifile <= numberOfFiles
	
   	#current file
   	select Strings list

   	fileName$ = Get string... ifile

       	#strip extension to get basename
   	name$ = fileName$ - ".wav"
  
	
	idx  = index (fileName$, pattern$)
   	printline 'fileName$'

	### subselct the file to process
	if idx <> 0

		#load and open wav and textgrid together
   		Read from file... 'soundDir$'/'fileName$'
		select Sound 'name$'
	
		Read from file... 'textDir$'/'name$''ext$'.TextGrid
         	 	select TextGrid 'name$''ext$'
		plus Sound 'name$'
 		Edit
		
		# ask for modification
   		pause Modify text grid if required

		select TextGrid 'name$''ext$'

		print  'textDir$'/'name$''ext$'.TextGrid
		
		# save modifications
		Write to short text file... 'textDir$'/'name$''ext$'.TextGrid

		###### Cleaning up objects before proceeding to the next file
		select all
		minus Strings list
		Remove

		
		
	endif
	
	ifile = ifile + 1

endwhile

###### After you're done with all files, remove Strings object for complete object cleaning up
select Strings list
Remove

########################################################
## END OF SCRIPT
#######################################################
