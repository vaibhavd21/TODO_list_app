from todo_list_app.views import home
from django.urls import path
from .views import home,login, signup,LogOut,AddTodo,delete_todo,ChangeStatus,updateTask


urlpatterns = [
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('logout/',LogOut,name = 'logout'),
    path('add-todo/',AddTodo,name='add-todo'),
    path('delete-todo/<int:id_of_todo>' , delete_todo, name='delete_todo'),
    path('StatusChange-todo/<int:id_of_todo>/<str:update_status_mark>',ChangeStatus,name='ChangeStatus'),
    path('update_task/<int:id_of_todo>/',updateTask,name='update_task')
]
