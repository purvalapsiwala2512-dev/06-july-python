from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp.models import *


def index(request):
    return render(request, "index.html")


def test(request):
    q = request.GET.get("q")
    return HttpResponse(f"Hello {q}")


def search(request):
    q = request.GET.get("q")


def countries(request):
    try :
        print("test")
        countries = Country.objects.all()
        print(countries)
        return JsonResponse({"data":list(countries.values())})
    except Exception as e:
        print(e)


def states(request):
    cid = request.GET.get("cid")
    state=State.objects.filter(country_id=cid)
    return JsonResponse({"data":list(state.values())})



def cities(request):
    sid = request.GET.get("sid")
    cities=City.objects.filter(state_id=sid)
    return JsonResponse({"data":list(cities.values())})

    # country_id = request.GET.get("country_id")

    # # states = State.objects.filter(country_id=country_id)

    # # return JsonResponse({
    # #     "data": list(states.values("id", "name"))
    # # })
    
    # # state_id = request.GET.get("state_id")

    # # cities = City.objects.filter(state_id=state_id)

    # # return JsonResponse({
    # #     "data": list(cities.values("id", "name"))
    # # })
    # pass

