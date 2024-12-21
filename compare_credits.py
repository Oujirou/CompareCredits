# Step 1: Remove all companies you don't want to compare against from text file.
# Step 2: Remove all major categories from file, leaving only the Title | Names sections.
# Step 3: Replace Mobygames credits.txt file with the following...
#   Find: ([A-Za-z0-9/ &,:-]+) \t
# 	Replace: \n
# Step 4: Remove the (as Person Name) entries.
#    Find:  \((as( [A-Za-z]+){1,4})\)
#    Replace: (Leave Empty)

# Example Run: 
#    python compare_credits.py BatmanArkhamCity.txt SuicideSquad.txt

# Search Name: ([éøñíłüáđa-zA-Z-]+) ([A-Z. ]+){0,3}(([é'íøłñüđá’'a-zA-Z-]+)[ ]{0,1}){1,3}

# Add argparser to allow for command line arguments.

import re
import os
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("file1", help="The first file to compare.")
parser.add_argument("file2", help="The second file to compare.")

args = parser.parse_args()

def read_file(file):
    with open(file, 'r') as f:
        contents = f.read()
        
        # Match the names in the file.
        matches = re.findall(r"([éøñíłüáđa-zA-Z-]+) ([A-Z. ]+){0,3}(([é'íøłñüđá’'a-zA-Z-]+)[ ]{0,1}){1,3}", contents)

        print(f"Found {len(matches)} matches in {file}.")

        return matches

firstGame = read_file(args.file1)
secondGame = read_file(args.file2)

foundNames = 0

for name in firstGame:
    if name in secondGame:
        foundNames += 1

print(f"Found {foundNames} names in both files.")

percentage1 = (foundNames / len(firstGame)) * 100
percentage2 = (foundNames / len(secondGame)) * 100

print(f"Percentage of people from {args.file1}  working on {args.file2}: {percentage1:.2f}%")
print(f"Percentage of people from {args.file2} that worked on {args.file1}: {percentage2:.2f}%")


# Example Output:
#   Found 139 matches in BatmanArkhamCity.txt.
#   Found 512 matches in SuicideSquad.txt.
#   Found 61 names in both files.
#   Percentage of people from BatmanArkhamCity.txt  working on SuicideSquad.txt: 43.88%
#   Percentage of people from SuicideSquad.txt that worked on BatmanArkhamCity.txt: 11.91%