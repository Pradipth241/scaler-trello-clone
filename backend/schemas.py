from pydantic import BaseModel
from typing import List

# ---------- LIST CREATE ----------

class ListCreate(BaseModel):
    title: str
    position: int


# ---------- CARD CREATE ----------

class CardCreate(BaseModel):
    title: str
    description: str
    list_id: int
    position: int


# ---------- CARD MOVE (DnD) ----------

class CardMove(BaseModel):
    list_id: int
    position: int


# ---------- LIST REORDER (DnD) ----------

class ListReorderItem(BaseModel):
    id: int
    position: int


class ListReorderRequest(BaseModel):
    updates: List[ListReorderItem]


# ---------- CARD EDIT ----------

class CardEditRequest(BaseModel):
    title: str
    description: str
