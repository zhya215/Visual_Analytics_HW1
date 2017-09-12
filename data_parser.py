import pandas as pd
import math
import itertools
from bokeh.palettes import Dark2_5 as palette

def parse_excel_data(directory, sheet_name):
    ds = pd.ExcelFile(directory)
    ds_df = ds.parse(sheet_name)
    return ds_df

def extract_column_names(df):
	return list(df)

def extract_row_names(df):
	return list(df.index)

#parameters: dataframe, countries list, years list, and dataset's name
def convert_df2json(df, countries, years, ds_name):
	data_json_list = []
	colors = itertools.cycle(palette)
	i = 0
	for country, color in zip(countries, colors):
	    # add the extracted json objects into data_json_list
	    data_json_list.append(extract_data(i, country, color, df, years, ds_name))
	    i += 1
	return data_json_list

# remove the datasets without values, and return the result in json format.
def extract_data(country_indice, country, color, df, years, ds_name):
    tmp_years = []
    tmp_ages = []
    # extract all years without data.
    # extract all not nan ages.
    i = 0
    for x in list(df.iloc[country_indice, :]):
        if math.isnan(x) != True:
            tmp_years.append(years[i])
            tmp_ages.append(x)
        i += 1
    tmp_json = {"country": country, "years": tmp_years, ds_name: tmp_ages, "color": color}
    return tmp_json