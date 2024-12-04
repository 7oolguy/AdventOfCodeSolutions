"""
--- Day 2: Red-Nosed Reports ---
Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?
"""


file_path = r"2\input.txt"

# Initialize the data
data = []

# Read the file and process the numbers
try:
    with open(file_path, "r") as file:
        for line in file:
            # Extract numbers from the line
            row = [int(num) for num in line.split()]
            data.append(row)

except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# data [[1,2,3,4,5,6,7], [2,1,0,2,3,4,5]] EXEMPLE

def is_safe_report(report):
    # Check if the report is strictly increasing or decreasing
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]

    # Verify all differences are within the range [1, 3] or [-3, -1]
    if all(1 <= diff <= 3 for diff in differences):
        return True  # Increasing and valid differences
    if all(-3 <= diff <= -1 for diff in differences):
        return True  # Decreasing and valid differences

    return False  # Not safe


# Count the number of safe reports
safe_count = sum(is_safe_report(report) for report in data)

print(f"The number of safe reports is: {safe_count}")
