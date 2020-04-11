# Download a sequence of file
# python download_sequential_files.py

import os
import re
import urllib.request


def increment_file_sequence(url):
    '''
    Increment the file sequence. Implementation is case specific meaning that to be used in another context this logic must be updated
    In this case 'image001.jpg' we know that the counter is the last part of the filename before the extension
    If for example we deal with '../pictures/01/image_1920x1080.jpg' where the conunter is inside the path we have to update this function
    '''
    path, filename = url.rsplit('/', 1)
    name, extension = filename.split('.')

    match = re.match(r"([a-z]+)([0-9]+)", name, re.I)
    base_filename, counter = match.groups()
    counter = str(int(counter) + 1).zfill(3)

    return path + '/' + base_filename +  counter + '.' + extension


def download_sequential_files(url_first_file, output_filepath):
    '''
    Download a sequence of file

    Arguments:
        url_first_file (str): urld of the first file to download
        output_filepath (str): download destination path

    Returns:
        None
    '''
    if not os.path.isdir(output_filepath):
        os.mkdir(output_filepath)
        
    next_download = True
    url = url_first_file

    while next_download == True:
        path, filename = url.rsplit('/', 1)
        print('Try download: {}'.format(filename), end = '')
        try:        
            urllib.request.urlretrieve(url, output_filepath + '/' + filename)
            print(' - Completed')
            url = increment_file_sequence(url)
        except:
            next_download = False
            print(' - Failed')


if __name__ == '__main__':
    #print(increment_file_sequence('http://699340.youcanlearnit.net/image001.jpg'))
    download_sequential_files('http://699340.youcanlearnit.net/image001.jpg', 'download')