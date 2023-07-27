from django.shortcuts import render
from . import models

# Create your views here.
def ShowRoom(request):
    showrooms = models.ShowRoom.objects.all()
    brands = models.Brand.objects.all()
    return render(request, 'showroom/showroom.html', {'showrooms': showrooms, 'brands': brands} )

def BrandDetail(request, brand_id):
    showrooms = models.ShowRoom.objects.all()
    brands = models.Brand.objects.all()
    brand = models.Brand.objects.get(id=brand_id)
    all_models = models.Model.objects.filter(brand=brand)
    return render(request, 'showroom/brand_detail.html', {'showrooms': showrooms, 'brands': brands, 'brand': brand, 'models': all_models})

def Staff(request):
    showrooms = models.ShowRoom.objects.all()
    staff = models.Staff.objects.all()
    brands = models.Brand.objects.all()
    return render(request, 'showroom/staff.html', {'showrooms': showrooms, 'brands': brands, 'staff': staff})

def StaffDetail(request, staff_id):
    showrooms = models.ShowRoom.objects.all()
    member = models.Staff.objects.get(id=staff_id)
    brands = models.Brand.objects.all()
    return render(request, 'showroom/staff_detail.html', {'showrooms': showrooms, 'brands': brands, 'member': member})

def ModelDetail(request, brand_id, model_id):
    brands = models.Brand.objects.all()
    brand = models.Brand.objects.get(id=brand_id)
    model = models.Model.objects.get(id=model_id)
    return render(request, 'showroom/model_detail.html', {'brands': brands, 'brand':brand, 'model': model})