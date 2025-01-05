from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi

from . import appbuilder, db
from .models import Todo

class TodoView(ModelView):
    datamodel = SQLAInterface(Todo)

    list_columns = ["entry", "completed"]
    base_order = ("entry", "asc")
    show_fieldsets = [
        ("Summary", {"fields":["entry", "completed"]}),
    ]
    add_fieldsets = [
        ("Summary", {"fields": ["entry", "completed"]}),
    ]
    edit_fieldsets = [
        ("Summary", {"fields": ["entry", "completed"]}),
    ]


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
appbuilder.add_view(
    TodoView,
    "Todo",
    icon = "fa-folder-open-o",
    category = "Todo",
    category_icon= "fa-envelope"
)
