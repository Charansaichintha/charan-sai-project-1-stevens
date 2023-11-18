import csv
import argparse
import sys

def sum_numerical_columns(csv_file):
    # Initialize a dictionary to store column sums
    column_sums = {}

    try:
        with open(csv_file, 'r') as file:
            # Create a CSV reader object
            csv_reader = csv.DictReader(file)

            # Initialize column_sums based on the first row of data
            first_row = next(csv_reader)
            for col, value in first_row.items():
                try:
                    float(value)
                    column_sums[col] = 0
                except ValueError:
                    pass

            # Update column_sums with the rest of the data
            for row in csv_reader:
                for col, value in row.items():
                    if col in column_sums:
                        column_sums[col] += float(value)

    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        return 1  # Return non-zero exit code for file not found error
    except Exception as e:
        print(f"Error: {e}")
        return 2  # Return non-zero exit code for other errors

    # Print the column sums
    for col, total in column_sums.items():
        print(f"Sum of {col}: {total}")

    return 0  # Return exit code 0 for successful execution

def main():
    # Set up command line argument parser
    parser = argparse.ArgumentParser(description='Sum numerical columns in a CSV file.')
    parser.add_argument('csv_file', help='Path to the CSV file to process')

    # Parse command line arguments
    args = parser.parse_args()

    # Process the CSV file and return appropriate exit code
    sys.exit(sum_numerical_columns(args.csv_file))

if __name__ == "__main__":
    main()
