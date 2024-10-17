from rest_framework import viewsets
from .models import Note
from .seriallizers import NoteSerializer

# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer