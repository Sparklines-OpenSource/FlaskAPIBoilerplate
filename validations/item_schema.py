from configs.validator import validator
from marshmallow import fields, validate, EXCLUDE


class ItemSchema(validator.Schema):
    item_name = fields.Str(required=True, validate=[lambda x: x!="" and len(x.strip())!=0], error_messages={"validator_failed": "Field may not be empty."})
    status = fields.Bool(required=True, description="item status")

    class Meta:
        unknown = EXCLUDE
        fields = ('item_id','item_name','status','created_at')


item_create_schema = ItemSchema(only=('item_name','status'))
items_list_schema = ItemSchema(many=True)
item_schema = ItemSchema()