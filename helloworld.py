import webapp2

form="""
<form>
	<select name="q">
		<option value="1">one</option>
		<option value="2">two</option>
		<option value="3">three</option>
	</select>
	<br>
	<input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

class TestHandler(webapp2.RequestHandler):
	def post(self):
		q = self.request.get("q")
		self.response.write(q)

		# self.response.headers['Content-Type'] = 'text/plain'
		# self.response.write(self.request)
		
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/testform', TestHandler)
], debug=True)