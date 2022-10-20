# The data we need to retrive
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote. 

# Import the datetime class form the datetime module.
## import datetime
import datetime as dt
import csv
import random
import numpy
import os

# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()

# Print the present time.
print ("The time right now is", now)

# # Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'

# # Open the election results and read the file.
# election_data = open(file_to_load,'r')

# # To do: perform analysis.
# print ("Data file is being read")

# # Close the file.
# election_data.close()


# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # To do: perform analysis.
#     print(election_data)


# Assign a variable for the file to load and the path.

file_to_load = os.path.join("Resources","election_results.csv")

# Open the election results and read the file.

with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)
    
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)    

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

outfile = open(file_to_save,"w")

outfile.write("Hello World!")

outfile.close()

# Using the with statement open the file as a text file.
with open(file_to_save,"w") as txt_file:

    # # Write some data to the file.
    # txt_file.write("Hello World again!")


    # # Write three counties to the file.
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson")

    # # Write three counties to the file.
    # txt_file.write("Arapahoe\nDenver\nJefferson")

    txt_file.write("Counties in the Election\n------------------\nArapahoe\nDenver\nJefferson")

