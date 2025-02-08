from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data' : {
        "name" : "Vishnu"
    }}

@app.get('/about')
def about():
    return {
        "page" : "This is about page",
        "data" : {
            "name" : "Vishnu",
            "email" : "vishnu@gmail.com",
            "phone" : "+91 1234567890"
        }
    }