from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse

data = {
    "telefon":"telefon kategorisindeki ürünler",
    "bilgisayar":"bilgisayar kategorisindeki ürünler",
    "elektronik":"elektronik kategorisindeki ürünler"
}


def index(request):
    list_items = ""
    category_list = list(data.keys())

    for category in category_list:
        redirect_path = reverse("products_by_category", args=[category])
        list_items += f"<li><a href=\"{redirect_path}\">{category}</a></li>"

    html = f"<ul>{list_items}</ul>"
    return render(request, 'myapp/index.html')


def getProductsByCategoryId(request, category_id):
    category_list = list(data.keys())
    if category_id > len(category_list):
        return HttpResponseNotFound("yanlış kategori seçimi")
    category_name = category_list[category_id-1]
    #reverse metodu bir bakıma urlyi döndürüyorki tekrardan yazma diye
    redirect_path = reverse("products_by_category", args=[category_name])
    return redirect(redirect_path)

def getProductsByCategory(request, category):
    try:
        category_text = data[category]
        return render(request, 'myapp/products.html', {
            "category": category,
            "category_text": category_text
        })
    except:
        return HttpResponseNotFound(f"<h1>yanlış kategori seçimi</h1>")

