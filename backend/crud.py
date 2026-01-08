from sqlalchemy.orm import Session
import models

def get_board(db: Session):
    lists = db.query(models.List).order_by(models.List.position).all()
    cards = db.query(models.Card).order_by(models.Card.position).all()
    return lists, cards

def create_list(db, title, position):
    lst = models.List(title=title, position=position, board_id=1)
    db.add(lst)
    db.commit()
    return lst

def create_card(db, title, description, list_id, position):
    card = models.Card(
        title=title,
        description=description,
        list_id=list_id,
        position=position,
    )
    db.add(card)
    db.commit()
    return card

def move_card(db, card_id, list_id, position):
    card = db.query(models.Card).get(card_id)
    card.list_id = list_id
    card.position = position
    db.commit()

def update_card(db, card_id, title, description):
    card = db.query(models.Card).get(card_id)
    card.title = title
    card.description = description
    db.commit()

def reorder_lists(db, updates):
    for item in updates:
        lst = db.query(models.List).get(item["id"])
        lst.position = item["position"]
    db.commit()
