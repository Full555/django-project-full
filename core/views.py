

from django.shortcuts import render, get_object_or_404, redirect

from django.views import View

from .filters import MasterFilter, PhotoFilter, FeedbackFilter

from .models import Master, Photo, Feedback, Services, ServiceType

from .forms import BookingForm



def index_pag(request):
    return render(request, "base.html")




class MastersView(View):
    def get(self, request):
        masters = Master.objects.all()
        photos = Photo.objects.all()
        feedbacks = Feedback.objects.all()

        filterset = MasterFilter(request.GET, queryset=masters)
        filtersett = PhotoFilter(request.GET, queryset=photos)
        filtersettt = FeedbackFilter(request.GET, queryset=feedbacks)

        return render(request, 'index.html', {
            'photos': filtersett.qs,
            'masters': filterset.qs,
            'feedbacks': filtersettt.qs,
            'types': ServiceType.objects.all(),
            'active_type': request.GET.get('typename'),



            'lashes_id': ServiceType.objects.get(name='Наращивание ресниц').id,
            'nails_id': ServiceType.objects.get(name='Ногтевой сервис').id,
            'brows_id': ServiceType.objects.get(name='Брови').id,
        })


class AboutViews(View):
    def get(self, request):
        masters = Master.objects.all()
        filterset = MasterFilter(request.GET, queryset=masters)
        return render(request, 'about.html', {
            'masters': filterset.qs,
            'types': ServiceType.objects.all(),
            'active_type': request.GET.get('typename'),
        })



class ServicesView(View):
    def get(self, request):
        service_types = ServiceType.objects.prefetch_related('services')
        form = BookingForm()
        return render(request, 'service.html', {
            'service_types': service_types,
            'form': form
        })

    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)

        service_types = ServiceType.objects.prefetch_related('services')
        return render(request, 'service.html', {
            'service_types': service_types,
            'form': form
        })



class MastersHomeView(View):
    def get(self, request):
        masters = Master.objects.all()
        photos = Photo.objects.all()
        filterset = MasterFilter(request.GET, queryset=masters)
        filtersett = PhotoFilter(request.GET, queryset=photos)

        return render(request, 'master.html', {
            'photos': filtersett.qs,
            'masters': filterset.qs,
            'types': ServiceType.objects.all(),
            'type': ServiceType.objects.all(),
            'active_type': request.GET.get('typename'),

        })




class MasterDetailViews(View):
    def get(self, request, id):
        master = get_object_or_404(Master, id=id)
        photos = Photo.objects.filter(master=master)
        form = BookingForm()

        return render(request, 'masterdeatil.html', {
            'master': master,
            'photos': photos,
            'feedbacks': Feedback.objects.all(),
            'form': form,
        })

    def post(self, request, id):
        master = get_object_or_404(Master, id=id)
        photos = Photo.objects.filter(master=master)
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(request.path)


        return render(request, 'masterdeatil.html', {
            'master': master,
            'photos': photos,
            'feedbacks': Feedback.objects.all(),
            'form': form,
        })



class ServicesByTypeView(View):
    def get(self, request, type_id):
        service_type = get_object_or_404(ServiceType, id=type_id)
        services = Services.objects.filter(typename=service_type)
        form = BookingForm()

        return render(request, 'services_by_type.html', {
            'service_type': service_type,
            'services': services,
            'form': form,
        })

    def post(self, request, type_id):
        service_type = get_object_or_404(ServiceType, id=type_id)
        services = Services.objects.filter(typename=service_type)
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(request.path)

        return render(request, 'services_by_type.html', {
            'service_type': service_type,
            'services': services,
            'form': form,
        })

