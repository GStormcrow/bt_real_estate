from django.shortcuts import render
from .models import Listing, Realtor
from django.core.paginator import Paginator
from listings.choices import price_choices, state_choices, bedroom_choices
def index(request):
    listings = Listing.objects.all()
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings':paged_listings
    }
    return render(request, 'listings/listings.html', context)
def listing(request, listing_id):
    listing = Listing.objects.get(id = listing_id)
    # realtor = Realtor.objects.get(name = listing.realtor)
    return render(request,'listings/listing.html', {'listing':listing})
def search(request):
    # listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    queryset_listings = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_listings = queryset_listings.filter(description__icontains = keywords)
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_listings = queryset_listings.filter(state__iexact = state)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_listings = queryset_listings.filter(city__iexact = city)
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_listings = queryset_listings.filter(bedrooms__lte = bedrooms)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_listings = queryset_listings.filter(price__lte = price)
    context = {
        'listings':queryset_listings,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'values':request.GET,
    }
    return render(request,'listings/search.html',context)
# Create your views here.