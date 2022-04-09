# Import plotting modules
from plotly.graph_objs import Bar
from plotly import offline

# Import modules we'll use to retrieve and operate with data from HN API.
import requests
import json
from operator import itemgetter

from .post import Post
from .checks import check_limit_to

class PopularAsksVisual():
	"""Class used to plot most-voted ask-type posts on Hacker News"""

	def __init__(self, url='https://hacker-news.firebaseio.com/v0/askstories.json?orderBy="$priority"', limit_to=20):
		"""Initialise attributes used for HN API call and data analysis"""
		# Limit number of posts to be retrieved to a default amount of 30
		self.url = url
		self.limit_to = limit_to
		# Check if limit doesn't surpass total number of AskHN ID's in the HN 
		# API, if so then we set 'limit_to' to total number of AskHN ID's
		self.limit_to = check_limit_to(self.url, self.limit_to)
		self.payload = {'limitToFirst': self.limit_to}
		self.r = requests.get(url, params=self.payload)

		self.submission_ids = self.r.json()
		self.sub_dicts = []
		self.submission_contents = {}
		self.links, self.scores, self.hovertexts = [], [], []

	def generate_axis_values(self):
		"""Sorts list of dictionaries for each post by their number of votes
		in ascending order, then extracts top 30 submissions and stores vals
		we use for x and y axis in their respective lists"""
		self.sub_dicts = sorted(self.sub_dicts, key=itemgetter('sub_score'), reverse=True)
		for sub_dict in self.sub_dicts[:self.limit_to]:
			self.links.append(sub_dict['sub_link'])
			self.scores.append(sub_dict['sub_score'])
			self.hovertexts.append(sub_dict['sub_hovertext'])

	def analyse_data(self):
		"""Retrieves and analyses data within each post, and stores data we want 
		for further processing"""
		for id in self.submission_ids:
			current_post = Post(id)
			sub_url = f'https://hacker-news.firebaseio.com/v0/item/{id}.json'
			current_post.get_content(url=sub_url)
			sub_link = current_post.gen_hyperlink(title=current_post.submission_contents['by'])
			sub_hovertext = current_post.submission_contents['title']
			sub_dict = current_post.gen_dict(sub_link, current_post.submission_contents['score'], sub_hovertext)
			self.sub_dicts.append(sub_dict)

	def plot_data(self):
		"""Generates x and y values, and plots the data using plotly module"""
		print("---Plotting data---")
		self.generate_axis_values()
		title = f'Top {self.limit_to} recent Ask HN stories'
		data = [{
			'type': 'bar',
			'x': self.links,
			'y': self.scores,
			'hovertext': self.hovertexts,
			'marker': {
				'color': 'rgb(60, 100, 150)',
				'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
			},
			'opacity': 0.6,
		}]
		layout = {
			'title': title,
			'titlefont': {'size': 28},
			'xaxis': {
				'title': 'Name of authors',
				'titlefont': {'size': 24},
				'titlefont': {'size': 24},
				'tickfont': {'size': 14},
				},
			'yaxis': {
				'title': 'Number of Votes',
				'titlefont': {'size': 24},
				'tickfont': {'size': 14},
				},
		}

		fig = {'data': data, 'layout': layout}
		offline.plot(fig, filename='plots/popular_asks_visual.html')


