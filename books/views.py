from django.shortcuts import render
from django.http import HttpResponse


from .models import Book, BookSerializer
# Create your views here.


def index(request):
    return render(request, 'books/index.html')


def save_book(request):

    name = request.GET['name']
    price = request.GET['price']
    pages = request.GET['pages']
    book = Book.objects.create(name=name, price=price, pages=pages)
    print(book)
    return HttpResponse(book.name +"is saved")


def get_all_books(request):
    # lst=[]
    # books = Book.objects.all()
    # for i in books:
    #     serializer = BookSerializer(i, many=False)
    #     lst.append(serializer.data)
    # import json
    # val = json.dumps(lst)
    # print(val[0])
    # return HttpResponse(val)

    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    val = serializer.data
    import json
    val = json.dumps(val)
    print(val)
    return HttpResponse(val)
