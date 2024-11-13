from .models import sensor
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .serializers import IOTSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
#from sklearn.model_selection import train_test_split
"""from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier"""

from  django.conf import settings
import os
import json


@api_view(['GET' ,'POST'])
def liste(request):
    if request.method=='GET':
        Iot = sensor.objects.all()
        seriali = IOTSerializer(Iot, many=True)
        return JsonResponse({'sensor':seriali.data})
    if request.method== 'POST':
        seriali = IOTSerializer(data=request.data)
        if seriali.is_valid():
            seriali.save()
            return Response (seriali.data, status=status.HTTP_201_CREATED)
        
@api_view(['PUT','GET','DELETE','OPTIONS'])

def uni(request,id):
    try :
        senso = sensor.objects.get(id=id)
    except sensor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    senso = get_object_or_404(sensor, pk=id)
    if request.method=='PUT' or request.method=='OPTIONS':   
        serial = IOTSerializer(senso, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_202_ACCEPTED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method=='GET':
        serial = IOTSerializer(senso)
        return JsonResponse(serial.data, safe=False)
    
    if request.method == 'DELETE':
        senso = sensor.objects.get(id=id)
        senso.delete()
        return Response("delete")


"""@api_view(['GET' ,'POST'])
def survie(request):
    if request.method=='POST':
        age=request.POST["age"]
        anaemia=request.POST["anemia"] 
        creatinine_phosphokinase=request.POST["creatinine_phosphokinase"] 
        diabetes=request.POST["diabetes"] 
        ejection_fraction=request.POST["ejection_fraction"]
        high_blood_pressure=request.POST["high_blood_pressure"]
        platelets=request.POST["platelets"]
        serum_creatinine=request.POST["serum_creatinine"]
        serum_sodium=request.POST["serum_sodium"]
        sex=request.POST["sex"]
        smoking=request.POST["smoking"]
        #time=request.POST["time"]
        time = 60
        # filepath = os.path.join(settings.STATIC_ROOT, 'attaque_cardiaque.csv')
        data = pd.read_csv(os.path.join('static/','attaque_cardiaque.csv'))
        IQR = 582-121
        Max=582+(1.5*IQR)
        Min=121-(1.5*IQR)
        data = data.drop(data[data['creatinine_phosphokinase']>3000].index)
        data.loc[data['creatinine_phosphokinase'] > Max, 'creatinine_phosphokinase'] = Max
        IQR2=45-30
        Max1 = 45+(1.5*IQR2)
        data.loc[data['ejection_fraction'] > Max1, 'ejection_fraction'] = Max1
        IQR3= 310000-213000
        Max3 = 310000 + (1.5*IQR3)
        Min3 = 213000 - (1.5*IQR3)
        data = data.drop(data[data['platelets']>600000].index)
        data.loc[data['platelets'] > Max3, 'platelets']= Max3
        data.loc[data['platelets']< Min3 ,'platelets'] = Min3
        IQR4=140.0-134.0
        Min4= 134.0 - (1.5*IQR4)
        data.loc[data['serum_sodium'] <Min4 , 'serum_sodium']= Min4
        IQR5=1.400000-0.900000
        Max5=1.400000 + (1.5*IQR5)
        data.loc[data['serum_creatinine']>Max5, 'serum_creatinine'] =Max5
        y = data['DEATH_EVENT']
        X = data.drop (['DEATH_EVENT'], axis=1)
        X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=0.25, random_state=123)
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)
        classifer = KNeighborsClassifier(n_neighbors=5)
        classifer.fit(X_train,y_train)
        classifer.score(X_train,y_train)
        classifer.score(X_test,y_test)
        predict = classifer.predict(sc.transform([[age, anaemia, creatinine_phosphokinase, diabetes,ejection_fraction, high_blood_pressure, platelets,serum_creatinine, serum_sodium, sex, smoking, time]]))
        proba =classifer.predict_proba(sc.transform([[age, anaemia, creatinine_phosphokinase, diabetes,ejection_fraction, high_blood_pressure, platelets,serum_creatinine, serum_sodium, sex, smoking, time]]))
        #survie(classifer,10,0,45,0,30,0,328000,2.00,120,0,1,60)
        print("JSON ",predict) 
        #print(proba)
        
        # return JsonResponse({'sensor':predict})
         
        result = int(predict[0])
        #vie = int(proba[0])
        #Mort = int(proba[1])
        print("JSON ",result) 
        bonjour = 'edson'
        #return json.dumps({'message':result})
        response_data = {
            'message': result,  # Use meaningful titles for each data item
            #'vie': vie,
            #'Mort':Mort,
        # ... add more data items with titles ...
        }
        #print(Mort)
        #print(vie)
        #return Response(response_data)S
    
    if request.method== 'POST':
        seriali = IOTSerializer(data=request.data)
        if seriali.is_valid():
            seriali.save()
            return Response (seriali.data, status=status.HTTP_201_CREATED)"""