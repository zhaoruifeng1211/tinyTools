import math
import sys
file_path = sys.argv[1]

# Rest of the code...

pointsList = []
with open(file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        words = line.split()
        if((words[6]=='5')|(words[6]=='6')):
            pointsList.append([float(words[0]),float(words[1]),float(words[2])])

file_name = f"{file_path[:-4]}_building.xyz"    
with open(file_name, "w") as output_file:
    for point in pointsList:
        output_file.write(str(point[0])+" "+str(point[1])+" "+str(point[2])+"\n")