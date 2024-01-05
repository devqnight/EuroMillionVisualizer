import sys
from utils.utils import display_dict, display_mtx, arrayToStr
from utils.config import Config
import utils.file as file
import utils.api as api
import utils.mail as mail
from datetime import datetime
import json
import os

# normal grid positions : 1 2 3 4 5
# normal grid : 1 to 50
# star grid positions : 1 2
# star grid : 1 to 12

winning_grids = {
    '1':    [5,2],
    '2':    [5,1],
    '3':    [5,0],
    '4':    [4,2],
    '5':    [4,1],
    '6':    [3,2],
    '7':    [4,0],
    '8':    [2,2],
    '9':    [3,1],
    '10':   [3,0],
    '11':   [1,2],
    '12':   [2,1],
    '13':   [2,0]
}


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

def test_numbers(numbers, stars, latest_draw_nb, latest_draw_stars):
    cnt_nb = 0
    cnt_st = 0
    for nb in numbers :
        if str(nb) in latest_draw_nb:
            cnt_nb += 1   
    for st in stars :
        if str(st) in latest_draw_stars:
            cnt_st += 1
    return [cnt_nb, cnt_st]
 
def get_personal_numbers():
    path = os.path.join(os.getcwd(),'src','assets','personal_numbers.json')       
    if(os.path.isfile(path)):
        return json.loads(file.read_from_file(path))
    
def check_draw_mail(draw):
    personal = get_personal_numbers()
    res = []
    message = 'Date: ' + draw['date'] + '\n'\
            + 'Played numbers:\n'
    for x in personal:
        message += '    - numbers: ' + arrayToStr(x['numbers']) + '; stars: ' + arrayToStr(x['stars']) + '\n' 
        test = test_numbers(x['numbers'], x['stars'],draw['numbers'], draw['stars'])
        if test in list(winning_grids.values()):
            res.append([x['numbers'],x['stars'],test])
    message += '\n'
    message += 'Winning numbers: ' + arrayToStr(draw['numbers']) + ', stars: ' + arrayToStr(draw['stars']) + '\n'
    if len(res) == 0:
        message += 'Nothing won today...\n'
    else:
        for r in res:
            message += '    - '+arrayToStr(r[0])+';'+arrayToStr(r[1])+' : [n]='+r[2][0]+', [*]='+r[2][1]+';\n'
    
    mail.send_mail(message)

def check_date(date):
    draw = api.get_parsed_data_from_api_param_date((Config()).cfg['API'],date)
    check_draw_mail(draw[0])
    
def check_day():
    day = datetime.today().strftime('%Y-%m-%d')
    draw = api.get_parsed_data_from_api_param_date((Config()).cfg['API'],day)
    check_draw_mail(draw[0])

def check_all_ever():
    personal = get_personal_numbers()
    all_draws = get_data()
    final = []
    for draw in all_draws:
        for x in personal:
            test = test_numbers(x['numbers'],x['stars'],draw['numbers'], draw['stars'])
            if test in list(winning_grids.values()):
                d = {'date':draw['date'],'numbers':draw['numbers'], 'stars':draw['stars'], 'results':test, 'played':{'numbers':x['numbers'], 'stars':x['stars']}}
                final.append(d)
    path = os.path.join(os.getcwd(),'src','assets','results_ever.json')
    written = file.write_to_file(path, json.dumps(final))
    if written:
        print('successfully wrote the data to json')
    else:
        print('failed to write data')
    

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
        

if __name__ == '__main__':
    globals()[sys.argv[1]]()#(sys.argv[2])


# if __name__ == "__main__":
#     #print(os.getcwd())
#     data = get_data()
#     grid_rate, stars_rate = get_occurence_rate_per_number(data)
#     display_dict('grid',grid_rate,'%\n')
#     display_dict('stars',stars_rate,'%\n')
#     mtx_g, mtx_star = get_occurence_rate_per_number_per_position(data)
#     display_mtx('grid', mtx_g)
#     pass

