import webapp2

from google.appengine.ext import db

class Post(db.Model):
    content = db.StringProperty(multiline=True)
    comment = db.StringProperty(multiline=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.query = Post.all()
        self.response.write("""<html><h1>Parallel Project</h1><body>
        Post Here : <form method="post">
        <input type="textarea" name="post"></input>
        <input type="submit"></input></form>
        Search & View Post Here : <form method="post>
        <select name="pos">""")
        for self.comment in self.query:
            self.response.write('<option>%s</option>' % self.comment.content)
        self.response.write("""</select><input type="textarea" name="comm"></input>
        <input type="submit"></input></form>
        <form method="post">
        Search & View Comment Here : <select name="vw">""")
        for self.comment in self.query:
            self.response.write('<option>%s</option>' % self.comment.content)
        self.response.write("""</select><input type="submit">
        </input></form>""")

        self.response.write("""Delete Post Here : < select name = "del" >""")
        for self.comment in self.query:
            self.response.write('<option>%s</option>' % self.comment.content)
        self.response.write(""" </select>< input type = "submit"> </input>""")
        self.response.write('</body></html>')

    def post(self):
        self.comment = Post(content=self.request.get('post'))
        self.comment.put()
        self.redirect('/')

    def view(self):
        if self.comment == Post(content=self.request.get('pos')):
            self.comment = Post(comment=self.request.get('comm'))
        self.comment.put()
        self.redirect('/')

    def viewcom(self):
        if self.comment == Post(content=self.request.get('vw')):
            for self.comment in self.query:
                self.response.write('<p1>%s</p1><br/>' % self.comment.comment)
        self.response.write('<a href="/">Click Here To Return</a>')

    def delete(self):
        if self.comment == Post(content=self.request.get('del')):
            self.comment = Post(content=self.request.get('del'))
        self.comment.delete()
        self.redirect('/')


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)