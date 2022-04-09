import requests

class Post():
	"""Class representing attributes and methods you would carry out when 
	working with a Hacker News Post"""

	def __init__(self, id):
		"""Get the ID of the post so we can start working with it"""
		self.id = id 

	def gen_hyperlink(self, title):
		"""Returns a neatly formatted hyperlink for the title of a post"""
		return f"<a href='https://news.ycombinator.com/item?id={self.id}'>{title}</a>"

	def get_content(self, url):
		"""Gets dictionary with information for a certain post"""
		sub_r = requests.get(url)
		self.submission_contents = sub_r.json()
		print(f"Status of post {self.id}: {sub_r.status_code}")

	def gen_dict(self, sub_link, score, hovertext):
		"""Generates a dictionary for a single post only with information we want"""
		return {'sub_score': score, 'sub_link': sub_link, 'sub_hovertext': hovertext}
