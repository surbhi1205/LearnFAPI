from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data' : {'name':'Surbhi'}}

@app.get('/about')
def about():
    return {'data': {'class':'tenth'}}