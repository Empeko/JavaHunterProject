from django.shortcuts import render
from .models import top_vacancies_skillls as TopVacancies
from .hh import apiManager as hh_api


def index(request):
    return render(request, 'java_vacancies/index.html')


def demand(request):
    return render(request, 'java_vacancies/demand.html')


def geography(request):
    return render(request, 'java_vacancies/geography.html')


def skills(request):
    y_2015 = TopVacancies.objects.order_by('-count').filter(year=2015)[:10]
    y_2016 = TopVacancies.objects.order_by('-count').filter(year=2016)[:10]
    y_2017 = TopVacancies.objects.order_by('-count').filter(year=2017)[:10]
    y_2018 = TopVacancies.objects.order_by('-count').filter(year=2018)[:10]
    y_2019 = TopVacancies.objects.order_by('-count').filter(year=2019)[:10]
    y_2020 = TopVacancies.objects.order_by('-count').filter(year=2020)[:10]
    y_2021 = TopVacancies.objects.order_by('-count').filter(year=2021)[:10]
    y_2022 = TopVacancies.objects.order_by('-count').filter(year=2022)[:10]
    skills_years = (
        ("2015", y_2015), ("2016", y_2016), ("2017", y_2017), ("2018", y_2018), ("2019", y_2019), ("2020", y_2020),
        ("2021", y_2021), ("2022", y_2022))
    context = {'skills_years': skills_years}
    return render(request, 'java_vacancies/skills.html', context)


def hh_vacancies(request):
    vacancies = hh_api.get_vacancies(10)
    context = {'vacancies': vacancies}
    return render(request, 'java_vacancies/hh_vacancies.html', context)
