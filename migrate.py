from api.api_server import create_app
from configs.database import db


app = create_app()
app.app_context().push()
db.create_all()