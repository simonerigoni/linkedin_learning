# Create the directories to contains the challenges files
# python make_directories_and_files.py

import os

challenges = ['Find prime factors'
    , 'Identify a palindrome'
    , 'Sort a string'
    , 'Find all list items'
    , 'Play the waiting game'
    , 'Save a dictionary'
    , 'Set an alarm'
    , 'Send an email'
    , 'Simulate dice'
    , 'Count unique words'
    , 'Generate a password'
    , 'Merge CSV files'
    , 'Solve a Sudoku'
    , 'Build a ZIP archive'
    , 'Download sequential files'
]

if __name__ == '__main__':
    for directory in challenges:
        directory_name = directory.lower().replace(' ', '_')

        #print(directory_name)
        
        if os.path.isdir(directory_name) == False:
            os.mkdir(directory_name)

        filepath = directory_name + '/' + directory_name + '.py'
        
        if os.path.isfile(filepath) == False:
            with open(filepath, 'w') as python_file:
                python_file.write('#\n# python ' + directory_name + '.py')

        if os.path.isfile(filepath.replace('/', '/test_')) == False:
            with open(filepath.replace('/', '/test_'), 'w') as test_file:
                test_file.write('# Test\n# pytest')