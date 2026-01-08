from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
import crud, models

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def seed():
    db = SessionLocal()
    if db.query(models.Board).count() == 0:
        board = models.Board(title="My Trello board")
        db.add(board)
        db.commit()
        db.add_all([
            models.List(title="This Week", position=0, board_id=board.id),
            models.List(title="Today", position=1, board_id=board.id),
            models.List(title="Later", position=2, board_id=board.id),
        ])
        db.commit()
    db.close()

@app.get("/board")
def board(db: Session = Depends(get_db)):
    return dict(zip(["lists","cards"], crud.get_board(db)))

@app.post("/lists")
def add_list(title: str, position: int, db: Session = Depends(get_db)):
    return crud.create_list(db, title, position)

@app.post("/cards")
def add_card(title: str, description: str, list_id: int, position: int, db: Session = Depends(get_db)):
    return crud.create_card(db, title, description, list_id, position)

@app.put("/cards/{card_id}")
def move(card_id: int, list_id: int, position: int, db: Session = Depends(get_db)):
    crud.move_card(db, card_id, list_id, position)

@app.put("/cards/{card_id}/edit")
def edit(card_id: int, title: str, description: str, db: Session = Depends(get_db)):
    crud.update_card(db, card_id, title, description)


from schemas import ListReorderRequest

@app.put("/lists/reorder")
def reorder_lists(
    payload: ListReorderRequest,
    db: Session = Depends(get_db)
):
    for item in payload.updates:
        lst = db.query(models.List).get(item.id)
        lst.position = item.position
    db.commit()
    return {"status": "ok"}

