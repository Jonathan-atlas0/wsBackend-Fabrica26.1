from django.shortcuts import render
from .virustotal import VirusTotalService

def home(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        result = VirusTotalService().scan_url(url)
        return render(request, 'base.html', {'result': result, 'link': url})
    return render(request, 'base.html')