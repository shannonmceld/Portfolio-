import csv
import sys
from sys import argv
import re
import pickle


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    database = []
    # TODO: Read database file into a variable
    myfile = sys.argv[1]
    with open(myfile) as file:
        reader = csv.DictReader(file)
        for i in reader:
            name = i["name"]
            AGATC = i["AGATC"]
            AATG = i["AATG"]
            TATC = i["TATC"]
            # name,AGATC,TTTTTTCT,AATG,TCTAG,GATA,TATC,GAAA,TCTG
            database.append({"name": name, "AGATC": AGATC, "AATG": AATG, "TATC": TATC})

    # TODO: Read DNA sequence file into a variable
    txtfile = sys.argv[2]
    with open(txtfile, "r") as file:
        data_sequence = file.read().rstrip()

    # TODO: Find longest match of each STR in DNA sequence
    subsequences = list(database[0].keys())[1:]

    STRs = {}
    for subsequence in subsequences:
        STRs[subsequence] = longest_match(data_sequence, subsequence)

    # TODO: Check database for matching profiles
    for dict in database:
        match = 0
        for subsequence in subsequences:
            if int(dict[subsequence]) == STRs[subsequence]:
                match += 1
        if match == len(subsequences):
            print(dict["name"])
            return

    print("No Match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
