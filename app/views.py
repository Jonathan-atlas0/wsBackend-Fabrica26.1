from django.shortcuts import render
from .virustotal import VirusTotalService
from .models import Historico

def home(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        try:
            result = VirusTotalService().scan_url(url)
        except Exception as e:
            return render(request, 'base.html', {'erro': str(e), 'link': url})
        return render(request, 'base.html', {'result': result, 'link': url})
    return render(request, 'base.html')

def home(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        try:
            result = VirusTotalService().scan_url(url)

            Historico.objects.create(
                tipo='URL',
                url=url,
                resultado='Malicioso' if result['data']['attributes']['stats']['malicious'] > 0 else 'Limpo'
            )
        except Exception as e:
            return render(request, 'base.html', {'erro': str(e), 'link': url})

        historico = Historico.objects.all().order_by('-data')
        return render(request, 'base.html', {'result': result, 'link': url, 'historico': historico})

    historico = Historico.objects.all().order_by('-data')
    return render(request, 'base.html', {'historico': historico})