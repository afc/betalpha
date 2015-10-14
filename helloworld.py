import jinja2
import webapp2

import os


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
  def get(self):
    # self.response.headers['Content-Type'] = 'text/plain'
    # self.response.write('Hello, World!')
    # self.response.out.write()
    template = jinja_environment.get_template('googlec96559fede4f36fc.html')
    self.response.write(template.render(content="Let's Bet Alpha!"))


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
