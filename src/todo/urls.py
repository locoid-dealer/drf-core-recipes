from django.urls import path

from .views import TodoGenericViewSet, TodoModelViewSet

urlpatterns = [
    path(
        "todo/",
        TodoModelViewSet.as_view({"get": "list", "post": "create"}),
        name="todo_model_viewset",
    ),
    path(
        "todo/<int:pk>/",
        TodoModelViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="todo_model_viewset_detail",
    ),
    path(
        "todo/generic_viewset/",
        TodoGenericViewSet.as_view({"get": "list", "post": "create"}),
        name="todo_generic_viewset",
    ),
    path(
        "todo/generic_viewset/<int:pk>/",
        TodoGenericViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="todo_generic_viewset_detail",
    ),
]
