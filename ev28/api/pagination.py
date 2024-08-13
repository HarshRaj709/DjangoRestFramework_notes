from rest_framework.pagination import LimitOffsetPagination

class CustomPage(LimitOffsetPagination):
    default_limit = 3   #by this we can define default size
    limit_query_param = 'lallu' #by this we change default keyword limit of url
    max_limit = 1       #Atmost data to show
