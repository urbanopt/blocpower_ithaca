import pandas as pd 
import Py_GeoJSON
from Py_GeoJSON import read_data
from Py_GeoJSON import process_item 


#read input files 
input_data='test_data.csv' #This file has feature IDs and names of their corresponding system types 
urbanopt_geojson_file='uo_test_file.json' #A typical UO geojson file--not used in this example. 
input_geojson_file='input_test_file.json' #A source GeoJSON file (this example is from Tompkins County) 


#Read in input data 
data=pd.read_csv(input_data) 

#Process data (for generating csv) 
geojson = read_data(input_geojson_file) #Read in the input GeoJSON file 

#Print the IDs of the features in the input file 
address=[bldg['properties']['LOCADDR'] for bldg in geojson['features']] 
floor_area=[bldg['properties']['SQ_FT'] for bldg in geojson['features']] 
output = pd.DataFrame(
    {'address': address,
     'floor_area': floor_area
    })
output.to_csv('bldg_data_output.csv')

#generate a list of the floor area also 

#Modify the sample GeoJSON file to add HVAC system types. As an illustration, this uses a separate input data file. 
#As an illustration, this example includes one invalid GeoJSON ID in the test input CSV file. 
results = [process_item(row[0], row[1], input_geojson_file) for row in zip(data['id'], data['system_type'])] 