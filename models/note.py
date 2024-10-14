from pydantic import BaseModel 


class Note(BaseModel):
    title: str          # Correct spelling
    description: str    # Correct spelling
    isImportant: bool
