# Extract_Images_Videos
<p align="center">
	<a href="https://www.python.org/" alt="MADE WITH: PYTHON">
		<img src="https://forthebadge.com/images/badges/made-with-python.svg" />
	</a>
</p>
<p align="center">
  <a href="https://www.python.org/downloads/" alt="Powered by: Python 3.8.2">
    <img src="https://badgen.net/badge/Powered%20by/Python%20v3.8.2/3570A0" />
  </a>
  <a href="https://pypi.org/project/Pillow/" alt="Dependency: Pillow">
    <img src="https://badgen.net/badge/Pillow/v7.1.2/148024" />
  </a>
  <a href="https://pypi.org/project/python-dotenv/" alt="Dependency: python-dotenv">
    <img src="https://badgen.net/badge/python-dotenv/v0.13.0/148024" />
  </a>
	<a href="https://opensource.org/licenses/MIT" alt="License: MIT">
		<img src="https://img.shields.io/badge/License-MIT-green.svg" />
	</a>
</p>
<p align="center">
  <strong>This tool extracts .jpg, .jpeg, .jfif, .webp and .png images, convert the extracted .jfif, .webp and .png formats to .jpeg and extracts Videos (.mp4) from the downloaded / saved ".html" pages.</strong>
</p>

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
2. The value for variable ***MINIMUM_SIZE***  is ***"20"*** by default and it provided under the *** ".env"*** file, indicating the minimum size of an ***"image"***  to be extracted is 20kb.
3. Update the ***MINIMUM_SIZE = 1*** in the ***".env"*** file to include all the ***"images"*** irrespective of their size. 
```bash 
MINIMUM_SIZE = 1
```
4. Images are extracted to the ***"output/images"*** directory and videos are extracted to the ***"output/videos"*** directory. These directories are automatically created on the fly.

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