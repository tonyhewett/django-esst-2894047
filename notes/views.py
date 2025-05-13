from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, ListView, DetailView

from .models import Notes
from .forms import NotesForm

# Create your views here.

class NotesCreateView(CreateView):
    model = Notes
    # fields = ['title', 'content']
    # template_name = 'notes/notes_create.html'
    success_url = '/smart/notes'  # Redirect to the notes list after creation
    form_class = NotesForm  # Use the form class for validation and rendering


'''
    def form_valid(self, form):
        # You can add custom logic here if needed
        return super().form_valid(form)
'''

class PopularNotesListView(ListView):
    model = Notes
    context_object_name = "notes_list"
    template_name = "notes/notes_list.html"
    queryset = Notes.objects.filter(count_likes__gte=1)  # Filter for popular notes

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes_list"
    template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_detail.html"


    # queryset = Notes.objects.all()  # Optional, can be set in the model
'''
def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes_list': all_notes})
'''
'''
def detail(request, id):
    try:
        my_note = Notes.objects.get(id=id)
    except Notes.DoesNotExist:
        return render(request, 'notes/notes_404.html',{"note_id": id}, status=404) 
        # raise Http404('Note not found for that id')    
    return render(request, 'notes/notes_detail.html', {'note': my_note})
'''
'''    
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        note = Notes(title=title, content=content)
        note.save()
        return render(request, 'notes/detail.html', {'note': note})
    return render(request, 'notes/create.html')
def update(request, id):     
'''    