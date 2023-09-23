from django.shortcuts import render
from .forms import ImageUploadForm
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

# Create your views here.

def handle_file(f):
    with open('img.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def index(request):
    return render(request, "predApp/index.html")

def predict(request):
    form = ImageUploadForm(request.POST, request.FILES)
    if form.is_valid():
        handle_file(request.FILES['image'])
        model = ResNet50(weights='imagenet')
        img_path = 'img.jpg'
        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        preds = model.predict(x)
        print('Predicted:', decode_predictions(preds, top=3)[0])
        pred = decode_predictions(preds, top=3)[0]
        res = []
        for p in pred:
            res.append((p[1].replace('_', ' ').replace('-', ' ').title(), np.round(p[2]*100, 2)))

    return render(request, "predApp/result.html", {'res': res,})