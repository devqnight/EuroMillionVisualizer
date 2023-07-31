from src.utils.config import Config
import utils.file as file
import utils.api as api
import json
import os



def get_data_to_json():
    euro_mil_data = api.get_parsed_data_from_api((Config()).cfg['API'])
    written = file.write_to_file('euro_million_data.json', json.dumps(euro_mil_data))
    if written:
        print('successfully wrote the data to json')
    else:
        print('failed to write data')
    return written

#get_data_to_json()



if __name__ == "__main__":

    pass

