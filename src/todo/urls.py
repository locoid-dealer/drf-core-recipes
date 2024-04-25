from django.urls import path

from .views import (
    TodoCreateAPIView,
    TodoDestroyAPIView,
    TodoGenericViewSet,
    TodoListAPIView,
    TodoModelViewSet,
    TodoRetrieveAPIView,
    TodoUpdateAPIView,
    TodoViewSet,
)

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
    path(
        "todo/viewset/",
        TodoViewSet.as_view({"get": "list", "post": "create"}),
        name="todo_viewset",
    ),
    path(
        "todo/viewset/<int:pk>/",
        TodoViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="todo_viewset_detail",
    ),
    path(
        "todo/list_api_view/",
        TodoListAPIView.as_view(),
        name="todo_list_api_view",
    ),
    path(
        "todo/create_api_view/",
        TodoCreateAPIView.as_view(),
        name="todo_create_api_view",
    ),
    path(
        "todo/retrieve_api_view/<int:pk>/",
        TodoRetrieveAPIView.as_view(),
        name="todo_retrieve_api_view",
    ),
    path(
        "todo/update_api_view/<int:pk>/",
        TodoUpdateAPIView.as_view(),
        name="todo_update_api_view",
    ),
    path(
        "todo/destroy_api_view/<int:pk>/",
        TodoDestroyAPIView.as_view(),
        name="todo_destroy_api_view",
    ),
]
