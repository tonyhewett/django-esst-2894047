from django.shortcuts import render
from django.http import Http404


from .models import Notes
# Create your views here.

def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes_list': all_notes})

def detail(request, id):
    try:
        my_note = Notes.objects.get(id=id)
    except Notes.DoesNotExist:
        return render(request, 'notes/notes_404.html',{"note_id": id}, status=404) 
        # raise Http404('Note not found for that id')    
    return render(request, 'notes/notes_detail.html', {'note': my_note})

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