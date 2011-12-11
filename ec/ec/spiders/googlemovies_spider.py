from scrapy.spider import BaseSpider 
from scrapy.selector import HtmlXPathSelector
from ec.items import GoogleMovieItem
from pymongo import Connection

class GoogleMovieSpider(BaseSpider):
	name = "googlemovies.es"
	allowed_domains = ["google.es"]
	start_urls = ["http://www.google.es/movies?hl=es&near=madrid"]

	def parse(self, response):
		connection = Connection('localhost', 27017)
		db = connection.mydb
		movies_mongo = db.movies

		hxs = HtmlXPathSelector(response)
		movies = hxs.select('//div[@class="movie"]/div[@class="name"]/a')

		items = []

		for movie in movies:
			title = movie.select('text()').extract()
			link = movie.select('@href').extract()

			print "Saving ... (title: " + title[0] +  " || link:" + link[0] + ")"
			movies_mongo.insert({"title" : title[0], "link" : link[0]})
