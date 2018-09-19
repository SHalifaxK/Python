'''
xmltodics usage
'''

import xmltodict

'''
Use context manager to read in the xml and conver it to dict and save the result to tree variable
'''

with open('L1_param.xml','r') as f:
    tree = xmltodict.parse(f.read())

'''
print out the 'nested value' that you want from dict
'''

print(tree['L1_parameters']['Parameters']['ant_port_layer'])
