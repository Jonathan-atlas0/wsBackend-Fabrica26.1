from django.shortcuts import render, redirect
from .virustotal import VirusTotalService
from .models import Historico




##funções banco com virustotal
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

def limpar_historico(request):
    Historico.objects.all().delete()
    return redirect('app:home')

def editar_historico(request, id):
    item = Historico.objects.get(id=id)
    if request.method == 'POST':
        item.tipo = request.POST.get('tipo')
        item.url = request.POST.get('url')
        item.resultado = request.POST.get('resultado')
        item.save()
        return redirect('app:home')
    return render(request, 'editar.html', {'item': item})
##funçao do ipinfo

def buscar_ip(request):
    if request.method == 'POST':
        ip = request.POST.get('ip')
        try:
            from .ipinfo import buscar_ip as consultar_ip
            resultado_ip = consultar_ip(ip)
        except Exception as e:
            return render(request, 'base.html', {'erro_ip': str(e), 'ip': ip})
        
        historico = Historico.objects.all().order_by('-data')
        return render(request, 'base.html', {'resultado_ip': resultado_ip, 'ip': ip, 'historico': historico})
    
    return redirect('app:home')


