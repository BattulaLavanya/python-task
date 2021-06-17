#Text Wrap

import textwrap

def wrap(string, max_width):
    i = 0
    l = list()
    
    for i in range(0,len(string),max_width):
        l.append(string[i:i+max_width])
    return "\n".join(l)
        
        
    

if __name__ == '__main__':
    string, max_width = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ', int(4)
    result = wrap(string, max_width)
    print(result)

 

    

