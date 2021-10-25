from django.shortcuts import render
from .forms import CsvForm
from .models import Csv
import csv
from django.contrib.auth.models import User
from soccer.models import Soccer, Statistic

# from django.http import HttpResponse

# Create your views here.


def upload_file_view(request):

    form = CsvForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        form = CsvForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)

            for row in reader:
                
                squad = row[0].upper()
                age = row[2].upper()
                poss = row[3].upper()

                # prod, _ = Statistic.objects.get_or_create(possession=row[3])
                
                # user= User.objects.get(username)

                Soccer.objects.create(
                    squad = squad,
                    # poss = poss,
                    # age = age,
                    # poss = int((poss))
                )
              
                # Statistic.objects.create(
                #     poss = poss,
                #     age = age,
                # )

                print(row[3])
                                
                # print(row)
                # print(type(row))

    return render(request, 'csvs/upload.html', {"form": form})

