from django.urls import path

from .views import TodoModelViewSet

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
]
