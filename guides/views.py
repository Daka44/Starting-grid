from django.shortcuts import render, get_object_or_404
from .models import Guide
# Create your views here.

def guide_list(request):
    guides = Guide.objects.all()
    return render(request, 'guides/guide_list.html', {'guides': guides})

def guide_detail(request, pk):
    guide = get_object_or_404(Guide, pk=pk)
    return render(request, 'guides/guide_detail.html', {'guide': guide})