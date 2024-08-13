from django.http import JsonResponse
from django.shortcuts import render
import requests

# Create your views here.
def allUsers(request):
    api_uri = 'https://dummyjson.com/users'
    try:
        response = requests.get(api_uri)
        data = response.json();
        # print(data['users'])
    except:
        data = {'error': 'An error occurred'}
    # return JsonResponse(data)
    return render(request, 'allUsers.html', {"users": data['users']})

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        try: 
            # finding user
            find_user_api = f'https://dummyjson.com/users/search?q={username}';
            response = requests.get(find_user_api)
            user = response.json()
            this_user = user['users'][0]
            if this_user['username'] == username and this_user['password'] == password:
                return render(request, 'login.html', {"user": this_user})
            else:
                return render(request, 'login.html', {"error": "Invalid username or password"})
        except:
            return render(request, 'login.html', {"error": "Username does not exists"})
    return render(request, 'login.html', {"user": ''})

def getCapacity(request):
    api_obj_uri = "https://api.restful-api.dev/objects"
    try:
        response = requests.get(api_obj_uri)
        jsonData = response.json() 
        print(jsonData[0]['data']['capacity'])
    except:
        jsonData = {'error': 'An error occurred'}

    return render(request, 'capacity.html', {"objects": jsonData})
