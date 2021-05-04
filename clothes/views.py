from django.shortcuts import render, get_object_or_404
from .models import Category, Outfit, Testimonial
from .forms import SearchForm, ContactForm


def home(request):
    category = Category.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, 'main.html', {'category': category, 'testimonials': testimonials})


def products(request):
    category = Category.objects.all()
    outfits = Outfit.objects.all()
    return render(request, 'products.html', {'categories': category, 'outfits': outfits})


def search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Outfit.objects.filter(name__startswith=query)
    return render(request, 'search.html', {'form': form, 'query': query, 'results': results})


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'contact-us.html', {'form': form})


def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    outfits = Outfit.objects.filter(category=category)
    print(outfits)
    return render(request, 'category_detail.html', {'category': category, 'outfits': outfits})


def outfit_detail(request, id):
    outfit = get_object_or_404(Outfit, id=id)
    return render(request, 'outfit_detail.html', {'outfit': outfit})