from django.shortcuts import render

# Create your views here.


from rest_framework.viewsets import ViewSet
from app.models import *
from app.serializers import *
from rest_framework.response import Response


class productcurdVS(ViewSet):
    def list(self,request):
        PQS=product.objects.all()
        PSD=productserializers(PQS,many=True)
        return Response(PSD.data)
    

    def create(self,request):
        SD=productserializers(data=request.data)
        if SD.is_valid():
            SD.save()
            return Response({'success':'product is  created'})
        else:
            return Response({'failed':'product is not created'})
        

    def retrieve(self,request,pk):
        SPO=product.objects.get(pk=pk)
        SPD=productserializers(SPO)
        return Response(SPD.data)
    

    def update(self,request,pk):
        SPO=product.objects.get(pk=pk)
        SPD=productserializers(SPO,data=request.data)
        if SPD.is_valid():
            SPD.save()
            return Response({'updated':'product is updated'})
        else:
            return Response({'failed':'product is not updated'})
        
    def partial_update(self,request,pk):
        SPO=product.objects.get(pk=pk)
        SPD=productserializers(SPO,data=request.data,partial=True)
        if SPD.is_valid():
            SPD.save()
            return Response({'updated':'product is updated'})
        else:
            return Response({'failed':'product is not updated'})
        
    def destroy(self,request,pk):
        product.objects.get(pk=pk).delete()
        return Response({'deleted':'product is deleted'})
