from selenium import webdriver
import unittest
import sys
if sys.version_info >= (2,7):
	# unittest2 features are native in Python 2.7
	import unittest
else:
	import unittest2 as unittest

class OpenGoogleSearch(unittest.TestCase):
	google_url = "http://www.google.com"
	search_query = ["android", "apple", "microsoft", "google"] # going to use this later
	google_search_textbox = "q"

	def test_open_google_do_search(self):
		""" Opens Google using Firefox and does a search 
			for "Android". Then closes the browser """
		
		ff = webdriver.Firefox()
		ff.get(self.google_url)
		ff.find_element_by_name(self.google_search_textbox).send_keys("android")
		ff.find_element_by_name(self.google_search_textbox).send_keys("\n") # google instant
		ff.close()