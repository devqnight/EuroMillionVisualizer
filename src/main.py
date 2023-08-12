from utils.utils import display_dict
from utils.config import Config
import utils.file as file
import utils.api as api
import json
import os

# normal grid : 1 to 50
# star grid : 1 to 12


def get_data_to_json():
    path = os.path.join(os.getcwd(),'src','assets','euro_million_data.json')
    euro_mil_data = api.get_parsed_data_from_api((Config()).cfg['API'])
    written = file.write_to_file(path, json.dumps(euro_mil_data))
    if written:
        print('successfully wrote the data to json')
    else:
        print('failed to write data')
    return written

def get_data():
    path = os.path.join(os.getcwd(),'src','assets','euro_million_data.json')
    if(os.path.isfile(path)):
        return json.loads(file.read_from_file(path))

#get_data_to_json()

def get_occurence_rate_per_number(data):
    grid = {str(x):0 for x in range(1, 50+1)}
    stars = {str(x):0 for x in range(1, 12+1)}
    length = len(data)
    for res in data:
        for x in res["numbers"]:
            grid[x] += 1
        for x in res["stars"]:
            stars[x] += 1
    grid = {x:(grid[x]/length*100) for x in grid}    
    stars = {x:(stars[x]/length*100) for x in stars}       
    return grid, stars
    


if __name__ == "__main__":
    #print(os.getcwd())
    data = get_data()
    grid_rate, stars_rate = get_occurence_rate_per_number(data)
    display_dict('grid',grid_rate,'%\n')
    display_dict('stars',stars_rate,'%\n')
    pass

