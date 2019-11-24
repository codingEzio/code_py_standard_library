import dis

code = """ 
my_dict = {'name': 'Alex'}
"""

print('Disassembly:\n')
dis.dis(code)

print('\nCode Details:\n')
dis.show_code(code)