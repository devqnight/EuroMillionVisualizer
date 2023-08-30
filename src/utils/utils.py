

def display_dict(name, data, ending='\n'):
    print(name,':')
    for x in data:
        print(x, ' = ', '%.2f'%data[x],end=ending)
        
def display_mtx(name, data):
    print(name, ':') 
    print((' '*4 + '+')+('-'*4)+('-'*5 + '+')*len(data[list(data.keys())[0]]))
    print(padding(4, '')+'|    ', end='')
    for x in list(data[list(data.keys())[0]]):
        print(padding(5,x)+x, end='|')
    print() 
    print(('-'*4 + '+')+('-'*4)+('-'*5 + '+')*len(data[list(data.keys())[0]]))
    for key, value in data.items():
        print(key, padding(3, key) + '|    ', end='')
        for keyy, valuey in value.items():
            end = ('|\n' if int(keyy) == len(value) else '|')
            print(padding(4,str(valuey)),valuey, end=end)    
        print(('-'*4 + '+')+('-'*4)+('-'*5 + '+')*len(data[list(data.keys())[0]]))
            
def padding(length, word):
    return (length - len(word)) * ' '