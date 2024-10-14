def NoteEntity(item)-> dict:
  return{
    "id":str(item["_id"]),
    "title": item["title"],
    "description": item["description"],
    "isImportant": item["isImportant"]
  }

def NotesEntity(items)-> list:
  return [NoteEntity() for item in items]