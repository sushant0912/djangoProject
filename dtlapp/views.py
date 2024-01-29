from django.shortcuts import render

# Create your views here.
# def index(request):
#     username=input("enter your Username=")
#     contxt={}
#     contxt["username"]=username
#     # return render(request, "index.html",{"username":username})
#     return render (request,"index.html",contxt)
def index(request):
    username="admin"
    products=["iphone","samsung","nokia","One plus","huawei","vivo"]
    movies={"avengers":5,"joker":3,"wolf of wall street":5,"interstellar":4,"inception":5}
    fruitsdata=fruits()
    context={"username":username,
             "products":products,
             "movies":movies,
             "fruitsdata":fruitsdata,
             }
    return render(request,"index.html",context)

def fruits():
    fruitlist=("apple","banana","mango","orange","papaya")
    return fruitlist

def login(request):
    username=input("enter your Username=")
    context={"username":username}
    return render(request,"login.html",context)
