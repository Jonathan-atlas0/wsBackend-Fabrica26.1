from django.shortcuts import render
from .virustotal import VirusTotalService

def home(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        try:
            result = VirusTotalService().scan_url(url)
        except Exception as e:
            return render(request, 'base.html', {'erro': str(e), 'link': url})
        return render(request, 'base.html', {'result': result, 'link': url})
    return render(request, 'base.html')