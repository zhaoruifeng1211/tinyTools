import math
import sys
file_path = sys.argv[1]

# Rest of the code...

error_list = []
with open(file_path, "r") as file:
    lines = file.readlines()
    lines = lines[1:]  # Delete the first line
    for line in lines:
        words = line.split()
        error_list.append(float(words[3]))        


# Calculate the sum of squared differences
squared_diff_sum = sum((error) ** 2 for error in error_list)

# Calculate the RMSE
rmse = math.sqrt(squared_diff_sum / len(error_list))

# Create a file named after the RMSE value
file_name = f"{file_path[:-4]}_RMSE.txt"
with open(file_name, "w") as output_file:
    output_file.write(file_path + "\n")
    output_file.write("RMSE: " + str(rmse))

# Print the RMSE
print("RMSE:", rmse)        
