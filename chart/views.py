from django.shortcuts import render
from chart.models import City
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def pie_chart(request):
    labels = []
    data = []

    queryset = City.objects.order_by('-population')[:5]
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)

    return render(request, 'chart/pie_chart.html', {
        'labels': labels,
        'data': data,
    })

@login_required
def bar_chart(request):
    labels = []
    data = []

    queryset = City.objects.order_by('-population')[:15]
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)

    return render(request, 'chart/bar_chart.html', {
        'labels': labels,
        'data': data,
    })
    
@login_required
def summary(request):
    sum = 0 
    count = 0  
    queryset = City.objects.values()
    for i in range(len(queryset)):
        sum += queryset[i]['population']
        count += 1
    return render(request, 'chart/summary.html',{'sum':sum,'count':count})
