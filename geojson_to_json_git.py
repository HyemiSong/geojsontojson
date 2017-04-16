# ----------------------Python2.7 ------------------
# This program is used to marge geojson data to a json file
# A summary file and Geojson files are required

# First version Dec 15, 2016
# Copyright(c) Hyemi Song

# modified on Marth 29th, 2017
# Author: Hyemi Song

import sys, glob, csv, json

fname_summary_list = ['filename.csv']
path_list = ['foldername']
fname_output_list = ['filename.json']

for i, fname_summary in enumerate(fname_summary_list):
    path = path_list[i]
    f_output = open(fname_output_list[i], 'w')

    output_str = []
    with open(fname_summary, 'rb') as csvfile:
        csv_summary = csv.reader(csvfile, dialect='excel')

        for row in csv_summary:
            data_trajectory = []
            data_trajectory.append(map(str,row[2:3]))
            pathstring= path + '/' + str(row[4]) + '.geojson'
            print '%s', pathstring
            try:
                with open(path + '/' + str(row[4]) + '.geojson') as jsonfile:
                    json_trajectory = json.load(jsonfile)

                for feature in json_trajectory['features']:
                 # print feature['geometry']['type']
                 # print feature['geometry']['coordinates']
                 json_geometry = feature['geometry']['coordinates']

                 #  for row2 in json_trajectory:
                 #     data_trajectory.append(map(float,row2))

                 data_trajectory.append(map(int,row[17:]))
                 output_str.append({'id':int(row[0]), 'gen':str(row[2]), 'ag':str(row[3]), 'ty':str(row[5]), 'srt':str(row[8]), 'end':str(row[9]), 'dis':float(row[11]), 'dur':float(row[12]), 'p':json_geometry})

            except IOError:
                pass       
                print '****except****'
            
        json.dump(output_str, fp=f_output, sort_keys=True, separators=(',',':'))
    f_output.close()
