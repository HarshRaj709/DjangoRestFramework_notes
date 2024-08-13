from rest_framework.pagination import PageNumberPagination

class CustomPage(PageNumberPagination):
    page_size = 3
    # page_query_param = 'p'
    # page_size_query_param = 'records' #with help of this user can get records ---->http://127.0.0.1:8000/listview/?page=1&records=5
    # max_page_size = 4   #by this we can limit user to get records use with page_size_query_param
    # last_page_strings = 'end' #by this we can override our last keyword used to go last page
    