from django.shortcuts import render
from .models import Tag, ProductTag
from store.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


@login_required
def index(request):
    tags = Tag.objects.all()
    context = {"tags": tags}
    return render(request, "index.html", context)


@login_required
def store(request):
    if request.method == "POST":
        name = request.POST.get("name")
        tag = Tag.objects.get_or_create(name=name)
        product = Product.objects.filter(user=request.user).latest('id')
        if not product:
            return messages.error(request, "Not found product.")
        product_tag = ProductTag(product=product, tag=tag)
        product_tag.save()
        return tag
    else:
        return "Invalid request method"
