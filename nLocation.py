from model import read_glacier_dataset
import math

def distance(x1, x2, y1, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def getInfo(lat, lng):
    df = read_glacier_dataset()
    df['distance'] = df.apply(lambda x: distance(lat, x['Latitude'], lng, x['Longitude']), axis=1)
    return df[df['distance']==df.distance.min()]
