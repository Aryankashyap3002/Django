from . import views

urlpatterns = [
    path('', view.posts_list),
]