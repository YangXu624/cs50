import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py CSVFILENAME TXTFILENAME")

    # TODO: Read database file into a variable
    dna_database = {}
    dna = []
    set = []
    names = []
    dna_num = 0
    counter = -1
    with open(sys.argv[1], "r") as database:
        reader = csv.reader(database)

        for index, row in enumerate(reader):
            if index == 0:
                num_obj = len(row) - 1

                for index1, obj in enumerate(row):
                    if index1 > 0:
                        dna.append(obj)
                        dna_num += 1

            if index > 0:
                for index1, obj in enumerate(row):
                    if index1 == 0:
                        if obj not in dna_database:
                            names.append(obj)
                            counter += 1
                            dna_database[names[counter]] = 0

                    for i in range(1, num_obj + 1):
                        set.append(row[i])

                    dna_database[names[counter]] = set
                    set = []

                print(f"Name: {names[counter]}, DNA Count: {dna_database[names[counter]]}")

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as text:
        sequence = text.read()

    # TODO: Find longest match of each STR in DNA sequence
        for i in range(dna_num):
            set.append(longest_match(sequence, dna[dna_num]))

    # TODO: Check database for matching profiles
        for i in range(counter):
            if set == dna_database[names[counter]]:
                print(dna_database[names])
            else:
                print("No match")

    return


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
