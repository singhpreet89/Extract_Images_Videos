# Extract_Images_Videos
This tool extracts Images (.jpg, .jpeg, .jfif, .webp), convert the extracted .jfif and .webp formats to .jpeg and extracts Videos (.mp4) from the downloaded / saved ".html" pages.

## Installation & Requirements
1. Install [Python 3](https://www.python.org/downloads/).
2. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [python-dotenv](https://pypi.org/project/python-dotenv/) and [Pillow](https://pypi.org/project/Pillow/).
```bash
pip install python-dotenv
pip install Pillow
```
3. Clone the Repository.

## Important notes
1. A few samples including ***".jpg's"*** are provided for testing in the ***"input"*** directory.
2. The value for variable ***self.MINIMUM_SIZE***  is set to ***"20"*** by default under *** ".env"*** file, indicating the minimum size of the ***"image"***  to be extracted is 20kb.
3. Update the ***MINIMUM_SIZE = 1*** in ***".env"*** file to include all the ***"image"*** files irrespective of their size. 
```bash 
MINIMUM_SIZE = 20
```
4. Images are extracted to the ***"output/images"*** directory and videos are extracted to the ***"output/videos"*** directory, ***temp*** directory is automatically created and is used as a temporary storage and its content is deleted when the program finishes execution.

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