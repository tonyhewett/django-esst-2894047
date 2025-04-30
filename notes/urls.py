from django.urls import path
from . import views
#     note = Notes.objects.get(id=id)
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         note.title = title
#         note.content = content
#         note.save()
#         return render(request, 'notes/detail.html', {'note': note})
#     return render(request, 'notes/update.html', {'note': note})
# def delete(request, id):
#     note = Notes.objects.get(id=id)
#     if request.method == 'POST':
#         note.delete()
#         return render(request, 'notes/list.html')
#     return render(request, 'notes/delete.html', {'note': note})
urlpatterns = [
    path('notes', views.NotesListView.as_view(), name='notes.list'),
    path('notes-popular', views.PopularNotesListView.as_view()),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name='notes.detail'),

#     path('detail/<int:id>/', views.detail, name='detail'),
#     path('create/', views.create, name='create'),
#     path('update/<int:id>/', views.update, name='update'),
#     path('delete/<int:id>/', views.delete, name='delete'),    
 ]
