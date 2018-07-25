states_abb = ['CT','DE','ME','MD','MA','NH','NJ','NY','PA','RI','VT','IA','MI','MN','WI','IL','IN','KY','MO','OH','TN','WV','AL','FL','GA','NC','SC','VA','MT','NE','ND','SD','WY','AR','KS','LA','MS','OK','TX','AZ','CO','NM','UT','ID','OR','WA','CA','NV']
state_names = ['Connecticut','Delaware','Maine','Maryland','Massachusetts','New Hampshire','New Jersey','New York','Pennsylvania','Rhode Island','Vermont','Iowa','Michigan','Minnesota','Wisconsin','Illinois','Indiana','Kentucky','Missouri','Ohio','Tennessee','West Virginia','Alabama','Florida','Georgia','North Carolina','South Carolina','Virginia','Montana','Nebraska','North Dakota','South Dakota','Wyoming','Arkansas','Kansas','Louisiana','Mississippi','Oklahoma','Texas','Arizona','Colorado','New Mexico','Utah','Idaho','Oregon','Washington','California','Nevada']

def get_fips(latitude, longitude):
    
    '''
    Uses https://geo.fcc.gov/api/census/ api to get FIPS code for that location
    '''

    response = requests.get('https://geo.fcc.gov/api/census/block/find?latitude='+str(latitude)+'&longitude='+str(longitude)+'&format=json')
    
    fips = str(response.json()['County']['FIPS']).zfill(5)
    
    return fips

def get_state_name(abbreviation):
    
    '''
    abbreviation: Two letter state abbreviation to get state name for
    '''
    
    for num, abb in enumerate(states_abb):
        
        if abb.upper() == abbreviation.upper():
        
            return state_names[num]
    
        else:
            
            pass
        
def get_state_abb(state_name):
    
    '''
    abbreviation: Two letter state abbreviation to get state name for
    '''
    
    for num, state in enumerate(state_names):
        
        if state_name == state:
            
            return states_abb[num]
            
        else:
            
            pass

        
        
population_response = requests.get('https://api.census.gov/data/2015/acs5?get=NAME,B01001_001E&for=county:*')
population_json = response.json()
population_frame = pd.DataFrame(population_json[1:],columns=population_json[0])
population_frame['Fips'] = population_frame['state'] + population_frame['county']

def get_population_by_fips(fips):
    
    '''
    Takes county Fips code and returns county population 
    '''
    
    return list(population_frame[population_frame['Fips'] == fips]['B01001_001E'])[0]



# Plotting statewide data --> frame should have two columns ('code': state abbreviations ('OH') and 'temperature': temperature data
import plotly.plotly as py
import pandas as pd

for col in df.columns:
    df[col] = df[col].astype(str)

scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
            [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]

data = [ dict(
        type='choropleth',
        colorscale = scl,
        autocolorscale = False,
        locations = frame['code'],
        z = frame['temperature'].astype(float),
        locationmode = 'USA-states',
        marker = dict(
            line = dict (
                color = 'rgb(255,255,255)',
                width = 2
            ) ),
        colorbar = dict(
            title = "Degrees (F)")
        ) ]

layout = dict(
        title = 'Temperature by State<br>(Hover for breakdown)',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showlakes = True,
            lakecolor = 'rgb(255, 255, 255)'),
             )
    
fig = dict( data=data, layout=layout )
py.iplot( fig, filename='d3-cloropleth-map' )

def CreateDates(start_date, end_date):
    
    '''
    Takes in start and end dates in the form of 'yyyy-mm-dd' and returns a list of dates that fall in between those two dates in
    the same format
    '''
    
    start_datetime = datetime.date(int(start_date.split('-')[0]), int(start_date.split('-')[1]), int(start_date.split('-')[2]))
    end_datetime = datetime.date(int(end_date.split('-')[0]), int(end_date.split('-')[1]), int(end_date.split('-')[2]))
    
    delt = end_datetime-start_datetime

    numdays = delt.days

    date_list = [start_datetime + datetime.timedelta(days=x) for x in range(0, numdays+1)]
    dates_for_reading = [date.strftime("20%y-%m-%d") for date in date_list]
    
    return dates_for_reading


ghcnd_txt_file = requests.get('https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt')
def find_ghcnd(ghcnd_code):
    
    '''
    Takes GHCND code in the form of 'USC00010823' and returns FIPS code for that county
    '''
    
    
    for line in ghcnd_txt_file.iter_lines():
    
        decoded = line.decode('utf-8')

        if ghcnd_code in decoded:

            latitude = decoded.split('  ')[1]
            longitude = decoded.split('  ')[2]
            
            print(latitude, longitude)

            response = requests.get('https://geo.fcc.gov/api/census/block/find?latitude={}&longitude={}&format=json'.format(latitude, longitude))
            print(response.json())
            fips = str(response.json()['County']['FIPS']).zfill(5)

            return fips
        
        else:
            
            pass
