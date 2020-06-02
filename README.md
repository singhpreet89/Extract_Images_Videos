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
  <a href="https://pypi.org/project/pipenv/" alt="Dependency: pipenv">
    <img src="https://badgen.net/badge/pipenv/v2020.5.28/148024" />
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
1. Install [Python 3](https://www.python.org/downloads/)
2. Clone the Repository.
3. Use the package manager [pip](https://pypi.org/project/pip/) to install [pipenv](https://pypi.org/project/pipenv/)
```bash
pip install pipenv
```
4. Install the required packages defined inside the pipfile.lock file using  [pipenv](https://pypi.org/project/pipenv/):
```bash
pipenv install --ignore-pipfile
```

## Important notes
1. Some sample **".jpg"** files are provided for testing in the **"input"** directory.
2. The value of **MINIMUM_SIZE**  is **"20"** by default in the ** ".env"** file, indicating that any **"image"** above **20kb** will be extracted.
  - However, updating the **MINIMUM_SIZE**  to **1** in the **".env"** file will include all the **"images"** irrespective of the size.
```bash 
MINIMUM_SIZE = 1
```

## Running the application
1. Copy the saved **web pages** or any directories containing **images** or **videos** to the **"input"** directory.
2. Navigate to the root directory and run the following command:
```bash
pipenv run python index.py
```
3. Images will be extracted in the **"output/images"** directory and videos will be extracted to the **"output/videos"** directory. These directories will be automatically created if  if not present.
  -  The **videos** extraction is not bound by any size. 
  
## License
[MIT](https://choosealicense.com/licenses/mit/)