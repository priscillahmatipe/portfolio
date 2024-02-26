from django.shortcuts import render
from .models import ContactMessage

# Create your views here.

def main(request):
    return render(request, 'index.html')

def contact_view(request):
    if request.method=='POST':
        Name=request.POST['name']
        Gmail=request.POST['gmail']
        Subject=request.POST['subject']
        
        
        ContactMessage.objects.create(Name=Name,Gmail=Gmail,Subject=Subject)
        return redirect('contact')
    
    return render(request,'contact.html')