from django.shortcuts import render


def home_view(request):
    title  = "home"
    return render(request, 'index.html',{"title":title})


def about_view(request):
    title ="about"
    return render(request, 'about.html',{"title":title})


def services_view(request):
    title = "services"
    return render(request, 'services.html',{"title":title})


def blog_view(request):
    title = "blog"
    return render(request, 'blog.html',{"title":title})


def contact_view(request):
    title = "contact"
    return render(request, 'contact.html',{"title":title})


def shop_view(request):
    title ="shop"
    return render(request, 'shop.html',{"title":title})

def cart_view(request):
    title ="cart"
    return render(request, 'cart.html',{"title":title})

def checkout_view(request):
    title = "checkout"
    return render(request, 'checkout.html',{"title":title})

def thankyou_view(request):
    title = "thankcyou"
    return render(request, 'thankyou.html',{"title":title})