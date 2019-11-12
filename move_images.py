import os
import glob
import shutil
import pathlib
import sys

class Move_images:
    
    def __init__(self):
        self.SOURCE_DIRECTORY = 'directories'
        self.TEMP = 'temp'
        self.DESTINITION_DIRECTORY = 'images'
        self.MINIMUM_SIZE = 20
        self.EXCEPTIONS = dict()                                    # To store all the exceptions
        
    def move(self):
       # Moving all the files from "directories" directory to "temp" directory 
        try:       
            for root, dirs, files in os.walk(self.SOURCE_DIRECTORY):
                for file in files:
                    path_file = os.path.join(root,file)
                    shutil.copy2(path_file, self.TEMP)
        except:
            print(f'\n*****\nALERT for FILE: {file}\nException: {sys.exc_info()[1]}\nException type: {sys.exc_info()[0]}\n*****\n')
            self.EXCEPTIONS[f'File: {str(file)}'] = f'Exception type: {sys.exc_info()[0]}, {sys.exc_info()[1]}'
    
        os.chdir(os.path.normpath(os.getcwd() + os.sep + self.TEMP))
        
        ########## Making sure only the .jpg and .jpeg files are moved to the "images" directory ##########
        for file in glob.glob('*.jpg'):
            try:
                # Discarding all the files which are less than 20KB in size
                if (os.path.getsize(file) / 1000) >= self.MINIMUM_SIZE:
                    shutil.move(f'{file}', os.path.normpath(os.getcwd() + os.sep + '..' + os.sep + str(self.DESTINITION_DIRECTORY)))  
            except:
                # print(f'\n*****\nALERT for FILE: {file}\nException: {sys.exc_info()[1]}\nException type: {sys.exc_info()[0]}\n*****\n')
                self.EXCEPTIONS[f'File: {str(file)}'] = f'Exception type: {sys.exc_info()[0]}, {sys.exc_info()[1]}'
            
        for file in glob.glob('*.jpeg'):
            try:
                # Discarding all the files which are less than 20KB in size
                if (os.path.getsize(file) / 1000) >= self.MINIMUM_SIZE:
                    shutil.move(f'{file}', os.path.normpath(os.getcwd() + os.sep + '..' + os.sep + str(self.DESTINITION_DIRECTORY)))  
            except:
                # print(f'\n*****\nALERT for FILE: {file}\nException: {sys.exc_info()[1]}\nException type: {sys.exc_info()[0]}\n*****\n')
                self.EXCEPTIONS[f'File: {str(file)}'] = f'Exception type: {sys.exc_info()[0]}, {sys.exc_info()[1]}'
                
        for file in glob.glob('*.jfif'):
            try:
                # Discarding all the files which are less than 20KB in size
                if (os.path.getsize(file) / 1000) >= self.MINIMUM_SIZE:
                    shutil.move(f'{file}', os.path.normpath(os.getcwd() + os.sep + '..' + os.sep + str(self.DESTINITION_DIRECTORY)))  
            except:
                # print(f'\n*****\nALERT for FILE: {file}\nException: {sys.exc_info()[1]}\nException type: {sys.exc_info()[0]}\n*****\n')
                self.EXCEPTIONS[f'File: {str(file)}'] = f'Exception type: {sys.exc_info()[0]}, {sys.exc_info()[1]}'
        ####################################################################################################
        
        ######### Deleting all the files from the "temp" directory
        for file in  glob.glob('*'):
            try: 
                os.remove(file)
            except:
                # print(f'\n*****\nALERT for FILE: {file}\nException: {sys.exc_info()[1]}\nException type: {sys.exc_info()[0]}\n*****\n')
                self.EXCEPTIONS[f'File: {str(file)}'] = f'Exception type: {sys.exc_info()[0]}, {sys.exc_info()[1]}'
     
    ########## Checking all the exceptions if required ##########          
    def check_exceptions(self):   
        if self.EXCEPTIONS:
            print("\nComplete with the following exceptions:")
            for key, value in self.EXCEPTIONS.items():
                print(f'{key} -----> {value}')
            print("\n")
        else:
            print("\nComplete.....\n")
        
obj = Move_images()
obj.move()
obj.check_exceptions()