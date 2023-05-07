from django.shortcuts import render
from .models import UserInfo
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    info = UserInfo.objects.all()
    
    return render(request=request, template_name='index.html', context={'info' : info})

# @csrf_exempt
def save_info(request):
    if request.method == 'POST':
        stuid = request.POST.get('id')
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        if stuid == "":
            user = UserInfo(name=name, email=email, password=password)
        else:
            user = UserInfo(id=stuid, name=name, email=email, password=password)
        user.save()
        stud = UserInfo.objects.values()
        print(stud)
        information = list(stud)
        return JsonResponse({'status': 'Save', 'information':information})
    else:
        JsonResponse({'status': 0})


def update_info(request):
    if request.method == 'POST':
        id = request.POST['sid']
        user = UserInfo.objects.get(pk=id)
        user_data = {'id':user.id, 'name': user.name, 'email': user.email, 'password': user.password}
        return JsonResponse(user_data)
    else:
        JsonResponse({'status': 0})

def delete_info(request):
    if request.method == 'POST':
        id = request.POST['sid']
        user = UserInfo.objects.get(pk=id)
        print(user)
        user.delete()
        return JsonResponse({'status': 1})
    else:
        JsonResponse({'status': 0})
    