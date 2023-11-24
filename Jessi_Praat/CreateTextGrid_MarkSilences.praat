#################################################################
## Simple script to create text grids for all file in a folder. Tier 1 marking silences vs voiced. Tier 2 Transcription. Tier 3 Notes. Tier 4 Exclude.
## Made for Katerina by Jessi Oct 5 2023
#################################################################

# brings up form that prompts the user to enter directory name
# creates variable

## Directory with the wav file to process



soundDir$	= "D:\GitHub\experiment1\data\090101_REPSWITCH1_version1_list1_2023-11-22_13h45.01.739_micRespv1l1_recorded"
textDir$	= soundDir$



#clearinf

#Warning: voiced part detection has been set to 0.60 i/o 0.45 and
# the time set has been set to 0.09 s i/o 0.0


# Get the lists of all the signal in files in the given directory
Create Strings as file list... list 'soundDir$'/*.wav


# get number of files to process
numberOfFiles = Get number of strings

print 'numberOfFiles'

ifile = 1

# Deal file by file
while ifile <= numberOfFiles
    
   # select the list objects in Praat Objects window
   select Strings list

   # Get file name	
   fileName$ = Get string... ifile
   
   # strip extension to get basename
   name$ = fileName$ - ".wav"
   #namefi$ = fileName$ - ".wav"

   # read the wav file
   Read from file... 'soundDir$'/'fileName$'
    
	
   select Sound 'name$'
    

	To TextGrid (silences): 100, 0, -25, 0.1, 0.1, "silent", "sounding"
	#minimum silence duration (100 ms), silence threshold (0 dB), intensity threshold (-25 dB), and maximum interval duration (0.1 seconds)

	select TextGrid 'name$'
	Insert interval tier... 2 'SubjResponse'
	Insert interval tier... 3 'Modality_Correct'
	Insert interval tier... 4 'Item_Correct'
	Insert interval tier... 5 'Hesitation'
	Insert interval tier... 6 'Notes'
	Insert interval tier... 7 'Exclude'
	

    # save the textgrid with intensity boundaries

    select TextGrid 'name$'
    Write to short text file... 'textDir$'/'name$'.TextGrid


	
    #clean the object list and go the the next file
    ifile = ifile+ 1
    select Sound 'name$'
    plus TextGrid 'name$'
    Remove
endwhile
    

###### After you're done with all files, remove Strings object for complete object cleaning up
select Strings list
Remove

########################################################
## END OF SCRIPT
#######################################################
