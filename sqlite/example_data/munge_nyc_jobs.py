#PART 1: OPEN ORIGINAL DATA FILE

import codecs
f = codecs.open("./nyc_jobs.csv", mode='r', encoding='utf-8')

#loop through each line in the file
firstLine = True #flag/sentinel

#make a blank dictionary that will hold the agency names and ids
agencies = {}

#keep track of numbers we've used before as ids
id_counter = 1

all_lines = [] #this will store all lines of data as we want to save it


#PART 2: MUNGE DATA FROM FILE

for line in f:
    #check whether flag is true
    if firstLine == True:
        #if so, set it to false, and skip to the next line
        firstLine = False
        continue

    #at this point, we can assume we are at a line of data
    line_data = line.split(",")
    agency_name = line_data[1]

    #see whether this agency has already got an id
    if agency_name in agencies.keys():
        #if it does, then figure out it's id, which is the key
        agency_id = agencies[agency_name]

    else:
        agency_id = str(id_counter)
        id_counter = id_counter + 1
        agencies[agency_name] = agency_id

    # at this point, our dictionary has all the agencies we've found so  far...
    # and we know the id and name in the current row of the file

    # overwrite the agency name in the second field in the line with the id
    line_data[1] = agency_id

    #add this data to the all_lines list
    all_lines.append(line_data)


#PART 3: WRITE NEW JOBS DATA FILE

#create a new text file with just the data for the jobs table
jobs_file = codecs.open("jobs_data.csv", mode='w', encoding='utf-8')

for line in all_lines:
    line_text_with_commas = ",".join(line)
    #print("printing line...")
    jobs_file.write(line_text_with_commas)

jobs_file.close() #close the file when done


#PART 4: WRITE NEW AGENCIES DATA FILE

#create a new text file with just the agencies data
agencies_file = codecs.open("agencies_data.csv", mode='w',encoding='utf-8')

for item in agencies.items():
    line_text_with_commas = str(item[0]) + "," + str(item[1])
    agencies_file.write(line_text_with_commas + "\n")

agencies_file.close() #close the file