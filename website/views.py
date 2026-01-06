from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from website.models import *

def index(request):

    if request.method == "POST":
        response = handle_form(request)
        if response:
            messages.success(request, "Your message has been sent successfully!")
            return redirect('/')
        else:
            messages.error(request, "There was an error sending your message. Not you its us!.")
            return redirect('/')


    context = {
        "services": Service.objects.filter(is_active=True),
        "case_studies": CaseStudy.objects.filter(is_active=True),
        "doctors": Doctor.objects.filter(is_active=True),
        "testimonials": Testimonial.objects.filter(is_active=True),
        "clients" : ClientHospitals.objects.filter(is_active=True),
    }
    return render(request, "index.html", context)



from .utils import send_discount_html_email
from django.utils import timezone

def handle_form(request):
    if request.method == "POST":
        ContactRequest.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
            message=request.POST.get("message")
        )
        context = {
            "patient_name": request.POST.get("first_name"),
            "patient_email": request.POST.get("email"),
            "patient_phone": request.POST.get("phone"),
            "discount_range": "20–30%",
            "reference_id": "REF" + timezone.now().strftime("%Y%m%d%H%M%S"),
            "request_date": timezone.now().strftime("%d %b %Y, %I:%M %p"),
            "hospital_name": "Health Secure Plus",
            "hospital_phone": "",
            "support_email": "healthsecurepluss@gmail.com",
            "terms_url": "https://healthsecureplus.com/",
            "call_to_action_url": "https://healthsecureplus.com/",
            "hospital_address": "Your City, India",
        }
        try:
            send_discount_html_email(context["patient_email"], context)
        except Exception as e:
            print(f"Error sending email: {e}")
            return None

        return True