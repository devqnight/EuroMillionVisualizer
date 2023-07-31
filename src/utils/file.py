

def write_to_file(file_name, data): 
    with open(file_name, 'w') as f:
        f.write(data)
    return f.closed
    
def read_from_file(file_name):
    f = open(file_name, 'r')
    data = f.read()
    f.close()
    return data
