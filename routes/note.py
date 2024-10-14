from fastapi import APIRouter , Form , Request
from models.note import Note
from config.ConnectDb import ConnectDb , db_collection
from schemas.note import  NoteEntity, NotesEntity
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse 
from pydantic import BaseModel

from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

# initialize dotenv 
load_dotenv()

ConnectDb()
note = APIRouter()


templates = Jinja2Templates(directory="templates")


@note.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={  "request":request , "id": id}
    )




# POST route to handle form submission
@note.post("/create-note", response_class=HTMLResponse)
async def create_item(request: Request, title: str = Form(...), description: str = Form(...), isImportant: bool = Form(False)):
    new_note:Note = {
        "title": title,
        "description": description,
        "isImportant": isImportant
    }
    
    try:
        result = db_collection.insert_one(new_note)
        print(f"New note created with id: {result.inserted_id}")
        # Render the response template with a success message
        return templates.TemplateResponse("success.html", {"request": request, "note_id": str(result.inserted_id)})
    except Exception as e:
        print(f"Failed to insert note into MongoDB: {e}")
        # Handle error appropriately, perhaps render an error template
        return templates.TemplateResponse("error.html", {"request": request, "error": str(e)})

# GET route to render the form
@note.get("/create-note", response_class=HTMLResponse)
async def create_note(request: Request):
    return templates.TemplateResponse("createNotes.html", {"request": request})