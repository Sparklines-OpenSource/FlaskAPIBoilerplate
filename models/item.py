from __future__ import annotations
from configs.database import db
from datetime import datetime

class Item(db.Model):
    __tablename__ = 'TBL_ITEM'
    item_id = db.Column(db.Integer, db.Sequence("item_id_seq",1,1), primary_key=True)
    item_name = db.Column(db.String(1500), nullable=False)
    status = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime(), default=datetime.now)


    @staticmethod
    def create_item(item : Item) -> None:
        db.session.add(item)
        db.session.commit()


    @staticmethod
    def list_all() -> list[Item]:
        q = db.session.query(Item)
        result = q.all()
        return result