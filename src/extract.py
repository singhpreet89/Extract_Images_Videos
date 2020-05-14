import os
from glob import glob
from PIL import Image
import shutil
import sys
from dotenv import load_dotenv

class Extract:
    def __init__(self):
        load_dotenv()

        self.SOURCE_DIRECTORY = os.getenv("SOURCE_DIRECTORY")
        self.TEMP = os.getenv("TEMP_DIRECTORY")
        self.DESTINATION_DIRECTORY = os.getenv("DESTINATION_DIRECTORY")
        
        # Minimum size of an Image to be extracted
        self.MINIMUM_SIZE = int(os.getenv("MINIMUM_SIZE"))

        self.SAVE_FORMATS = ['*.' + value for value in os.getenv("SAVE_FORMATS").split(',')]
        self.CONVERT_TO_JPG = ['*.' + value for value in os.getenv("CONVERT_TO_JPG").split(',')]
    
        self.EXCEPTIONS = dict()                
    
    def copy_to_temp(self):
        print('Please wait.....')

        # pylint: disable=unused-variable   #(Since "directories" variable is not being used)
        for root, directories, files in os.walk(self.SOURCE_DIRECTORY):
            for file in files:
                try: 
                    path_file = os.path.join(root, file)
                    shutil.copy2(path_file, self.TEMP)
                except:
                    # print(f'\n*****\nALERT for FILE: {file}\nException: {sys.exc_info()[1]}\nException type: {sys.exc_info()[0]}\n*****\n')
                    self.EXCEPTIONS[f'File: {str(file)}'] = f'Exception type: {sys.exc_info()[0]}, {sys.exc_info()[1]}'
        os.chdir(os.path.normpath(os.getcwd() + os.sep + self.TEMP))

    def convert(self):
        for format in self.CONVERT_TO_JPG:
            try:
                for file in glob(format):
                    webp_image_name = os.path.splitext(file)[0]
                    Image.open(file).convert("RGB").save(webp_image_name + ".jpg", "jpeg")
            except:
                self.EXCEPTIONS[f'File: {str(file)}'] = f'Exception type: {sys.exc_info()[0]}, {sys.exc_info()[1]}'
        print("\nConversion to .jpg complete.....")    
            
    def extract(self):
        for format in self.SAVE_FORMATS:
            for file in glob(format):
                try:
                    if (format == '*.jpg' or format == '*.jpeg') and (os.path.getsize(file) / 1000) >= self.MINIMUM_SIZE:
                        shutil.move(f'{file}', os.path.normpath(os.getcwd() + os.sep + '..' + os.sep + str(self.DESTINATION_DIRECTORY) + os.sep + 'images'))
                    elif format == '*.mp4':
                        shutil.move(f'{file}', os.path.normpath(os.getcwd() + os.sep + '..' + os.sep + str(self.DESTINATION_DIRECTORY) + os.sep + 'videos'))
                except:
                    self.EXCEPTIONS[f'File: {str(file)}'] = f'Exception type: {sys.exc_info()[0]}, {sys.exc_info()[1]}'

    def delete_temp_directory(self):
        for file in glob('*'):
            try: 
                os.remove(file)
            except:
                # print(f'\n*****\nALERT for FILE: {file}\nException: {sys.exc_info()[1]}\nException type: {sys.exc_info()[0]}\n*****\n')
                self.EXCEPTIONS[f'File: {str(file)}'] = f'Exception type: {sys.exc_info()[0]}, {sys.exc_info()[1]}'
        print("\nTemporary files deleted.....")
              
    def check_exceptions(self):   
        if self.EXCEPTIONS:
            print("\n******************** EXCEPTIONS ********************")
            for key, value in self.EXCEPTIONS.items():
                print(f'{key} =====> {value}')
            print("\nFINISHED with one or more exceptions.....")
        else:
            print("\nFINISHED.....\n")
            
    def boot(self):
        self.copy_to_temp()
        self.convert()
        self.extract()
        self.delete_temp_directory()
        self.check_exceptions()