import json
import csv 
import pandas as pd 

#read csv 

input_data='test_data.csv'
geojson_file='Sample_UO_GeoJSON.json'

#get list of IDs in the file 

#apply the below chunk to all IDs in the CSV 


def read_data(input_data, geojson_file):
     data=pd.read_csv(input_data) 
     #read in the GeoJSON data, add to it, and then write it out
     f = open(geojson_file, "r") #will need to close it
     #with open(geojson_file, 'a') as f:     
     geojson=json.load(f)
     f.close()

def process_item(item, geojson_file): #make that the list of IDs from the csv, each one is processed, get this called for each item in list 
    f = open(geojson_file, "w")
    index=input_data.loc[input_data['id'] == item].index[0]
    system=input_data['sys_type'][index]
    bldg= [obj for obj in geojson if obj['properties']['id']==item]  
    obj['properties']['system_type']=system
    json.dump(geojson, f)
    f.close()

    #return result

#results = [process_item(item) for item in item_list]


def write_data(geojson, geojson_file): 
     f = open(geojson_file, "w")
     print(geojson['features'][6]['properties']['system_type'])
     print(geojson['features'][6]['properties']['id'])
     geojson['features'][6]['properties']['system_type']='PTAC' #this worked successfully 
     json.dump(geojson, f)
     f.close()
     
      
     
     
     
     
#def write_geojson(data, geojson):

#loop thru the geojson data and the input data and update the geojson properties for each key in the input data file 

read_data(input_data, geojson_file) 


#call methods 