from flask import Blueprint, jsonify, request
from validations.item_schema import item_create_schema, items_list_schema, item_schema
from models.item import Item
from apifairy import response, other_responses, body


item_bp = Blueprint('item',__name__)


@item_bp.route('/create',methods=['POST'])
@body(item_create_schema)
@response(item_schema,200)
@other_responses({
    400 : (item_schema,'Validation Error')
})
def create_item():
    """Register a new item
    Clients can use this endpoint when they need to register a new item
    in the system.
    """
    body = request.get_json()
    errors = item_create_schema.validate(body)
    if len(errors) != 0:
        return jsonify(errors), 400
    else:
        item = Item(**body)
        Item.create_item(item)
        return item_schema.dump(item), 200
    
@item_bp.route('/get',methods=['GET'])
def list_items():
    items = Item.list_all()
    return items_list_schema.dump(items), 200