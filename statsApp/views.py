from django.shortcuts import render, get_object_or_404
from .models import *
from django.views import View

class LatestTransfersView(View):
    def get(self, request):
        context = {
            'transferlar': Transfer.objects.order_by('-sana')
        }

        return render(request, 'latest-transfers.html')

class TransferView(View):
    def get(self, request):
        transfers = Transfer.objects.order_by('-narx')
        context = {'transfers': transfers}
        return render(request, 'transfer-records.html', context)

class Transfers150View(View):
    def get(self, request):
        bashoratlar = Transfer.objects.order_by('-sana')[:150]
        return render(request, '150-accurate-predictions.html', {'bashoratlar': bashoratlar})

class Top50transfersbyexpendeture(View):
    def get(self, request):
        club = Transfer.objects.order_by('-narx')
        return render(request, 'top-50-clubs-by-expenditure-in-2021.html', {'club': club})



