import argparse
import statistics

def read_data(filename):
    data = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if i >= 3:  # Skip the first two lines                                                                                                
                try:
                    # Split the line by commas and extract the third column (which is at index 2)                                                 
                    parts = line.split(',')
                    value = int(parts[2].strip())  # Strip any extra spaces and convert to integer                                                
                    data.append(value)
                except (ValueError, IndexError):
                    print(f"Invalid data at line {i+1}: {line.strip()}")
    return data

def calculate_statistics(data):
    stats = {}
    stats['mean'] = statistics.mean(data)
    stats['median'] = statistics.median(data)
    stats['mode'] = statistics.mode(data) if len(data) > 0 else None
    stats['std_dev'] = statistics.stdev(data) if len(data) > 1 else 0
    stats['min'] = min(data)
    stats['max'] = max(data)

    return stats

def print_statistics(data, stats):
    print("Values Considered for the 3rd Column:")
    print(data)  # Print the data array used in the statistics                                                                                    

    print("\nStatistical Information for the 3rd Column:")
    print(f"Mean: {stats['mean']}")
    print(f"Median: {stats['median']}")
    print(f"Mode: {stats['mode']}")
    print(f"Standard Deviation: {stats['std_dev']}")
    print(f"Min: {stats['min']}")
    print(f"Max: {stats['max']}")

if __name__ == "__main__":
    # Set up the argument parser                                                                                                                  
    parser = argparse.ArgumentParser(description="Process a file and calculate statistics for the third column.")
    parser.add_argument('filename', type=str, help="The file to be processed")

    # Parse the arguments                                                                                                                         
    args = parser.parse_args()

    # Read the data from the file provided as a command-line argument                                                                             
    data = read_data(args.filename)

    if len(data) > 0:
        stats = calculate_statistics(data)
        print_statistics(data, stats)
    else:
        print("No valid data found in the file.")




