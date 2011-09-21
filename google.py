from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.ext.webapp.util import run_wsgi_app
import wsgiref.handlers
import urllib2
import urllib
import os
from xml.dom import minidom

#This page has been corrupted because of the corruption of tabs and spaces but fixed agaain

#models

class Story(db.Model):
	title = db.StringProperty()
	body = db.TextProperty()
	created = db.DateTimeProperty(auto_now_add=True)
      
class FormSpecial(db.Model):
	text = db.StringProperty()
	time = db.DateTimeProperty(auto_now_add=True)



class TesterPage(webapp.RequestHandler):
	pass




class MainPage(webapp.RequestHandler):
    def get(self,*args):	
		self.response.out.write(template.render('Templates/page-main.html',''))		

		
class ContactPage(webapp.RequestHandler):
    def get(self,*args):
		self.response.out.write(template.render('Templates/page-contact.html',''))
    def post(self, *args):
		self.redirect('/contact')
			
class AboutPage(webapp.RequestHandler):
    def get(self,*args):
		self.response.out.write(template.render('Templates/page-about.html',''))
			
class PortfolioPage(webapp.RequestHandler):
    def get(self,*args):
		self.response.out.write(template.render('Templates/page-portfolio.html',''))
		
class ServicesPage(webapp.RequestHandler):
    def get(self,*args):
		self.response.out.write(template.render('Templates/page-services.html',''))	
				
    def post(self, *args):	
			form = FormSpecial(text = self.request.get('test'))
			form.put()
			self.redirect('/')	


class CronTask(webapp.RequestHandler):
	def get(self,*args):
		form = FormSpecial(text='hello')		
		form.put()
			
			

	


# Display product with given ID in the given category.

application = webapp.WSGIApplication([(r'/', MainPage),(r'/contact', ContactPage),(r'/about-us', AboutPage),(r'/portfolio', PortfolioPage),(r'/services', ServicesPage),(r'/tasks/summary',CronTask)],debug=True)

#if you want to cache then use main
def mainsA():
	run_wsgi_app(application)

if __name__ == "__main__":
	mainsA()
