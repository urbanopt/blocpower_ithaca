import json
import csv 
import pandas as pd 

#This script takes a GeoJSON file as input, and demonstrates:
#a) writing a list of identifiers of the features to a CSV 
#b) modifying the original GeoJSON to add HVAC system types by feature ID, from an external CSV file. 
#Note that in practice, the output of a) could be used to generate input for b). As an illustration, separate
#files are used in this example. 

#To demonstrate the functionality of this script, one can add more ObjectIDs from the input GeoJSON to the 
#input data CSV, with a corresponding HVAC system type, and run this script in Python to see the modification. 

#The key used for identifying features ('ObjectID' in this cas) could easily be modified. 

#Set names of input files 
input_data='test_data.csv' #This file has feature IDs and names of their corresponding system types 
urbanopt_geojson_file='uo_test_file.json' #A typical UO geojson file--not used in this example. 
input_geojson_file='input_test_file.json' #A source GeoJSON file (this example is from Tompkins County) 

#use address to look up values 

#Read in input data 
data=pd.read_csv(input_data) 


def read_data(geojson_file): #Load a GeoJSON file 
     f = open(geojson_file, "r")   
     geojson=json.load(f)
     f.close()
     return geojson  

#This method modifies a GeoJSON file (the 'input GeoJSON file') to set system types of features by an id number, using data from the 'input data' file 
def process_item(ident, sys_type, geojson_file):  
    system=sys_type   
    geojson=read_data(geojson_file) 
    bldg= [obj for obj in geojson['features'] if obj['properties']['LOCADDR']==(ident)] #ObjectID is an identifier from the Tompkins County GeoJSON data 
    if bldg: #make sure list isn't empty 
        bldg[0]['properties']['system_type']=system 
        f = open(geojson_file, "w")
        json.dump(geojson, f, indent=4, sort_keys=True) #this formats the output GeoJSON 
        f.close()
    else:
        print("ID not present in GeoJSON file") 

#Process data (for generating csv) 
geojson = read_data(input_geojson_file) #Read in the input GeoJSON file 

#Print the IDs of the features in the input file 
output=[bldg['properties']['LOCADDR'] for bldg in geojson['features']] 
df = pd.DataFrame(output)
df.to_csv('bldg_id_list.csv')

#Modify the sample GeoJSON file to add HVAC system types. As an illustration, this uses a separate input data file. 
#As an illustration, this example includes one invalid GeoJSON ID in the test input CSV file. 
results = [process_item(row[0], row[1], input_geojson_file) for row in zip(data['id'], data['system_type'])] 


