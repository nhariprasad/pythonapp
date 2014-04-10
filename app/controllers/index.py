import jinja2
import os
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('app/templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class IndexPage(webapp2.RequestHandler):
	def get(self):
		template_values = {}
		template = JINJA_ENVIRONMENT.get_template('index.html')
		self.response.write(template.render(template_values))