"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

from app.http.controllers.PostController import PostController

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    
    RouteGroup([
      
      Get("/","PostController@index").name("index"),
      Post("/","PostController@create").name("create"),
      Get("/@id","PostController@show").name("show"),
      Put("/@id","PostController@update").name("update"),
      Delete("/@id","PostController@destroy").name("delete"),
      
      
      
      ],prefix="/posts",name="posts")
]
