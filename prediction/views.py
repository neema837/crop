from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.db.models import Q
from . models import *
import numpy as np
import os
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

# Create your views here. 
filepath = 'D:\\farm\\crop\\Training Sets\\tomato-leaftrain\\tomato-leaf.h5'
model = load_model(filepath)

def welcomepred(request):
    return render(request,'Prediction/tomato_leaf/tomleaf_sample.html')


def tomatoleafpredict(request):
    if request.method == 'POST':
        file = request.FILES['image'] # fet input
        filesave= UploadImage(image=file)
        filesave.save()
        filename = str(filesave.image)   
        print("@@ Input posted = ", filename)
        path = settings.MEDIA_ROOT
        print("Path =  ",path)
        print(path + "/" +filename)

        file_path = path + "\\" +filename

        print("@@ Predicting class......")
  
        test_image = load_img(file_path, target_size = (128, 128)) # load image 
        print("@@ Got Image for prediction")
        
        test_image = img_to_array(test_image)/255 # convert image to np array and normalize
        test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
        
        result = model.predict(test_image) # predict diseased palnt or not
        print('@@ Raw result = ', result)
        
        pred = np.argmax(result, axis=1)
        print(pred)
        if pred==0:
            input_image = filename
            text = "Tomato - Bacteria Spot Disease"
            desc ="Copper fungicides are the most commonly recommended treatment for bacterial leaf spot. Use copper fungicide as a preventive measure after you’ve planted your seeds but before you’ve moved the plants into their permanent homes. You can use copper fungicide spray before or after a rain, but don’t treat with copper fungicide while it is raining. If you’re seeing signs of bacterial leaf spot, spray with copper fungicide for a seven- to 10-day period, then spray again for one week after plants are moved into the field. Perform maintenance treatments every 10 days in dry weather and every five to seven days in rainy weather."
            return render(request, 'Prediction/tomato-leaf/Tomato-Disease-Prediction.html',{'input_image':input_image,'pred_text':text,'desc':desc})
            
        elif pred==1:
            input_image = filename
            text = "Tomato - Early Blight Disease"
            desc = "Tomatoes that have early blight require immediate attention before the disease takes over the plants. Thoroughly spray the plant (bottoms of leaves also) with Bonide Liquid Copper Fungicide concentrate or Bonide Tomato & Vegetable. Both of these treatments are organic."
            return render(request, 'Prediction/tomato-leaf/Tomato-Disease-Prediction.html',{'input_image':input_image,'pred_text':text,'desc':desc})                 
        elif pred==2:
            input_image = filename
            text = "Tomato -Healthy Leaf"
            desc="There is no treatment for the healthy Tomato leaf."
            return render(request, 'Prediction/tomato-leaf/Tomato-Disease-Prediction.html',{'input_image':input_image,'pred_text':text,'desc':desc})                 

                
        elif pred==3:
            input_image = filename
            text = "Tomato - Late Blight Disease"
            desc ="Tomatoes that have early blight require immediate attention before the disease takes over the plants. Thoroughly spray the plant (bottoms of leaves also) with Bonide Liquid Copper Fungicide concentrate or Bonide Tomato & Vegetable. Both of these treatments are organic.."
            return render(request, 'Prediction/tomato-leaf/Tomato-Disease-Prediction.html',{'input_image':input_image,'pred_text':text,'desc':desc})
            
        elif pred==4:
            input_image = filename
            text = "Tomato - Leaf Mold Disease"
            desc ="Use drip irrigation and avoid watering foliage. Use a stake, strings, or prune the plant to keep it upstanding and increase airflow in and around it. Remove and destroy (burn) all plants debris after the harvest."
            return render(request, 'Prediction/tomato-leaf/Tomato-Disease-Prediction.html',{'input_image':input_image,'pred_text':text,'desc':desc})          
          
        elif pred==5:
            input_image = filename
            text = "Tomato -Septoria Leaf Spot Disease"
            desc ="""Removing infected leaves:  Remove infected leaves immediately, and be sure to wash your hands and pruners thoroughly before working with uninfected plants.
                    Consider organic fungicide options: Fungicides containing either copper or potassium bicarbonate will help prevent the spreading of the disease. Begin spraying as soon as the first symptoms appear and follow the label directions for continued management.
                    Consider chemical fungicides: While chemical options are not ideal, they may be the only option for controlling advanced infections. One of the least toxic and most effective is chlorothalonil (sold under the names Fungonil and Daconil)."""
            return render(request, 'Prediction/tomato-leaf/Tomato-Disease-Prediction.html',{'input_image':input_image,'pred_text':text,'desc':desc})

                
        elif pred==6:
            input_image = filename
            text = "Tomato - Target Spot Disease"
            desc = "Many fungicides are registered to control of target spot on tomatoes. Growers should consult regional disease management guides for recommended products. Products containing chlorothalonil, mancozeb, and copper oxychloride have been shown to provide good control of target spot in research trials"
            return render(request, 'Prediction/tomato-leaf/Tomato-Disease-Prediction.html',{'input_image':input_image,'pred_text':text,'desc':desc})
            
                
        elif pred==7:
            input_image = filename
            text = "Tomato - Yellow Leaf Curl Viru Disease"
            desc ="Inspect plants for whitefly infestations two times per week. If whiteflies are beginning to appear, spray with azadirachtin (Neem), pyrethrin or insecticidal soap. For more effective control, it is recommended that at least two of the above insecticides be rotated at each spraying."
            return render(request, 'Prediction/tomato-leaf/Tomato-Disease-Prediction.html',{'input_image':input_image,'pred_text':text,'desc':desc})

        elif pred==8:
            input_image = filename
            text = "Tomato - Mosaic Virus Disease"
            desc ="""There are no cures for viral diseases such as mosaic once a plant is infected. As a result, every effort should be made to prevent the disease from entering your garden.
                    1.Fungicides will NOT treat this viral disease.
                    2.Plant resistant varieties when available or purchase transplants from a reputable source.
                    3.Do NOT save seed from infected crops.
                    4.Spot treat with least-toxic, natural pest control products, such as Safer Soap, Bon-Neem and diatomaceous earth, to reduce the number of disease carrying insects.
                    5.Harvest-Guard® row cover will help keep insect pests off vulnerable crops/ transplants and should be installed until bloom.
                    6.Remove all perennial weeds, using least-toxic herbicides, within 100 yards of your garden plot.
                    7.The virus can be spread through human activity, tools and equipment. Frequently wash your hands and disinfect garden tools, stakes, ties, pots, greenhouse benches, etc. (one part bleach to 4 parts water) to reduce the risk of contamination.
                    8.Avoid working in the garden during damp conditions (viruses are easily spread when plants are wet).
                    9.Avoid using tobacco around susceptible plants. Cigarettes and other tobacco products may be infected and can spread the virus.
                    10.Remove and destroy all infected plants (see Fall Garden Cleanup). Do NOT compost."""
            return render(request, 'Prediction/tomato-leaf/Tomato-Disease-Prediction.html',{'input_image':input_image,'pred_text':text,'desc':desc})

                
        elif pred==9:
            input_image = filename
            text = "Tomato - Two Spotted Spider Mite Disease"
            desc ="""For control, use selective products whenever possible. Selective products which have worked well in the field include:

                    bifenazate (Acramite): Group UN, a long residual nerve poison
                    abamectin (Agri-Mek): Group 6, derived from a soil bacterium
                    spirotetramat (Movento): Group 23, mainly affects immature stages
                    spiromesifen (Oberon 2SC): Group 23, mainly affects immature stages
                    OMRI-listed products include:

                    insecticidal soap (M-Pede)
                    neem oil (Trilogy)
                    soybean oil (Golden Pest Spray Oil)
                    With most miticides (excluding bifenazate), make 2 applications, approximately 5-7 days apart, to help control immature mites that were in the egg stage and protected during the first application. Alternate between products after 2 applications to help prevent or delay resistance."""
            return render(request, 'Prediction/tomato-leaf/Tomato-Disease-Prediction.html',{'input_image':input_image,'pred_text':text,'desc':desc})



bringal_filepath ='D:\\farm\\crop\\Training Sets\\brinjaltrain\\brinjal.h5'
bringalpath = load_model(bringal_filepath)


def brinjalprediction(request):
    return render(request,'prediction/brinjal/brinjal_sample.html')


def brinjalpred(request):
    if request.method == 'POST':
        file = request.FILES['image'] # fet input
        filesave= UploadImage(image=file)
        filesave.save()
        filename = str(filesave.image)   
        print("@@ Input posted = ", filename)
        path = settings.MEDIA_ROOT
        print("Path =  ",path)
        print(path + "/" +filename)

        file_path = path + "\\" +filename
        print("@@ Predicting class......")
        test_image = load_img(file_path, target_size = (128, 128)) # load image 
        print("@@ Got Image for prediction")
        
        test_image = img_to_array(test_image)/255 # convert image to np array and normalize
        test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
        
        result = bringalpath.predict(test_image) # predict diseased palnt or not
        print('@@ Raw result = ', result)
        # brinjal anthracnose phomopsis blight Healthy fruit rot
        pred = np.argmax(result, axis=1)
        if pred==0:
            input_image = filename
            text = "Brinjal Anthracnose Disease"
            desc = "asdfff"
            return  render(request,'prediction/brinjal/brinjal_result.html',{'input_image':input_image,'pred_text':text,'desc':desc})
       
        elif pred==1:
            input_image = filename
            text = "Brinjal Disease Phomopsis Blight"
            desc = ""
            return  render(request,'prediction/brinjal/brinjal_result.html',{'input_image':input_image,'pred_text':text,'desc':desc})
        
        elif pred==2:
            input_image = filename
            text = "Fruit Rot of Brinjal Disease"
            desc = ""
            return  render(request,'prediction/brinjal/brinjal_result.html',{'input_image':input_image,'pred_text':text,'desc':desc})
        
        elif pred==3:
            input_image = filename
            text = "Brinjal Healthy"
            desc = "There is no treatment for healthy brinjal"
            return  render(request,'prediction/brinjal/brinjal_result.html',{'input_image':input_image,'pred_text':text,'desc':desc})

#tomato_filepath ='E:\\farmproject\\Training Sets\\tomatotrain\\tomato.h5'
#tomatopath = load_model(tomato_filepath)


# def tomatopred(request):
#     return render(request,'Prediction/tomato/tomatoprediction.html')


# def tomatoprediction(request):
#     if request.method == 'POST':
#         file = request.FILES['image'] # fet input
#         filesave= UploadImage(image=file)
#         filesave.save()
#         filename = str(filesave.image)   
#         print("@@ Input posted = ", filename)
#         path = settings.MEDIA_ROOT
#         print("Path =  ",path)
#         print(path + "/" +filename)

#         file_path = path + "\\" +filename
#         print("@@ Predicting class......")
#         test_image = load_img(file_path, target_size = (128, 128)) # load image 
#         print("@@ Got Image for prediction")
        
#         test_image = img_to_array(test_image)/255 # convert image to np array and normalize
#         test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
        
#         result = tomatopath.predict(test_image) # predict diseased palnt or not
#         print('@@ Raw result = ', result)
#         pred = np.argmax(result, axis=1)
#         if pred==0:
#             input_image = filename
#             text = "Tomato Anthracnose Disease " 
#             desc =""
#             return render(request,'Prediction/tomato/Tomato-Disease.html',{'input_image':input_image,'pred_text':text,'desc':desc})
            
#         elif pred==1:
#             input_image = filename
#             text = "Tomato Bacterial Canker Disease " 
#             desc =""
#             return render(request,'Prediction/tomato/Tomato-Disease.html',{'input_image':input_image,'pred_text':text,'desc':desc})
                
#         elif pred==2:
#             input_image = filename
#             text = "Healthy Tomato  " 
#             desc ="There is no treatment needed"
#             return render(request,'Prediction/tomato/Tomato-Disease.html',{'input_image':input_image,'pred_text':text,'desc':desc})


# #pappaya_filepath ='E:\\farmproject\\Training Sets\\pappayatrain\pappaya.h5'
# #pappayapath = load_model(pappaya_filepath)


# def pappayapred(request):
#     return render(request,'Prediction/pappaya/pappayaprediction.html')

# def pappayaprediction(request):
#     if request.method == 'POST':
#         file = request.FILES['image'] # fet input
#         filesave= UploadImage(image=file)
#         filesave.save()
#         filename = str(filesave.image)   
#         print("@@ Input posted = ", filename)
#         path = settings.MEDIA_ROOT
#         print("Path =  ",path)
#         print(path + "/" +filename)

#         file_path = path + "\\" +filename
#         print("@@ Predicting class......")
#         test_image = load_img(file_path, target_size = (128, 128)) # load image 
#         print("@@ Got Image for prediction")
        
#         test_image = img_to_array(test_image)/255 # convert image to np array and normalize
#         test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
        
#         result = pappayapath.predict(test_image) # predict diseased palnt or not
#         print('@@ Raw result = ', result)
#         # brinjal anthracnose phomopsis blight Healthy fruit rot
#         pred = np.argmax(result, axis=1)
#         if pred==0:
#             input_image = filename
#             text = "Pappaya Anthracnose Disease"
#             desc =""
#             return render(request,'Prediction/pappaya/Papayya-Disease.html',{'input_image':input_image,'pred_text':text,'desc':desc})
       
#         elif pred==1:
#             input_image = filename
#             text = "Healthy Pappaya  "
#             desc ="There is no treatment needed"
#             return render(request,'Prediction/pappaya/Papayya-Disease.html',{'input_image':input_image,'pred_text':text,'desc':desc})
        
#         elif pred==2:
#             input_image = filename
#             text = "Pappaya Ringspot Disease"
#             desc =""
#             return render(request,'Prediction/pappaya/Papayya-Disease.html',{'input_image':input_image,'pred_text':text,'desc':desc})

#         elif pred==3:
#             input_image = filename
#             text = "Pappaya Phytophthora Disease"
#             desc =""
#             return render(request,'Prediction/pappaya/Papayya-Disease.html',{'input_image':input_image,'pred_text':text,'desc':desc})
                



# #paddy_filepath ='E:\\farmproject\\Training Sets\\paddytrain\paddy.h5'
# #paddypath = load_model(paddy_filepath)


# def paddypred(request):
#     return render(request,'Prediction/paddy/paddyprediction.html')


# def paddyprediction(request):
#     if request.method == 'POST':
#         file = request.FILES['image'] # fet input
#         filesave= UploadImage(image=file)
#         filesave.save()
#         filename = str(filesave.image)   
#         print("@@ Input posted = ", filename)
#         path = settings.MEDIA_ROOT
#         print("Path =  ",path)
#         print(path + "/" +filename)

#         file_path = path + "\\" +filename
#         print("@@ Predicting class......")
#         test_image = load_img(file_path, target_size = (128, 128)) # load image 
#         print("@@ Got Image for prediction")
        
#         test_image = img_to_array(test_image)/255 # convert image to np array and normalize
#         test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
        
#         result = paddypath.predict(test_image) # predict diseased palnt or not
#         print('@@ Raw result = ', result)
#         # brinjal anthracnose phomopsis blight Healthy fruit rot
#         pred = np.argmax(result, axis=1)
#         print(pred)
#         if pred==0:
#             input_image = filename
#             text= "Bacterial leaf blight Disease"
#             desc =""
#             return render(request,'Prediction/paddy/Paddy-Disease.html',{'input_image':input_image,'pred_output':text,'desc':desc})
#         elif pred==1:
#             input_image = filename
#             text= "Paddy-Brown spot Disease"
#             desc =""
#             return render(request,'Prediction/paddy/Paddy-Disease.html',{'input_image':input_image,'pred_output':text,'desc':desc})                
#         elif pred==2:
#             input_image = filename
#             text= "Healthy Paddy"
#             desc ="There is no Treatment needed"
#             return render(request,'Prediction/paddy/Paddy-Disease.html',{'input_image':input_image,'pred_output':text,'desc':desc})
                
#         elif pred==3:
#             input_image = filename
#             text= "Paddy Leaf smut Disease"
#             desc =""
#             return render(request,'Prediction/paddy/Paddy-Disease.html',{'input_image':input_image,'pred_output':text,'desc':desc})  