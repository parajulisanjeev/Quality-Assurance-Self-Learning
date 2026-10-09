# with open('demo.txt', 'w') as f:
#    f.write('This is a demo file for testing file handling in Python.')
# with open('demo.txt', 'a') as f:
#     f.write('\nThis line is appended to the demo file.')

# with open('demo.txt', 'r') as f:
#     print(f.read())

# with open('newfile.txt', 'x') as f:
#     f.write('This is a new file created using the x mode.')

import os
os.remove('newfile.txt')  # This will delete the newfile.txt file