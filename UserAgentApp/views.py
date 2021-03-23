from django.shortcuts import render


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    user_agent = request.META['HTTP_USER_AGENT']
    ip = get_client_ip(request)
    return render(request, 'index.html', {'user_agent': user_agent, 'user_ip': ip})
