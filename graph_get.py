import csv
import matplotlib.pyplot as plt

csv_file = open("change_of_num_11result.csv", "r")
reader = csv.reader(csv_file)
latitude_list = []
longtitude_list = []

for row in reader:
    if row[3] != "latitude":
        latitude = (float(row[3])-37.750506)/(37.80477-37.750506)
        longtitude = (float(row[4])+122.4442926)/(-122.3904285+122.4442926)
        latitude_list.append(latitude)
        longtitude_list.append(longtitude)
        
plt.scatter(longtitude_list, latitude_list, s=10)
plt.show()
