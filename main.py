from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# Get method - The operation on top of the path
# -- The function on top of the get operator -> "path operation function" 
# -- -- Decorator is called as -> path operator decorator
@app.get('/blog') # This is the base path
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None): # Instead of hardcoding, directly take the limit if passed
    if published:
        print(published)
        return {
            "data": f"Here are the {limit} published blogs from the db" # Take the limit from the query by ?limit=10
        }
    else:
        return {
            "data": f"Here are the {limit} blogs from the db" # Take the limit from the query by ?limit=10
        }

# Static routing always above the dynamic routing 
@app.get('/blog/unpublished') # This causes a integer type error -> as fast api goes line by line here -> move this above dynamic routing 
def unpublished():
    return {
        "data" : "All unpublished blogs"
    }

# Create a blog and dynamic with the id in the path 
@app.get('/blog/{id}') # If id = 1 get the blod with id 1, so on so forth -> with {}
def show(id: int): # Define the input id type -> only takes the input of this type
    # Fetch the blog with the corresponding id 
    return {
        "data": id
    }

@app.get('/blog/{id}/comments') # Same funda as that of the blog with id 
def comments(id: int, limit:int = 10):
    return {
        "data": {
            "1", "2"
        }
    }


class Blog(BaseModel): # This is the model -> blog model -> values from the user with API
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog): # Request input is of the type blog 
    return {
        "blog" : f"The blog is created with {request.title}"
    }

# @app.get('/blog/unpublished') # This causes a integer type error -> as fast api goes line by line here -> move this above dynamic routing 
