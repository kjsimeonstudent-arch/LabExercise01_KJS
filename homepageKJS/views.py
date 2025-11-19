from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def user_list_view(request):
    return render(request, 'user_list.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def users_html(request):
    return render(request, 'users.html')

def logout_view(request):
    return render(request, 'logout.html')

def register_user(request):
    return render(request, 'register_user.html')

def list_users(request):
    return render(request, 'list_users.html')

def user_detail(request, pk):
    return render(request, 'user_detail.html', {'pk': pk})
