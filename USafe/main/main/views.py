from django.shortcuts import render
import json
from ultralytics import YOLO
import numpy as np
from PIL import Image

from django.views.decorators.csrf import csrf_exempt


from django.http import HttpRequest,HttpResponse

# Create your views here.


def home_view(request : HttpRequest):
    return render(request, "main/home_view.html")



def about_view(request: HttpRequest):

    return render(request, "main/about_view.html")


def webcam_view(request):
    return render(request,"main/webcam.html")


model = YOLO('main/mymodel/best.pt')

def handle_uploaded_file(f):
    with open("uploads/image.jpeg", "wb") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@csrf_exempt
def webcam_result(request):
    
    
    if request.method == "POST" and "image" in request.FILES:   
        handle_uploaded_file(request.FILES["image"])
    
    
        img = None
        
        # with open("uploads/image.jpg", "rb") as file:
        #     img = file.read()
            
            
        img = Image.open("uploads/image.jpeg")
        
        
        #get the image
        
        image = ""
        #use the image to get the prediction
        
        results = model.track(source=img, show=True, tracker="bytetrack.yaml", conf=0.5, classes=1)

        fainted = False
        if results:
            fainted = True
        
        #return the reuslt
        
        response = {"is_fainted" : fainted}
    
    
        return HttpResponse(json.dumps(response))

    return HttpResponse("nothing")