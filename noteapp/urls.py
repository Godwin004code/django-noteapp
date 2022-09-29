from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addnote/', views.add, name='add'),
    path('addnote/create/', views.create, name='create'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit/update/<int:id>', views.editedNote, name='editedNote'),
    path('edit/delete/<int:id>', views.deleteEditedNote, name='editedNoteDelete'),
]