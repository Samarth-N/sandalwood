from django.shortcuts import render

# Create your views here.
def my_View(request):
    myName="sandalwood"
    s1="yash"
    s2="sudeep"
    s3="appu"
    s4="sreeleela"
    s5="aashika"
    s6="saptami"
    d={"name":myName,"actor1":s1,"actor2":s2,"actor3":s3,"actor4":s4,"actor5":s5,"actor6":s6}
    return render(request,"myApp/1.html",d)
        
