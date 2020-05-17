import os
from glob import glob
from PIL import Image
import shutil
import sys
from pathlib import Path
from functools import reduce
from dotenv import load_dotenv
from tqdm import tqdm

class Extract:
    def __init__(self):
        load_dotenv()

        self.SOURCE_DIRECTORY = os.getenv("SOURCE_DIRECTORY")
        self.DESTINATION_DIRECTORY = os.getenv("DESTINATION_DIRECTORY")
        self.MINIMUM_SIZE_IMAGE = int(os.getenv("MINIMUM_SIZE_IMAGE"))
        self.SUPPORTED_FORMATS = ['*.' + value for value in os.getenv("SUPPORTED_FORMATS").split(',')]
        self.EXCEPTIONS = dict()

        try:
            if not os.path.exists(os.path.normpath(os.path.join(os.getcwd(), self.SOURCE_DIRECTORY))):
                os.makedirs(os.path.normpath(os.path.join(os.getcwd(), self.SOURCE_DIRECTORY)))
            if not os.path.exists(os.path.normpath(os.path.join(os.getcwd(), self.DESTINATION_DIRECTORY, 'images'))):
                os.makedirs(os.path.normpath(os.path.join(os.getcwd(), self.DESTINATION_DIRECTORY, 'images')))
            if not os.path.exists(os.path.normpath(os.path.join(os.getcwd(), self.DESTINATION_DIRECTORY, 'videos'))):
                os.makedirs(os.path.normpath(os.path.join(os.getcwd(), self.DESTINATION_DIRECTORY, 'videos')))
        except:
            print(f'\n*****\nALERT: {sys.exc_info()[1]}\nException type: {sys.exc_info()[0]}\n*****')
            sys.exit()

    def save(self):
        print("\n******************** PROCESSING ********************\n")

        count = 1
        for format in self.SUPPORTED_FORMATS:
            for file in glob(self.SOURCE_DIRECTORY + os.sep + '**' + os.sep + format, recursive=True): 
                try:
                    directory = os.path.normpath(os.path.join(os.getcwd(), self.DESTINATION_DIRECTORY))
                    file_name = Path(file).stem.split('.')[0] + reduce(lambda extension, each_extension : extension + each_extension, Path(file).suffixes)  # A file could have multiple extensions (i.e. example.taz.gz)
                    
                    if (format == '*.jpg' or format == '*.jpeg') and (os.path.getsize(file) / 1000) >= self.MINIMUM_SIZE_IMAGE: 
                        shutil.copy2(file, os.path.normpath(os.path.join(directory, 'images', file_name)))
                        print(f'{count}. {file_name} =====> output/images/{file_name}\n----------------------------------------------------------------------------------------')
                        count += 1
                    elif format == '*.jfif' or format == '*.webp' or format == '*.png' and (os.path.getsize(file) / 1000) >= self.MINIMUM_SIZE_IMAGE:       # Converting .jfif, .webp and .png to .jpg format and then save 
                        if len(Path(file).suffixes) == 1:
                            new_file_name = Path(file).stem.split('.')[0]
                        elif len(Path(file).suffixes) > 1:
                            new_file_name = reduce(lambda extension, each_extension : extension + '.' + each_extension, Path(file).stem.split('.'))
                        Image.open(file).convert("RGB").save(os.path.normpath(os.path.join(directory, 'images', new_file_name + ".jpg")), "jpeg")
                        print(f'{count}. {file_name} =====> output/images/{new_file_name}.jpg\n----------------------------------------------------------------------------------------')
                        count += 1
                    elif format == '*.mp4': 
                        shutil.copy2(file, os.path.normpath(os.path.join(directory, 'videos', file_name)))
                        print(f'{count}. {file_name} =====> output/videos/{file_name}\n----------------------------------------------------------------------------------------')
                        count += 1
                except:
                    self.EXCEPTIONS[f'File: {str(file)}'] = f'EXTRACTION Exception type: {sys.exc_info()[0]}, {sys.exc_info()[1]}'
                
    def check_exceptions(self):   
        if self.EXCEPTIONS:
            print("\n******************** EXCEPTIONS ********************")
            for key, value in self.EXCEPTIONS.items():
                print(f'{key} =====> {value}')
            print("\nEXTRACTION finished with one or more exceptions.....")
        else:
            print('\nEXTRACTION finished.....')
            
    def boot(self):
        self.save()
        self.check_exceptions()