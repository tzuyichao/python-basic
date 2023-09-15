from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, expose, BaseView, has_access

from . import appbuilder, db

from app.models import Book

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""

class MyView(BaseView):
    route_base = "/index"

    @expose("/hello")
    def hello(self):
        return "hello world"
    
    @expose("/message/<string:msg>")
    @has_access
    def message(self, msg):
        return f"hello {msg}"
    
    @expose("/welcome/<string:msg>")
    def welcome(self, msg):
        return self.render_template("index.html", msg=f"Hello {msg}")


class BookModelView(ModelView):
    datamodel = SQLAInterface(Book)

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()

appbuilder.add_view_no_menu(MyView())
appbuilder.add_view(BookModelView, "List Books", icon="fa-folder-open-o", category="Books", category_icon='fa-envelope')