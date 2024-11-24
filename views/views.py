import os
# import gdown
# from io import BytesIO
from django.http import JsonResponse
from django.shortcuts import render
# import numpy as np
# import cv2
# from keras.preprocessing.image import img_to_array
# from keras.models import load_model
# from dotenv import load_dotenv
# from keras.preprocessing.image import load_img

# load_dotenv()

# model1 = None
# model2 = None
# model3 = None
# model4 = None

# def load_trained_model():
#     global model1
#     global model2
#     global model3
#     global model4

#     if model1 is None or model2 is None or model3 is None:
#         MODEL_DENSENET121 = "densenet121_model.h5"
#         MODEL_VGG19 = "vgg19_model.h5"
#         MODEL_MOBILENETV2 = "mobilenetv2_model.h5"
#         MODEL_INCEPTIONV3 = "inceptionv3_model.h5"

#         print("[INFO] loading models...")
#         try:
#             model1 = load_model(MODEL_DENSENET121)
#             model2 = load_model(MODEL_VGG19)
#             model3 = load_model(MODEL_MOBILENETV2)
#             model4 = load_model(MODEL_INCEPTIONV3)

#         except Exception as e:
#             print(f"[ERROR] Error loading model: {str(e)}")
#             raise e

# load_trained_model()

def index(request):
    return render(request, 'view/index.html')

def detect_image(request):
    if request.method == 'POST':
                return JsonResponse({'success': 1, 'label': "The model has not yet been deployed", 'value': 'error', 'probabilities': 0})
        
#         if model1 is None or model2 is None or model3 is None or model4 is None:
#             return JsonResponse({'success': 0, 'message': 'Model is not loaded properly'})

#         label_classes = ["No indication of tuberculosis", "Indicated tuberculosis", "Image cannot be identified!"]


#         if 'image' not in request.FILES:
#             return JsonResponse({'success': 0, 'message': 'No image file uploaded'})

#         useModel = request.POST.get('model', None)
        
#         print("Model used", useModel)
#         image_file = request.FILES['image']
        
#         filestr = image_file.read()


#         if not filestr:
#             return JsonResponse({'success': 0, 'message': 'Empty image file'})

#         if useModel == "InceptionV3" : 
            
#             image_stream = BytesIO(filestr)
#             img = load_img(image_stream, target_size=(224, 224))
#             img_array = img_to_array(img)

#             img_array = img_to_array(img)

#             if img_array.shape[-1] == 1:
#                 img_array = np.repeat(img_array, 3, axis=-1)

#             # Normalisasi gambar
#             img_array = img_array / 255.0

#             img_array = np.expand_dims(img_array, axis=0)
#             model = model4
            
#             proba = model.predict(img_array)[0]
#             predicted_class = np.round(proba).astype(int)

#             if predicted_class == 0:
#                 label = label_classes[0]
#                 value = "success"
#             elif predicted_class == 1:
#                 label = label_classes[1]
#                 value = "warning"
#             else:
#                 label = label_classes[2]
#                 value = "error"

#             return JsonResponse({'success': 1, 'label': label, 'value': value, 'probabilities': proba.tolist()})
            
#         npimg = np.frombuffer(filestr, np.uint8)
#         image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)


#         if image is None:
#             return JsonResponse({'success': 0, 'message': 'Failed to decode image'})


#         image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


#         image_resized = cv2.resize(image_rgb, (224, 224))
#         image_resized = image_resized.astype("float") / 255.0 
#         image_resized = img_to_array(image_resized)
#         image_resized = np.expand_dims(image_resized, axis=0)

#         if useModel == "DenseNet121" :
#             model = model1
#         if useModel =="VGG19" :
#             model = model2
#         if useModel == "MobileNetV2" :
#             model = model3
        
#         print("[INFO] Predicting image...")
#         proba = model.predict(image_resized)[0]
#         predicted_class = np.round(proba).astype(int)


#         if predicted_class == 0:
#             label = label_classes[0]
#             value = "success"
#         elif predicted_class == 1:
#             label = label_classes[1]
#             value = "warning"
#         else:
#             label = label_classes[2]
#             value = "error"


#         print(f"Label: {label}")
#         print(f"Prediction probabilities: {proba}")


#         return JsonResponse({'success': 1, 'label': label, 'value': value, 'probabilities': proba.tolist()})


    return JsonResponse({'error': 1, 'message': 'Unsupported HTTP method'})

