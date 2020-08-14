import errno
import os
import shutil

from extensions import extension_dict

downloads_directory = r'C:\Users\TomBomb\Downloads'

try:
    os.makedirs(os.path.join(downloads_directory, 'Pictures'))
    os.makedirs(os.path.join(downloads_directory, 'Documents'))
    os.makedirs(os.path.join(downloads_directory, 'Torrent'))
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

for filename in os.listdir(downloads_directory):
    filename_without_extension, file_extension = os.path.splitext(filename)
    print('MOVING', filename, file_extension)

    if file_extension in extension_dict:
        shutil.move(os.path.join(downloads_directory, filename),
                    os.path.join(downloads_directory, extension_dict[file_extension]))
