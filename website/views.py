from django.shortcuts import render
from website.models import Service, CaseStudy, Doctor, Testimonial

def index(request):
    context = {
        "services": Service.objects.filter(is_active=True),
        "case_studies": CaseStudy.objects.filter(is_active=True),
        "doctors": Doctor.objects.filter(is_active=True),
        "testimonials": Testimonial.objects.filter(is_active=True),
    }
    return render(request, "index.html", context)