from django.shortcuts import get_object_or_404, render
from main.models import *

def detail(request):
    partner = get_object_or_404(Partner, pk=1)
    hr = get_object_or_404(HumanResource, partner=partner)
    #review = get_object_or_404(Review, partner=partner)
    jobs = Job.objects.filter(hr=hr)
    return render(request, 'detail.html', {"partner": partner, "hr": hr, "jobs": jobs})#"review": review