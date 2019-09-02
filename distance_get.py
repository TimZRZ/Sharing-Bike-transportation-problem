import csv
import math

csv_file = open("change_of_num_29result_13.csv", "r")
reader = csv.reader(csv_file)
latitude_list = []
longtitude_list = []
final_result = []

for row in reader:
    if row[3] != "latitude":
        latitude = (float(row[3])-37.750506)/(37.80477-37.750506)
        longtitude = (float(row[4])+122.4442926)/(-122.3904285+122.4442926)
        latitude_list.append(latitude)
        longtitude_list.append(longtitude)
        
csv_file.close()
for i in range (0,len(latitude_list)):
    result_for_i = [i+1]
    for j in range (0,len(latitude_list)):
        if j == i:
            result_for_i.append(100)
        if j != i:
            result_for_i.append(math.sqrt((latitude_list[i]-latitude_list[j])*(latitude_list[i]-latitude_list[j])+(longtitude_list[i]-longtitude_list[j])*(longtitude_list[i]-longtitude_list[j])))
    final_result.append(result_for_i)
csv_result_file = open("distance_result_13.csv", "w")
fileheader = ['']
for i in range (1,30):
    fileheader.append(i)
writer = csv.writer(csv_result_file, lineterminator='\n')
writer.writerow(fileheader)
rows = final_result
for row in rows:
    writer.writerow(row)
csv_result_file.close()
