import requests

def is_limit_to_valid(url, limit_to, max_posts):
	"""Raises warning if the limit user sets is greater than the max number of posts in HN API."""
	r = requests.get(url)
	max_posts = len(r.json())
	if limit_to > max_posts:
		raise Warning

def check_limit_to(url, limit_to):
	"""Checks if user-set limit for posts is less than maxmium number of posts in HN API."""
	r = requests.get(url)
	max_posts = len(r.json())
	print("Checking if 'limit_to' is valid...")
	try:
		is_limit_to_valid(url, limit_to, max_posts)
	except Warning:
		print(f"Warning: 'limit_to' ({limit_to}) is set to an invalid value. Setting 'limit_to' to {max_posts}...")
		return max_posts	
	else:
		print("'limit_to' is valid! Proceeding as normal...")
		return limit_to	
