import SoundLevelMeterUtility
import os 
import csv
import xmlrpclib
import datetime

ip_address = "http://128.171.152.55:9000"
server = xmlrpclib.Server(ip_address)


file_location = os.path.dirname(os.path.abspath(__file__))
output_location = os.path.dirname(os.path.abspath(__file__))
directory_list = os.listdir(output_location)

archive_list = []
with open("archive.csv", "r") as archive_file:
    reader = csv.reader(archive_file, delimiter = ",")
    for input_row in reader:
        archive_list.append(input_row[0])

output_location_list = []
for directory in directory_list:
    if ".py" not in directory and ".csv" not in directory and\
        "_output.csv" not in directory and\
        directory not in archive_list:
        date_stamp = directory.split(" ")[0]
        date_stamp = datetime.datetime.strptime(date_stamp,\
            "%Y-%m-%d").date()
        today_date_stamp = datetime.datetime.now().date()
        if today_date_stamp != date_stamp:
            output_location = os.path.dirname(os.path.abspath(__file__))
            output_location = os.path.join(output_location, directory)
            output_location_list.append(output_location)
            archive_list.append(directory)
        
output_location = os.path.abspath(__file__)
for directory in output_location_list:
    try: 
        SoundLevelMeter = SoundLevelMeterUtility.\
            SoundLevelMeterUtility(\
            directory, file_location)
        SoundLevelMeter.extract_data()
        data_file = SoundLevelMeter.return_output_filename()
#        with open(data_file, "rb") as handle:
#            binary_data = xmlrpclib.Binary(handle.read())
#            server.push_sinclair_data(binary_data,\
#                "sound_level_meter_raw_data", data_file)
        SoundLevelMeter.clean_folder()
    except Exception, e:
        print e
    


with open("archive.csv", "wb") as archive_file:
    writer = csv.writer(archive_file, delimiter = ",")
    for directory in archive_list:
        output_row = []
        output_row.append(directory)
        writer.writerow(output_row)

