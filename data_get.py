import csv

csv_file = open("201802-fordgobike-tripdata.csv", "r")
reader = csv.reader(csv_file)
station_id_list = []
result = []
for i in range (0,343):
    station_id_list.append(i)
    result.append(0)
for row in reader:
    if row[2] != "start_station_id":
        start_id = int(row[2])
        end_id = int(row[6])
        result[start_id] -= 1
        result[end_id] += 1
for i in range (0,343):
    result[i] = int(result[i]/28)
csv_file.close()

csv_result_file = open("change_of_num_result.csv", "w",newline="")
fileheader = ["station_id", "delta_num"]
writer = csv.writer(csv_result_file)
writer.writerow(fileheader)
rows = zip(station_id_list,result)
for row in rows:
    writer.writerow(row)
csv_result_file.close()
