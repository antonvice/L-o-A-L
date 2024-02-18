from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from loawl import Loawl
from pathlib import Path
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Mount static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    # Assuming you have some form of Todo list to pass to the template
    todo_list = ["Langchain independence", "WebUI", "Formats", "Local models", "JSON Parsing"]
    return templates.TemplateResponse("index.html", {"request": request, "todo_list": todo_list})


@app.post("/upload")
async def upload_document(request: Request, document: UploadFile = File(...)):
    # Save uploaded file
    '''file_location = Path("uploaded_documents") / document.filename
    with open(file_location, "wb+") as file_object:
        file_object.write(document.file.read())'''
    # Process the document and return response
    return templates.TemplateResponse("main.html", {"request": request, "filename": document.filename})

@app.get("/main", response_class=HTMLResponse)
def generate(request: Request):
    # This is a placeholder. Adjust as necessary for your use case.
    loawl = Loawl()
    document = request.query_params.get("document")
    if document:
        loawl.document = document
        loawl.update_document_abstractions()
        return templates.TemplateResponse("generate.html", {"request": request, "abstractions": loawl.get_abstractions()})
    else:
        return templates.TemplateResponse("error.html", {"request": request, "message": "No document provided"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=12345)