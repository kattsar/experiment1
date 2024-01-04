#Description of this script
##  This script measures f0 and the first three formants at the midpoint of the vowel, and appends the
##  results to a text file.  It will be called "formant-log.txt", and will be written to the same
##  directory holding your sound files.
##  To run this script, you will have to have a bunch of sound files with accompanying text grids.  The
##  locations of vowels to be measured must be marked in tier 1 of the textgrid.  Anything with a non-null
##  label in that tier will be logged.
##  Modified by Jessi to save to new directory and include info from other tiers
##  Modified just for VOT and SOT
###End of description

##  Specify the directory containing your sound files in the next line:

inDirectory$ = "D:\GitHub\experiment1\data\250101_REPSWITCH1_version1_list1_2023-12-04_12h08.49.815_micRespv1l1_recorded\"
outDirectory$ = inDirectory$ 




##  Now I'm going to make a variable called "header_row$", then write that variable to the log file:

header_row$ = "Filename" + tab$ + "SubjResponse" + tab$  + "RT"+  tab$  + "Duration (ms.)" +  tab$ + "Modality_Correct" + tab$ + "Item_Correct" + tab$ + "Hesitation" + tab$ + "Notes" +  tab$  + "Exclude" + tab$ + newline$ 
header_row$ > 'outDirectory$'TestDataKaterina.txt



##  Now we make a list of all the sound files in the directory we're using, and put the number of
##  filenames into the variable "number_of_files":

Create Strings as file list...  list 'inDirectory$'*.wav
number_files = Get number of strings

# Then we set up a "for" loop that will iterate once for every file in the list:

for j from 1 to number_files

     #    Query the file-list to get the first filename from it, then read that file in:

     select Strings list
     current_token$ = Get string... 'j'
     Read from file... 'inDirectory$''current_token$'

     #    Here we make a variable called "object_name$" that will be equal to the filename minus the ".wav" extension:

     object_name$ = selected$ ("Sound")

  

    

     #    Now we get the corresponding TextGrid and read it in:

     Read from file... 'inDirectory$''object_name$'.TextGrid

     #    Now we query the TextGrid to get find out how many intervals there are in tier 1, storing
     #    that number in a variable called "number_of_intervals".  This is used to set up a for loop
     #    that will be used to go through each of the intervals and measure it (if its label is non-null).

     select TextGrid 'object_name$'
     number_of_intervals = Get number of intervals... 1
     for b from 1 to number_of_intervals
         select TextGrid 'object_name$'
          interval_label$ = Get label of interval... 1 'b'
			tier_two$ = Get label of interval... 2 1
			notes$ = Get label of interval... 6 1
			exclude$ = Get label of interval... 7 1			
			modality_correct$ = Get label of interval... 3 1
			item_correct$ = Get label of interval... 4 1
			hesitation$ = Get label of interval... 5 1
			


#Only Extract Formant Info on Intervals Labeled With V
          if interval_label$ = "sounding"
               begin_word = Get starting point... 1 'b'
               end_word = Get end point... 1 'b'
               #midpoint = begin_vowel + ((end_vowel - begin_vowel) / 2)
          
				rt = begin_word * 1000
               duration = (end_word - begin_word) * 1000
			   #notes$ = Get label of interval... 2 'j'

				
              fileappend "'outDirectory$'TestDataKaterina.txt" 'object_name$''tab$''tier_two$''tab$''rt:3''tab$''duration:3''tab$''modality_correct$''tab$''item_correct$''tab$''hesitation$''tab$''notes$''tab$''exclude$''tab$''newline$'
          endif
     endfor

     #  By this point, we have gone through all the intervals for the current sound object and
     #  textgrid, and written all the appropriate values to our log file.  We are now ready to go on to
     #  the next file, so we close can get rid of any objects we no longer need, and end our for loop

     select all
     minus Strings list
     Remove
endfor

# And at the end, a little bit of clean up and a message to let you know that it's all done.

select all
Remove
clearinfo
print All files have been processed.  What next?