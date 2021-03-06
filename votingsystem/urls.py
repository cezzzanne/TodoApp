
from django.urls import path
from .views import login_home, edit_profile, edit_password, logout_view, add_todo, add_folder, delete_todo


urlpatterns = [
    path('home', login_home),
    path('edit', edit_profile),
    path('edit-password', edit_password),
    path('logout/', logout_view),
    path('add-todo/<folder>', add_todo, name='folder'),
    path('add-folder', add_folder),
    path('add-todo/delete/<todo>', delete_todo),
]
