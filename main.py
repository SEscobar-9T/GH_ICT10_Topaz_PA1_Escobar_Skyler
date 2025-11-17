from pyscript import display

comarts = {'Carl', 'Shino', 'AJ'} # specified sets

glee = {'Jalainie', 'Sang-Heon', 'Carl'} # specified sets

display(comarts, target='output1')
display(glee, target='output2')

check_comarts = 'Carl' in comarts # check item
check_glee = 'Carl' in glee

display(check_comarts, target='output1')
display(check_glee, target='output2')

check_comarts = 'AJ' in comarts # check item for first club
display(check_comarts, target='output1')

check_glee = 'Jalainie' in glee # check item for second club
display(check_glee, target='output2')

check_glee = 'Sang-Heon' in glee # check item for 1 club
display(check_glee, target='output2')
