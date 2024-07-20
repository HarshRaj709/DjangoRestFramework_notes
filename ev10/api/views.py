from rest_framework import mixins,generics
from .models import Student
from .serializer import StudentSerializer

# List and create -pk not required.
class StudentList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

    queryset=Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    

#Retrive update and destroy
class StudentRetrieve(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,pk,*args,**kwargs):                #retieve ke through 1 dataset ko dekh sakte h.
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,pk,*args,**kwargs):            #it works for both partial adn complete update of dataset
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


    