import json
import csv 
import pandas as pd 

#Set names of input files 
input_data='test_data.csv'
urbanopt_geojson_file='uo_test_file.json'
input_geojson_file='input_test_file.json'

#get list of IDs in the file 

#apply the below chunk to all IDs in the CSV 

data=pd.read_csv(input_data) 



def read_data(geojson_file): 
     #read in the GeoJSON data, add to it, and then write it out
     f = open(geojson_file, "r")   
     geojson=json.load(f)
     f.close()
     return geojson  

#need to handle case when ID isn't present! 
def process_item(ident, sys_type, geojson_file): #make that the list of IDs from the csv, each one is processed, get this called for each item in list 
    system=sys_type   
    geojson=read_data(geojson_file) 
    print(ident)
    print(type(ident)) 
    bldg= [obj for obj in geojson['features'] if obj['properties']['OBJECTID']== int(ident)]
    print(bldg) 
    bldg[0]['properties']['system_type']=system 
    f = open(geojson_file, "w")
    json.dump(geojson, f)
    f.close()

geojson = read_data(input_geojson_file)
output=[bldg['properties']['OBJECTID'] for bldg in geojson['features']]
df = pd.DataFrame(output)
df.to_csv('bldg_id_list.csv')
results = [process_item(row[0], row[1], input_geojson_file) for row in zip(data['id'], data['system_type'])] 

#loop thru the geojson data and the input data and update the geojson properties for each key in the input data file 

