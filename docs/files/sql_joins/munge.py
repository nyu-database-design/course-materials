#PART 1: OPEN ORIGINAL DATA FILE

import codecs, csv
f = codecs.open("NYC_Jobs.csv", mode='r', encoding='utf-8')
reader = csv.DictReader(f) # use csv module to create dictionaries for each row in CSV

#create a new text file with just the data for the jobs table
jobs_file = codecs.open("jobs_data.csv", mode='w', encoding='utf-8')
jobs_fields = ['id', 'job_id', 'agency_id', 'title', 'salary_range_from', 'salary_range_to'] # fields in the jobs file
jobs_writer = csv.DictWriter(jobs_file, fieldnames=jobs_fields)

#create a new text file with just the agencies data
agencies_file = codecs.open("agencies_data.csv", mode='w',encoding='utf-8')
agencies_fields = ['agency_id', 'agency_name'] # fields in the agencies file
agencies_writer = csv.DictWriter(agencies_file, fieldnames=agencies_fields)

#make a blank dictionary that will hold the agency names and ids
agencies = {}

#keep track of numbers we've used before as ids
job_counter = 0
agency_counter = 0

for row in reader:
    
    ## STEP 1: deal with this job's Agency
    agency_name = row['Agency'] # extract the agency name for this job

    #see whether we have already assigned this agency a unique ID
    if agency_name in agencies.keys():
        #if yes, then figure out it's id, which is the key
        agency_id = agencies[agency_name]

    else:
        # give a new unique id to this agency
        agency_id = str(agency_counter)
        agency_counter = agency_counter + 1
        # write this agency's data to the file
        agencies_writer.writerow({
            'agency_name': agency_name, 
            'agency_id': agency_id 
        })
        # add this agency to our dictionary of agencies
        agencies[agency_name] = agency_id
        
    # add the agency ID to the dictionary
    row['Agency_id'] = agency_id

    ## STEP 2: deal with this job data
    jobs_writer.writerow({
        'id': job_counter,
        'job_id': row['Job ID'],
        'agency_id': agency_id, 
        'title': row['Business Title'],
        'salary_range_from': row['Salary Range From'], 
        'salary_range_to': row['Salary Range To']
    })

    job_counter += 1 # increment the job counter

#PART 3: WRITE NEW JOBS DATA FILE

jobs_file.close() #close the file when done
agencies_file.close() #close the file
f.close()