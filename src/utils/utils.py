

def display_dict(name, data, ending='\n'):
    print(name,':')
    for x in data:
        print(x, ' = ', '%.2f'%data[x],end=ending)
        
