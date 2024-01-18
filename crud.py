from sqlalchemy.orm import Session
import models, schemas



def get_todo(db: Session, id: int):
    return db.query(models.Todo).filter(models.Todo.id == id).first()


def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()

def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(text=todo.text)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, id: int, todo: schemas.TodoUpdate):
    db_todo = db.query(models.Todo).filter(models.Todo.id == id).first()
    if db_todo:
        update_data = todo.dict(exclude_unset=True)  # This will create a dictionary with only the attributes that have values in todo
        for key, value in update_data.items():
            setattr(db_todo, key, value)
        db.commit()
        db.refresh(db_todo)
        return db_todo
    return None  # Return None if Todo with given id is not found

def delete_todo(db: Session, id: int):
    db_todo = db.query(models.Todo).filter(models.Todo.id == id).first()
    if db_todo:
        db.query(models.Todo).filter(models.Todo.id == id).delete()
        db.commit()
        return True
    return False  # Return False if Todo with given id is not found