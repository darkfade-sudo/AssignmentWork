from django.shortcuts import render,redirect

from .forms import ContactForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect("contact")
    else:
        form= ContactForm()
    return render(request,"assignmentapp/contact.html",{"form":form})    
