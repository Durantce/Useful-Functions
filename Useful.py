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
