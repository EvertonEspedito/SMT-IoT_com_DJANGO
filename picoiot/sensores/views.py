from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Temperatura

def grafico(request):
    return render(request, 'sensores/grafico.html')

def dados_temperatura(request):
    dados = (
        Temperatura.objects
        .order_by('id')
        .values('valor', 'criado_em')
    )

    resposta = []
    for d in dados:
        resposta.append({
            'valor': d['valor'],
            'hora': d['criado_em'].strftime('%H:%M:%S')
        })

    return JsonResponse(resposta, safe=False)

@csrf_exempt
def receber_temperatura(request):
    if request.method != 'POST':
        return JsonResponse({'erro': 'Método inválido'}, status=405)

    try:
        data = json.loads(request.body.decode('utf-8'))

        temperatura = (
            data.get('temperatura')
            or data.get('temp')
            or data.get('valor')
        )

        if temperatura is None:
            return JsonResponse({'erro': 'Temperatura não enviada'}, status=400)

        Temperatura.objects.create(valor=float(temperatura))
        return JsonResponse({'status': 'ok'})

    except Exception as e:
        return JsonResponse({'erro': str(e)}, status=400)
