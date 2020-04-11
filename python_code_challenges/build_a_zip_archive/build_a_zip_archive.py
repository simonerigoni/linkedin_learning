# Make a zip archive
# python build_a_zip_archive.py


import os
from zipfile import ZipFile


def zip_all(input_directory_path, file_extensions, output_filepath):
    '''
    Zip file

    Arguments:
        input_directory_path (str): directory path
        file_extensions (list): list of file extensions
        output_filepath (str): output filepath

    Returns:
        None
    '''
    with ZipFile(output_filepath, 'w') as output_zip:
        for root, directories, files in os.walk(input_directory_path, topdown = False):
            relative_path = os.path.relpath(root, input_directory_path)
            for filename in files:
                filepath, extension = filename.split('.')
                if extension.lower() in file_extensions:
                    output_zip.write(os.path.join(root, filename), arcname = os.path.join(relative_path, filename))


if __name__ == '__main__':
    zip_all('fiori', ['jpg', 'png'], 'flowers.zip')