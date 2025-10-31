from tags.views import store
from .models import Tag
from .views import store
def createTag(request):
    return store(request)
