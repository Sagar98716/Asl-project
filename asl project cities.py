import matplotlib.pyplot as plt

def extract_column_data(file_path, lines_to_extract, line_range='last'):
    """Extracts the second column for a given range of lines (first or last 50 lines)."""
    column_data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        if line_range == 'last':
            lines = lines[-lines_to_extract:]  # Get the last N lines
        else:
            lines = lines[:lines_to_extract]  # Get the first N lines

        for line in lines:
            columns = line.split()  # Split based on spaces/tabs
            if len(columns) > 1:  # Ensure the second column exists
                column_data.append(float(columns[1]))  # Convert to float if numerical
    return column_data

def plot_histograms(data1, data2, min_val, max_val):
    """Plots two histograms with the same bins."""
    bins = [min_val + i * (max_val - min_val) / 10 for i in range(11)]  # Create 11 edges for 10 bins

    plt.hist(data1, bins=bins, edgecolor='black', alpha=0.5, label='First 50 Lines')
    plt.hist(data2, bins=bins, edgecolor='black', alpha=0.5, label='Last 50 Lines')
    
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Second Column Data (First 50 vs Last 50 Lines)')
    plt.legend(loc='upper right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# File path
file1 = 'barcelona_result.txt'

# Given max and min values
max_val = 1.664
min_val = -0.811

# Extract the second column for the first 50 lines and the last 50 lines
first_50_lines_data = extract_column_data(file1, 50, line_range='first')
last_50_lines_data = extract_column_data(file1, 50, line_range='last')

# Plot both histograms on the same plot
plot_histograms(first_50_lines_data, last_50_lines_data, min_val, max_val)
