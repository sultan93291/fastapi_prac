from pydantic import BaseModel 

class note(BaseModel):
  tittle:str
  descreption:str
  isImportant:bool