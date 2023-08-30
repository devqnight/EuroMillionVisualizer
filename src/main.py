from utils.utils import display_dict, display_mtx
from utils.config import Config
import utils.file as file
import utils.api as api
import json
import os

# normal grid positions : 1 2 3 4 5
# normal grid : 1 to 50
# star grid positions : 1 2
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
 
def get_occurence_rate_per_number_per_position(data):
    matrix_g = {str(x):{str(y):0 for y in range(1, 51)} for x in range(1,6)}
    matrix_star = {str(x):{str(y):0 for y in range(1, 13)} for x in range(1,3)}
    length = len(data)
    for res in data:
        for idx, x in enumerate(res["numbers"]):
            matrix_g[str(idx+1)][x] += 1
        for idx, x in enumerate(res["stars"]):
            matrix_star[str(idx+1)][x] += 1
    return matrix_g, matrix_star
        


if __name__ == "__main__":
    #print(os.getcwd())
    data = get_data()
    grid_rate, stars_rate = get_occurence_rate_per_number(data)
    display_dict('grid',grid_rate,'%\n')
    display_dict('stars',stars_rate,'%\n')
    mtx_g, mtx_star = get_occurence_rate_per_number_per_position(data)
    display_mtx('grid', mtx_g)
    pass

