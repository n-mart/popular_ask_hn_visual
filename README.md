# Popular Ask-HN Visual 

This is a program that by default fetches the top 20 'Ask HN'-style posts from the Hacker News API based on the number of votes each post gets, and then uses the Python module Plotly to create a both informative and interactive visualisation on the data.

## Installation instructions

I reccomend running this program in a virtual environment, using a module such as venv. This is so that all the packages used in the program are isolated from your system, and can easily be removed by removing the folder containing this project.

First download the zip file and extract it. Navigate into the folder, and from there create a virtual environment (with venv, you would use the command 'python -m venv venv', then activate the virtual environment by typing in 'source venv/bin/activate')

Type in 'pip install -r requirements.txt' to automatically install the required packages.

Then, run the program by executing main.py with the command 'python main.py'.

## Configuration

Currently, you can configure the number of Ask-HN posts that you want to include in the plot. By default, this is set to 20, however you can configure it to be a different value by going into main.py, and entering an integer into the my_api_call instance, as shown below:

my_api_call = pav.PopularAsksVisual(*number*)

Be sure though, not to enter a very large number. There are only so many posts that the Hacker News API can store, and if you surpass that number, you will recieve a warning in the terminal output. To compensate, the program will use all of the posts within the Hacker News API.
