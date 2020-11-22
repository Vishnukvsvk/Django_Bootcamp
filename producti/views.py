from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404

from .models import Product
from .forms import ProductForm
# Create your views here.

'''
    title = models.CharField(max_length=25)
    price = models.IntegerField(default=0)
    discount = models.BooleanField(default=True)
'''


def bad_view(request, *args, **kwargs):
    print(dict(request.GET))
    dict1 = dict(request.GET)
    title = dict1.get("title")
    price = dict1.get("price")
    discount = dict1.get("discount")
    Product.objects.create(title=title[0], price=int(
        price[0]), discount=discount[0])
    return HttpResponse("<h1>This is bad</h1>")


def form_view(request, *args, **kwargs):
    if(request.method == "POST"):
        post_data = request.POST or None
        if(post_data != None):
            my_form = ProductForm(request.POST)
            print(my_form.is_valid())
            print("data", post_data)
    return render(request, "forms.html", {})


def Home_View(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello Vishnu</h1>")
    context = {"name": "vishnu Kumar Kvs", "city": "Bangalore"}
    return render(request, "home.html", context)


def Product_View(request, *args, **kwargs):
    obj = Product.objects.get(id=2)
    context = {"object": obj}
    # return HttpResponse(f"Product title: {obj.title}")
    return render(request, "product.html", context)


def Product_Dynamic_View(request, id):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    return JsonResponse({"Title": obj.title})


def product_snippet_view(request, *args, **kwargs):
    qs = Product.objects.all()
    content = {"object_list": qs}
    return render(request, "prody.html", content)
