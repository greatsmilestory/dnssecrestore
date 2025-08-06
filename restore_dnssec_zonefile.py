# Set file paths
input_file = 'input.txt'
output_file = 'output.txt'

try:
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Initialize a list to store filtered lines
    filtered_lines = []

    # Initialize i and use a while loop to process lines
    i = 0
    while i < len(lines):
        if lines[i].startswith('			RRSIG'):
            # If a line starts with 'RRSIG', skip this line and the next 5 lines
            i += 6
        elif 'NSEC3' in lines[i]:
            # If a line contains 'NSEC3', skip this line
            i += 1
        else:
            # Add the line to the result list if it doesn't match any condition
            filtered_lines.append(lines[i])
            i += 1

    # Write the modified content to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(filtered_lines)

    print(f"Processing completed. The result has been saved to {output_file}.")

except FileNotFoundError:
    print(f"The file {input_file} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
