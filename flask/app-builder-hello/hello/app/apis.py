from app.models import Book
from flask_appbuilder.api import ModelRestApi
from flask_appbuilder.models.sqla.interface import SQLAInterface
from . import appbuilder

class BookModelApi(ModelRestApi):
    resource_name = "book"
    datamodel = SQLAInterface(Book)

appbuilder.add_api(BookModelApi)