def get_fips(latitude, longitude):
    
    '''
    Uses https://geo.fcc.gov/api/census/ api to get FIPS code for that location
    '''

    response = requests.get('https://geo.fcc.gov/api/census/block/find?latitude='+str(latitude)+'&longitude='+str(longitude)+'&format=json')
    
    fips = str(response.json()['County']['FIPS']).zfill(5)
    
    return fips
