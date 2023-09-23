from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
import csv
import urllib.parse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # Read-in data
    bus_stations_list = []
    with open('data-398-2018-08-30.csv', 'r') as f:
        csv_reader = csv.DictReader(f, delimiter=',')
        for line in csv_reader:
            sorted_line = {'Name': line['Name'], 'Street': line['Street'], 'District': line['District']}
            bus_stations_list.append(sorted_line)

    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(bus_stations_list, 11)
    current_page = paginator.get_page(page_num)

    objects_on_page = current_page.object_list

    next_page_url = f'{reverse(bus_stations)}?{urllib.parse.urlencode({"page": current_page})}'

    if current_page.has_next():
        next_page_params = {'page': current_page.next_page_number()}
        params = urllib.parse.urlencode(next_page_params)
        next_page_url = f'{reverse(bus_stations)}?{params}'

    prev_page_url = f'{reverse(bus_stations)}?{urllib.parse.urlencode({"page": current_page})}'

    if current_page.has_previous():
        prev_page_params = {'page': current_page.previous_page_number()}
        params = urllib.parse.urlencode(prev_page_params)
        prev_page_url = f'{reverse(bus_stations)}?{params}'

    context = {
        'bus_stations': objects_on_page,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    }

    return render(request, 'stations/index.html', context)
