# Extract_Images_Videos
This tool extracts Images (.jpg, .jpeg, .jfif, .webp), convert .jfif and .jpeg formats to .jpeg and extracts Videos (.mp4) from the downloaded / saved ".html" pages.

## Installation & Requirements
1. Install [Python 3](https://www.python.org/downloads/).
2. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [python-dotenv](https://pypi.org/project/python-dotenv/) and [Pillow](https://pypi.org/project/Pillow/).
```bash
pip install python-dotenv
pip install Pillow
```
3. Clone the Repository.

## Important notes
1. A few file Samples including ***".jpg's"*** are provided along with this tool for testing.
2. The value for variable ***self.MINIMUM_SIZE***  is set to ***"20"*** by default under *** ".env"*** file, indicating the minimum size of the ***"image"*** (i.e. 20kb) to be extracted. Change this value to ***"1"*** to include all the ***"image"*** files with size over 1kb.    
```bash 
MINIMUM_SIZE = 20
```
3. Images are extracted to the ***"output/images"*** directory and videos are extracted to the ***"output/videos"*** directory, ***temp*** directory is used as a temporary storage to keep the initially extracted files and are deleted at eventually.

## Running the application
1. Copy the saved ***".html"*** pages or any directories containing images and videos to the ***"input"*** directory. 
2. Navigate to the **Extract_Images_Videos** directory and run the following command:
```bash
python index.py
``` 
- ###### If Python 3 is installed along with Python 2, then use the following command.
```bash
python3 index.py
``` 

## License
[MIT](https://choosealicense.com/licenses/mit/)