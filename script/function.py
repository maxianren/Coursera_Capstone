print("hellow, future data scientist")
#corss group by pedestrain-severity
A_B=['PEDCOUNT','PEDCYLCOUNT', 'COLLISIONTYPE']
B_A=['PEDCYLCOUNT','PEDCOUNT','COLLISIONTYPE']

groupby_sort(A_B,B_A,90)

#corss group by cycle-severity

A_B=['PEDCYLCOUNT','SEVERITYCODE', 'COLLISIONTYPE']
B_A=['SEVERITYCODE', 'PEDCYLCOUNT','COLLISIONTYPE']

groupby_sort(A_B,B_A,90)

'''----------------------------------------------------------------------------'''

'''
chi-squre, p value, OR
'''

#OR
oddsratio, pvalue = stats.fisher_exact(pv)
print("OddsR: ", oddsratio, "p-Value:", pvalue)

#pivot table
pv=df.pivot_table(values='INC_hour', index='SEVERITYCODE',columns='PEDCOUNT',aggfunc='count')
pv.rename(columns={0:'no',1:'yes'},index={0:'no injury',1:'injury'})

#chi-square
chi2,p_value,freedom_degree,expected_frequencies = stats.chi2_contingency(pv)
print("chi-square: ", chi2, "p-Value:", '{0:.40f}'.format(p_value) )

'''----------------------------------------------------------------------------'''

'''
add marker on the map
'''

# instantiate a mark cluster object for the incidents in the dataframe
accidents = plugins.MarkerCluster().add_to(seattle_map)

# loop through the dataframe and add each data point to the mark cluster
for lat, lng, label, in zip(df_geo.Y, df_geo.X, df_geo.SEVERITYCODE):
    folium.Marker(
        location=[lat, lng],
        icon=None,
        popup=label,
    ).add_to(accidents)

# display map
seattle_map

'''----------------------------------------------------------------------------'''

'''
Geojson into dataframe
'''

#Json into df
#read json
with open(r'seattle_neighborhood.json', "r") as read_file:
    df_js = json.load(read_file)

#create new dictionary, keys -> new columns
dic_geo_js_seattle={'GEN_ALIAS':[],'DETL_NAMES':[],'NEIGHDIST':[],'AREA_ACRES':[],'AREA_SQMI':[],'OBJECTID':[]}

#extract info of new columns
for f in df_js['features']:
    dic_geo_js_seattle['GEN_ALIAS'].append(f['properties']['GEN_ALIAS'])
    dic_geo_js_seattle['DETL_NAMES'].append(f['properties']['DETL_NAMES'])
    dic_geo_js_seattle['NEIGHDIST'].append(f['properties']['NEIGHDIST'])
    dic_geo_js_seattle['AREA_ACRES'].append(f['properties']['AREA_ACRES'])
    dic_geo_js_seattle['AREA_SQMI'].append(f['properties']['AREA_SQMI'])
    dic_geo_js_seattle['OBJECTID'].append(f['properties']['OBJECTID'])

#new dictionary -> new df
df_geo_js_seattle=pd.DataFrame.from_dict(dic_geo_js_seattle)

#create random number of accidents for each neiborhood
arr_nhood=df_geo_js_seattle['NEIGHDIST'].unique()

random_accidents = np.random.randint(40,60,size=len(arr_nhood))

df_nhood_random=pd.DataFrame({'NEIGHDIST':arr_nhood,'count':random_accidents})

'''----------------------------------------------------------------------------'''

'''
Geojson into dataframe: centroid
'''
#read json
with open(r'seattle_neighborhood.json', "r") as read_file:
    df_js = json.load(read_file)

#create new dictionary, keys -> new columns
dic_geo_js_seattle={'GEN_ALIAS':[],'coordinates':[]}

#extract info of new columns
for f in df_js['features']:
    dic_geo_js_seattle['GEN_ALIAS'].append(f['properties']['GEN_ALIAS'])

    coordinates=f['geometry']['coordinates'][0]
    coordinates=[tuple(c) for c in coordinate]
    dic_geo_js_seattle['coordinates'].append(coordinates)

    #Polygon(coordinates).centroid.coords[0]

#new dictionary -> new df
df_geo_js_seattle=pd.DataFrame.from_dict(dic_geo_js_seattle)

df_geo_js_seattle
