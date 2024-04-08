import math
import sys
file_path = sys.argv[1]

# Rest of the code...

points_list = []
ground='4.7'
with open(file_path, "r") as file:
    lines = file.readlines()
    # lines = lines[1:]  # Delete the first line
    for line in lines:
        words = line.split()
        
        points_list.append(words)        


# Create a file named after the RMSE value
file_name = f"{file_path[:-4]}_ground.xyz"
# points_list2=points_list
with open(file_name, "w") as output_file:
    for points in points_list:
        output_file.write(points[0]+" "+points[1]+" "+points[2]+"\n")
    for points2 in points_list:
        points2[2]=ground
        output_file.write(points2[0]+" "+points2[1]+" "+points2[2]+"\n")
        # print(points2)

print("successed")        
