import pandas as pd 
import Py_GeoJSON_Test 
from Py_GeoJSON_Test import read_data
from Py_GeoJSON_Test import process_item 


#read input files 
input_data='test_data.csv' #This file has feature IDs and names of their corresponding system types 
urbanopt_geojson_file='uo_test_file.json' #A typical UO geojson file--not used in this example. 
input_geojson_file='input_test_file.json' #A source GeoJSON file (this example is from Tompkins County) 


#Read in input data 
data=pd.read_csv(input_data) 

#Process data (for generating csv) 
geojson = read_data(input_geojson_file) #Read in the input GeoJSON file 

#Print the IDs of the features in the input file 
output=[bldg['properties']['LOCADDR'] for bldg in geojson['features']] 
df = pd.DataFrame(output)
df.to_csv('bldg_id_list.csv')

#Modify the sample GeoJSON file to add HVAC system types. As an illustration, this uses a separate input data file. 
#As an illustration, this example includes one invalid GeoJSON ID in the test input CSV file. 
results = [process_item(row[0], row[1], input_geojson_file) for row in zip(data['id'], data['system_type'])] 