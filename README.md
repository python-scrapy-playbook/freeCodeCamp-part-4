# Installation Guide
If you want to get started with part 4 of the FreeCodeCamp Python Scrapy course. Follow the steps below.

This repo contains two folders: 
1. bookscraper (Which you can use to follow the part 4 video/article)
2. full-bookscraper (The completed spider which you would have at the end of part 4)

## Step 1 - Install & activate your python virtual environment
To install the python virtual environment follow the following instructions below.

For Mac: https://thepythonscrapyplaybook.com/freecodecamp-beginner-course/freecodecamp-scrapy-beginners-course-part-2-scrapy-environment/#setting-up-your-python-virtual-environment-on-macos

For Windows: https://thepythonscrapyplaybook.com/freecodecamp-beginner-course/freecodecamp-scrapy-beginners-course-part-2-scrapy-environment/#setting-up-your-python-virtual-environment-on-windows 

For Linux: https://thepythonscrapyplaybook.com/freecodecamp-beginner-course/freecodecamp-scrapy-beginners-course-part-2-scrapy-environment/#setting-up-your-python-virtual-environment-on-linux

Then to activate it so that any new modules that are installed are installed into this virtual environment:

`source venv/bin/activate`



## Step 2 - Install the required python modules
To install the required modules for this python project to run you need to install the required python modules using the following command:

`pip install -r requirements.txt`


## Step 3 - Run the project/ Follow the course
Once the required python modules are installed you should be able to view/run the Python Scrapy Spider with the following command (from within the project folder):

View the project spiders: `scrapy list`

Run the project spider: `scrapy crawl books`