import sys
import os
import datetime
import csv

class SoundLevelMeterUtility:
    def __init__(self,\
        file_location = os.path.dirname(os.path.abspath(__file__)),\
        output_file_location = os.path.dirname(os.path.abspath(__file__))):
        self._file_location = file_location
        self._output_file_location = output_file_location
        self._output_file_name = "output.csv"
        
    def __add_output_file_location(self, filename):
        return os.path.join(self._output_file_location, filename)
        
    def extract_data(self):
        self.__reshape()
    
    def __reshape(self):
        input_filename = os.path.split(self._file_location)[-1] 
        input_file = open(input_filename, "r")
        reader = csv.reader(input_file, delimiter = ",")
        output_file_name = str(os.path.split(self._file_location)[-1]) +\
            "_output.csv"
        output_file_name = output_file_name.replace(" ", "_")
        output_file_name = output_file_name.replace(".txt", "")
        self._output_file_name = output_file_name
        output_file = open(output_file_name, "wb")
        writer = csv.writer(output_file)
        input_row = reader.next()

        while len(input_row) < 3:
            input_row = reader.next()

        output_row = []
        output_row.append("timestamp")
        output_row.append("sensor_id")
        output_row.append("value")
        writer.writerow(output_row)
        for input_row in reader:
            output_row = []
            sensor_id = "SDB7"
            timestamp = str(input_row[0] + " " + input_row[1])
            timestamp = datetime.datetime.strptime(timestamp,\
                "%d-%m-%Y %H:%M:%S")
            output_row.append(str(timestamp))
            output_row.append(sensor_id)
            output_row.append(input_row[-2])
            writer.writerow(output_row)
    
    def return_output_filename(self):
        return self._output_file_name
    
    def clean_folder(self):
        directory_list = os.path.split(self._file_location)
        directory_location = os.path.join(directory_list[:-1])
        directory_files_list = os.listdir(directory_location[0])
        for directory in directory_files_list:
            if "_output.csv" in directory:
                os.remove(directory)