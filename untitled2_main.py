#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

from google.appengine.ext import db

class Comment(db.Model):
    content = db.StringProperty(multiline=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<html><h1>Project Parallel</h1>')
        self.query = Comment.all()
        for self.comment in self.query:
            self.response.write('<p>%s</p>' % self.comment.content)
        self.response.write("""Comment Here:
        <form method="post">
        <input type="textarea" name="post"></input>
        <input type="submit"></input></form>
        <form method="post">
        <select name="del">
        """)
        for self.comment in self.query:
            self.response.write('<option>%s</option>' % self.comment.content)
        self.response.write("""<input type="submit"></input>""")
        self.response.write('</body></html>')

    def post(self):
        self.comment = Comment(content=self.request.get('post'))
        self.comment.put()
        self.redirect('/')

    def delete(self):
        if self.comment == Comment(content=self.request.get('del')):
            self.comment.delete()
        self.redirect('/')



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
