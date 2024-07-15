

-------------------------------------> Lets start with Django Rest Framework <------------------------------------


Ques.1 What is serialization in DRF?

Ans.1 THe process of converting data such as querysets and model instances to native python datatype are called 
        serialization in DRF.

                ------------> Starting with installing DjangoRestFrameWork(DRF) <--------------

    ------> pip install djangorestframework

------------------------------------------------------------------------------------------------------------------


            --------------------------> gs1 Django Serializer <----------------------------

    Python json: Python has a built in package called json,which is used to work with json data.

            dumps(data):This is used to convert python dictionary into json string.

                        import json
                        python_data = {'name':'harsh'.'roll':101}
                        json_data = json.dumps(python_data)
                        print(json_data)        ----------> {"name":"harsh","roll":101}

            loads(data): This is used to parse json string.

                        import json
                        json_data = {"name":"harsh","roll":101}
                        parsed_data = json.loads(json_data)
                        print(parsed_data)          ------------> {'name':'harsh'.'roll':101}

    
    Serializers: In Django, serializers are a crucial component for converting complex data types, such as Django 
                 model instances or querysets, into native Python data types(called serialization). They also 
                 facilitate the process of converting native Python data types back into complex data types. 
                 Serializers play a significant role in handling the conversion of data to and from formats 
                 like JSON for frontend.

                Serializer are also responsible for deserialization which means it allows parsed data to be converted
                back into complex types,after first validating the incoming data.

            --------------------> TO do serialization we use Serializer Class <-------------------

    A Serializer Class is very similar to a django Form and Model form class, and includes similar validation flags
    on the various fields, such as required,max_length and default.

    Drf provides a Serializer class which gives you a powerful,generic way to control the output of your responses,
    as well as a ModelSerializer Class which provides a useful shortcut for creating that deal with model instances
    and querysets.

-------------------> Approach

    Create a seperat serializers.py file to write all serializers

            from rest_framework import serializers

            class StudentSerializers(serializers.Serializer):
                name = serializers.Charfield(max_length=100)
                roll = serializers.IntegerField()
                city = serializers.Charfield(max_length=100)

    serializer.data:
        This is serialized data. to check what is in serializer.

    JSONRenderer:
        This is used to render data into JSON which is understandable by Front-end.

        from rest_framework.renderers import JSONRenderer

        json_data = JSONRenderer().render(serializer.data)


-------------------------

        (Model Objects)-----------serialization----------->(Python Dict)---------Render into Json-----> (Json Data)
        complex data types                           Python native Data  type                          

-------------------------

    JsonResponse():
        JsonResponse(data,encode=DjangoJSONEncoder,safe = True,json_dumps_params = None,**kwargs)

        An httpResponse subclass that helps to create a JSON-encoded response.it inherits most behaviour from its
        superclass a couple differences.



           ---------------------------------> Practical Approach <---------------------------------------------


    Create project, then create app, register app and rest_framework.....

Step1:          INSTALLED_APPS = [
                    'django.contrib.admin',
                    'django.contrib.auth',
                    'django.contrib.contenttypes',
                    'django.contrib.sessions',
                    'django.contrib.messages',
                    'django.contrib.staticfiles',
                    'rest_framework',
                    'api',
                ]

Step2:   Create models.py
            from django.db import models

            # Create your models here.
            class Student(models.Model):
                name = models.CharField(max_length=50)
                roll = models.IntegerField()
                city = models.CharField(max_length=50)

                def __str__(self):
                    return self.name

step3:  create Serializers.py
            from rest_framework import serializers

            class StudentSerializers(serializers.Serializer):
                name = serializers.CharField(max_length=50)
                roll = serializers.IntegerField()
                city = serializers.CharField(max_length=50)

step4:  Create Views.py

        from django.shortcuts import render,HttpResponse
        from .models import Student
        from .serializers import StudentSerializers
        from rest_framework.renderers import JSONRenderer


        # Create your views here.
        def student_details(request):
            stu = Student.objects.get(id=3)         #specifying which objects data we want?
            serializer = StudentSerializers(stu)        #here we serialized our data----> complex data to python native datatype
            print(serializer)
            json_data = JSONRenderer().render(serializer.data)      #rendering our python native datatype to jsondata.
            return HttpResponse(json_data,content_type = 'application/json')

-------------------> Quesryset


        def student_details(request):
            stu = Student.objects.all()         #specifying which objects data we want?
            serializer = StudentSerializers(stu,many = True)        #here we use all students data so we have to make many = True
            print(serializer)
            json_data = JSONRenderer().render(serializer.data)      #rendering our python native datatype to jsondata.
            return HttpResponse(json_data,content_type = 'application/json')


--------------------------------------------> Api Use Example

        here we create a new file. 

        myapp.py

            import requests

            URL = 'http://127.0.0.1:8000/stuinfo/'

            r = requests.get(url = URL)

            data = r.json()
            print(data,end='')

            output - [{'name': 'Harsh', 'roll': 101, 'city': 'lucknow'}, 
                      {'name': 'Rahul', 'roll': 102, 'city': 'kanpur'}, 
                      {'name': 'Ashish Bajpai', 'roll': 103, 'city': 'barabanki'}]


---------------------------> Use of JsonResponse

    By this we can reduce line of code, in this we dont need to render data.

    from django.http import JsonResponse 

    def student_details(request):
        stu = Student.objects.all()         #specifying which objects data we want?
        serializer = StudentSerializers(stu,many = True)        #here we use all students data so we have to make many = True
        print(serializer)
        # json_data = JSONRenderer().render(serializer.data)      #rendering our python native datatype to jsondata.
        # return HttpResponse(json_data,content_type = 'application/json')
        return JsonResponse(serializer.data,safe=False)


-------------> If you want to see id in json data you have explicitly define that in serializers.py

                from rest_framework import serializers

                class StudentSerializers(serializers.Serializer):
                    id = serializers.IntegerField()
                    name = serializers.CharField(max_length=50)
                    roll = serializers.IntegerField()
                    city = serializers.CharField(max_length=50)

-------------> How to pass jason data to templates

                from django.shortcuts import render
                from .serializers import StudentSerializers
                from django.http import JsonResponse
                from .models import Students

                ----> views.py

                        def stu(request):
                            # student = Students.objects.get(pk=1)
                            student = Students.objects.all()
                            serial = StudentSerializers(student,many=True)
                            context = {'student_data':serial.data}
                            return render(request,'trial/student.html',context)


------------------------------------------------------------------------------------------------------------------

                            -------------> gs2 - deserialization <---------------

        
        
    In Django, deserialization refers to the process of converting data from a serialized format 
    (such as JSON or XML) back into native Python objects. This process is commonly used when handling incoming 
    data from external sources, like user input or API requests. Django provides a built-in serializer called 
    serializers in the django.core package, which makes it easy to serialize and deserialize complex data types, 
    such as Django models.

    ----------> Before Start with deserialization in practical there are some terms which are necessary to know..

    1.BytesIO:   
            BytesIO is not specifically a part of Django or Django REST Framework; rather, it is a class provided 
            by the Python standard library in the io module.
            BytesIO is a class that implements an in-memory binary stream using a bytes-like interface. It allows 
            you to treat bytes data as a file-like object, providing methods for reading and writing.

    2.JsonParser:
            JSONParser is a class provided by the Django REST Framework, an extension to the Django web framework 
            that adds support for building RESTful APIs. Specifically, JSONParser is part of the DRF's parsing 
            framework.
            The JSONParser class is responsible for parsing incoming JSON data from HTTP requests. When a client 
            sends a POST or PUT request with JSON-formatted data in the request body, the JSONParser is used to 
            interpret that data and convert it into a Python data structure that can be easily processed by the 
            Django views and serializers.

----------------> Practical Approach

    ---->1.create models.py 

            from django.db import models

            # Create your models here.
            class Student(models.Model):
                name = models.CharField(max_length=50)
                roll = models.IntegerField()
                city = models.CharField(max_length=50)

    ---->2. serializers.py

                from rest_framework import serializers
                from .models import Student

                class Studentserializer(serializers.Serializer):
                    name = serializers.CharField(max_length=50)
                    roll = serializers.IntegerField()
                    city = serializers.CharField(max_length=50)

                    def create(self,validate_data):                         #here we use spaecial function to add data in our database
                        return Student.objects.create(**validate_data)      

    ---->3. Create an external python app which sends json data to our webapp...

            import requests
            import json

            URL = 'http://127.0.0.1:8000/stu/'

            data = {
                'name':'Harsh',
                'roll':101,
                'city':'lucknow'
            }

            json_data = json.dumps(data)

            r = requests.post(url=URL,data=json_data)
            data = r.json()
            print(data)

    ---->4. Create Urls

                from django.contrib import admin
                from django.urls import path
                from api import views

                urlpatterns = [
                    path('admin/', admin.site.urls),
                    path('stu/',views.student_create,name='home')
                ]

    ---->5. Create views.py

                from django.shortcuts import render
                import io
                from rest_framework.parsers import JSONParser
                from .serializers import Studentserializer
                from rest_framework.renderers import JSONRenderer
                from django.http import HttpResponse,JsonResponse
                from django.views.decorators.csrf import csrf_exempt


                # Create your views here.
                @csrf_exempt
                def student_create(request):
                    if request.method == 'POST':
                        json_data = request.body            #used to catch data
                        stream = io.BytesIO(json_data)          # Create a BytesIO stream from the JSON data.
                        python_data = JSONParser().parse(stream)        # Use the JSONParser to parse the JSON data into Python data.
                        serializer = Studentserializer(data=python_data)
                        if serializer.is_valid():
                            serializer.save()
                            res = {'msg':'data created'}
                            # json_data = JSONRenderer().render(res)
                            # return HttpResponse(json_data,content_type = 'application/json')
                            return JsonResponse(serializer.data)
                        json_data = JSONRenderer().render(serializer.errors)        #Render JSON-formatted validation errors.
                        return HttpResponse(json_data,content_type = 'application/json')


-------------------------------------------------------------------------------------------------------------------

                ----------------------> ev3 API Crud Application <-----------------------

1.  Update Data: 

                from rest_framework import serializers

                class StudentSerializer(serializer.Serializers):
                    name = serializers.CharField(max_length = 50)
                    roll = serializers.IntegerField()
                    city = serializers.CharField(max_length = 50)

                    def update(self,instance,validate_data):            #instance = old data on database, validate_data = new data to update.
                        instance.name = validate_data.get('name',instance.name)
                        instance.roll = validate_data.get('roll',instance.roll)
                        instance.city = validate_data.get('city',instance.city)
                        instance.save()
                        return instance

---------> complete Update data: In update we have to provide all values, otherwise we will get error.
        Required all Data form front/Client.

        serializer = StudentSerializer(stu,data = python_data)
        if serializer.is_valid():
            serializer.save()

--------> Partial Update Data:But what if we only want to update some fields of data, not whole/each field of data 
                in that case we use this Approach.
                    
        serializer = StudentSerializer(stu,data = python_data,partial = True)
        if serializer.is_valid():
            serializer.save()


---------------------------------------------> Practical Approach <---------------------------------------------


        How to run this Project (ev3) first run all migration command and create super user.
        THen open terminal and run server.
        Open another terminal run app.py ....
<html>
        <body>
        <img src = 'https://github.com/HarshRaj709/DjangoRestFramework_notes/blob/main/ss.png' width = '100%', height='50%' >
        </body>
</html>
      

                                ------------> Only to Access data <---------------
-----> models.py

        from django.db import models

        # Create your models here.
        class Student(models.Model):
            name = models.CharField(max_length = 50)
            roll = models.IntegerField()
            city = models.CharField(max_length = 50)
    
------> serializers.py

        from rest_framework import serializers
        from .models import Student

        class Studentserializer(serializers.Serializer):
            name = serializers.CharField(max_length = 50)
            roll = serializers.IntegerField()
            city = serializers.CharField(max_length = 50)

------> myapp.py: here we applied logic that if we not provide id then it will retrive all students data. otherwise
                    will provide single user data.

        import requests
        import json

        URL = 'http://127.0.0.1:8000/'

        def get_data(id = None):
            data = {}
            if id is not None:
                data = {'id':id}            #this is python dict, so we have to convert it to json type.
            json_data = json.dumps(data)        #converted python dictionary to json data.
            r= requests.get(url = URL,data = json_data)     #here we used GET method
            data = r.json()
            print(data)
        get_data()

-------> views.py

            from django.shortcuts import render
            from rest_framework.parsers import JSONParser
            from rest_framework.renderers import JSONRenderer
            import io
            from .models import Student
            from .serializers import Studentserializer
            from django.http import HttpResponse

            # Create your views here.
            def student_api(request):
                if request.method == 'GET':
                    json_data = request.body
                    stream = io.BytesIO(json_data)
                    python_data = JSONParser().parse(stream)            #converted data to python data
                    id = python_data.get('id',None)     # checking for id

                    if id is not None:
                        stu = Student.objects.get(pk=id)
                        serializer = Studentserializer(stu)
                        # return JsonResponse(serializer.data)
                        json_data = JSONRenderer().render(serializer.data)          #converting back to json data.
                        return HttpResponse(json_data,content_type='application/json')
                    else:
                        stu = Student.objects.all()
                        serializer = Studentserializer(stu,many = True)
                        json_data = JSONRenderer().render(serializer.data)
                        return HttpResponse(json_data,content_type='application/json')


                        ---------------------> Create New Data <--------------------

    -------> Myapp.py: third party application to test our APIs

                def post_data():
                data = {
                    'name':'kohinoor',
                    'roll':106,
                    'city':'bareli',
                }

                json_data = json.dumps(data)
                r = requests.post(url = URL,data = json_data)       #there may be a chances that we get some notification or data after saving user we will show it thorugh r
                data = r.json()       #here we converted our data back to json to show it in frontend.
                print(data)

            post_data()

    --------> serializers.py

                    from rest_framework import serializers
                    from .models import Student

                    class Studentserializer(serializers.Serializer):
                        name = serializers.CharField(max_length = 50)
                        roll = serializers.IntegerField()
                        city = serializers.CharField(max_length = 50)

                        def create(self,validate_data):
                            return Student.objects.create(**validate_data)


    ----------> VIews.py

                if request.method == 'POST':
                    json_data = request.body
                    stream = io.BytesIO(json_data)  
                    python_data = JSONParser().parse(stream)        # converting json data to python data
                    serializer = Studentserializer(data = python_data)      #conerting python data to complex data
                    if serializer.is_valid():
                        serializer.save()
                        res = {'msg':'data saved successfully'}
                        json_data = JSONRenderer().render(res)  #converting back python to json data type.
                        return HttpResponse(json_data,content_type='application/json')
                    json_data = JSONRenderer().render(serializer.errors)    #if serializer not get validate then pass errors.
                    return HttpResponse(json_data,content_type='application/json')


                                --------------> Updating Data <-------------

    partially upadted: here in our myapp.py we not provided the value of roll....

    -------> myapp.py

                    def update_data():
                        data = {
                            'id':4,
                            'name':'new',
                            # 'roll':106,
                            'city':'bareli',
                        }

                        json_data = json.dumps(data)
                        r = requests.put(url = URL,data = json_data)       #there may be a chances that we get some notification or data after saving user we will show it thorugh r
                        data = r.json()       #here we converted our data back to json to show it in frontend.
                        print(data)

                    update_data()

    -------> serializers.py

                from rest_framework import serializers
                from .models import Student

                class Studentserializer(serializers.Serializer):
                    name = serializers.CharField(max_length = 50)
                    roll = serializers.IntegerField()
                    city = serializers.CharField(max_length = 50)

                    def create(self,validate_data):
                        return Student.objects.create(**validate_data)

                    def update(self,instance,validate_data):
                        instance.name = validate_data.get('name',instance.name)
                        instance.roll = validate_data.get('roll',instance.roll)
                        instance.city = validate_data.get('city',instance.city)
                        instance.save()
                        return instance

    -------> Views.py

                if request.method == 'PUT':
                    json_data = request.body
                    stream = io.BytesIO(json_data)  
                    python_data = JSONParser().parse(stream)        # converting json data to python data
                    id = python_data.get('id')
                    stu = Student.objects.get(id=id)
                    serializer = Studentserializer(stu,data = python_data,partial = True)       #as we are partially updating our data
                    if serializer.is_valid():
                        serializer.save()
                        res = {'msg':'data updated successfully'}
                        json_data = JSONRenderer().render(res)  #converting back python to json data type.
                        return HttpResponse(json_data,content_type='application/json')
                    json_data = JSONRenderer().render(serializer.errors)    #if serializer not get validate then pass errors.
                    return HttpResponse(json_data,content_type='application/json')

                ------------------------------> Delete data <----------------------------------

    ---------> views.py

                if request.method =='DELETE':
                    json_data = request.body
                    stream = io.BytesIO(json_data)
                    python_data = JSONParser().parse(stream)
                    id = python_data.get('id')
                    stu = Student.objects.get(id=id)
                    stu.delete()
                    res = {'msg':'data deleted'}
                    json_data = JSONRenderer().render(res)  #converting back python to json data type.
                    return HttpResponse(json_data,content_type='application/json')

    -------> myapp.py

                def delete_data():
                    data = {'id':4}

                    json_data = json.dumps(data)
                    r = requests.delete(url = URL,data = json_data)   # here we write delete
                    data = r.json()       #here we converted our data back to json to show it in frontend.
                    print(data)

                delete_data()


---------------------------------------------------------------------------------------------------------------

                    --------------------->ev4: Validation / Validators <------------------------
        
    There are two ways to apply Validation.
1. Field Level Validation       : single Field validation multiple field validation.
2. Object Level Validation      : Multiple Field validation


1.Field Level Validation:
    Used to add custom Field Validation.
    Same as clean_fieldName methods on Django forms.
    validate_fieldName methods should return the validated value or raise a serializers.ValidaionError

        Syntax:
                def validate_fieldname(self,value):     # in forms validation we only need to pass: def clean_fieldname(self)
        
        where value is the field that requires validation.

Exmaple:
        from rest_framework import serializers
        class Student(serializers.Serializer):
            name = serializers.CharField(max_length=50)
            roll = serializers.IntegerField()
            city = serializers.CharField(max_length=50)

            def validate_roll(self,value):      #value in this scenario have roll
                if value >= 200:
                    raise serializers.ValidaionError('Seat full')           # in Djangoforms we raise forms.ValidaionError('message')
                return roll

            def validate_name(self,value):      #check name already exist or not
                if Student.objects.filter(name = value):
                    raise serializers.ValidationError('name already used')
                return value
    
    THis method is automatically invoked when is_valid(): method is called same as forms.is_valid():

2. Object Level Validation
    In this we use validate() to validate objects.

        Syntax: def validate(self,data):
            where data is a dictionary of field values.

    Example:
        def validate(self,data):
            name = data.get('name')     #as data is dictionary
            city = data.get('city')
            if name.lower() == 'rohit' and city.lower != 'ranchi'
                raise serializers.ValidaionError('city must be Ranchi')
            return data

3. Validators
    This is used make our validation method reusable.
    declaring at single place and can use to multiple places.

        def start_with_r(value):        #before class declaration
            if value[0].lower() != 'r':
                raise serializers.ValidationError('name should start with r')
            

        class Studentserializers(serializers.Serializer):
            name = serializers.CharField(max_length=100,validators = [start_with_r])
            roll = serializers.IntegerField()
            city = serializers.CharField(max_length=50)
