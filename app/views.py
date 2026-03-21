from django.shortcuts import render, redirect
from .virustotal import VirusTotalService
from .ipinfo import buscar_ip as consultar_ip
from .models import Tipo, ConsultaVirusTotal, ConsultaIPInfo


def home(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        try:
            result = VirusTotalService().scan_url(url)
            tipo = Tipo.objects.get_or_create(nome='URL')[0]

            ConsultaVirusTotal.objects.create(
                tipo=tipo,
                url=url,
                status=result['data']['attributes']['status'],
                malicioso=result['data']['attributes']['stats']['malicious'],
                inofensivo=result['data']['attributes']['stats']['harmless'],
                suspeito=result['data']['attributes']['stats']['suspicious'],
            )
        except Exception as e:
            return render(request, 'base.html', {'erro': str(e), 'link': url})

        historico_url = ConsultaVirusTotal.objects.all().order_by('-data')
        historico_ip = ConsultaIPInfo.objects.all().order_by('-data')
        return render(request, 'base.html', {'result': result, 'link': url, 'historico_url': historico_url, 'historico_ip': historico_ip})

    historico_url = ConsultaVirusTotal.objects.all().order_by('-data')
    historico_ip = ConsultaIPInfo.objects.all().order_by('-data')
    return render(request, 'base.html', {'historico_url': historico_url, 'historico_ip': historico_ip})


def limpar_historico(request):
    if request.method == 'POST':
        ConsultaVirusTotal.objects.all().delete()
        ConsultaIPInfo.objects.all().delete()
    return redirect('app:home')


def editar_historico(request, id):
    item = ConsultaVirusTotal.objects.get(id=id)
    if request.method == 'POST':
        item.url = request.POST.get('url')
        item.status = request.POST.get('status')
        item.malicioso = request.POST.get('malicioso')
        item.inofensivo = request.POST.get('inofensivo')
        item.suspeito = request.POST.get('suspeito')
        item.save()
        return redirect('app:home')
    return render(request, 'editar.html', {'item': item})


def buscar_ip(request):
    if request.method == 'POST':
        ip = request.POST.get('ip')
        try:
            resultado_ip = consultar_ip(ip)
            tipo = Tipo.objects.get_or_create(nome='IP')[0]

            ConsultaIPInfo.objects.create(
                tipo=tipo,
                ip=ip,
                cidade=resultado_ip.get('city', ''),
                regiao=resultado_ip.get('region', ''),
                pais=resultado_ip.get('country', ''),
                organizacao=resultado_ip.get('org', ''),
                timezone=resultado_ip.get('timezone', ''),
            )
        except Exception as e:
            return render(request, 'base.html', {'erro_ip': str(e), 'ip': ip})

        historico_url = ConsultaVirusTotal.objects.all().order_by('-data')
        historico_ip = ConsultaIPInfo.objects.all().order_by('-data')
        return render(request, 'base.html', {'resultado_ip': resultado_ip, 'ip': ip, 'historico_url': historico_url, 'historico_ip': historico_ip})

    return redirect('app:home')