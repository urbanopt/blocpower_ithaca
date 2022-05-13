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

#The key used for identifying features ('LocAddr' in this case) could easily be modified. 



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




