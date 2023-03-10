from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse, StreamingResponse
from app.sample import Sample

app = FastAPI()
# allow communication from all frontends
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get('/', response_class=PlainTextResponse)
def root():
    return 'Welcome to the root api \n Go to /questions/ endpoint '

@app.get('/questions/', response_class=PlainTextResponse)
def questions(course:str):
    return StreamingResponse(content=Sample(course), media_type='text/html')
