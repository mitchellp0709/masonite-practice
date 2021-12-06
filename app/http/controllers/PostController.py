""" A PostController Module """

from masonite.controllers import Controller
from masonite.request  import Request
from app.Post import Post


class PostController(Controller):
    """Class Docstring Description
    """
    def __init__(self,request:Request):
      self.request = request
      
      
    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", PostController)
        """
        id= self.request.param("id")
        return Post.where("id",id).get()

        

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", PostController)
        """
        return Post.all()

        

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", PostController)
        """
        title = self.request.input("title")
        body = self.request.input("body")
        body = Post.create({"title":title,"body":body})
        return body
        

        

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", PostController)
        """
        id=self.request.param("id")
        title = self.request.input("title")
        body = self.request.input("body")
        Post.where("id",id).update({"title":title,"body":body})
        return Post.where("id",id).get()

        

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", PostController)
        """
        id=self.request.param("id")
        title=self.request.input("title")
        body = self.request.input("body")
        post = Post.where("id",id).get()
        Post.where("id",id).delete()
        return post
        