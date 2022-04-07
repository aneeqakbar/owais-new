from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from sheets.process_data import ProcessSheetData
from dashboard.models import Client
from django.contrib.auth import login
from django.contrib.auth.models import User
import datetime

# Create your views here.

CLIENT_SHEET_FOLDER = "media/data_sheets/"

class HomeView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            user = User.objects.get(username="admin")
            login(request, user)
        return render(request, "home/index.html")


class UploadClientData(View):
    def post(self, request, client_id):
        client = Client.objects.get(id = client_id)

        if not client.user == request.user:
            return HttpResponse("Cant access the client", status = 401)
        
        uploaded_file = request.FILES["file"]
        date = request.POST["date"]
        print(date)
        fs = FileSystemStorage(location=CLIENT_SHEET_FOLDER) #defaults to   MEDIA_ROOT  
        new_name = f"{datetime.datetime.now().timestamp()}--{uploaded_file._name}"
        filename = fs.save(new_name, uploaded_file)
        file_path = f"{CLIENT_SHEET_FOLDER}{filename}"

        file_process = ProcessSheetData(file_path=file_path, type="P", client=client)
        date = date.split("-")
        date = datetime.datetime(year=int(date[0]), month=int(date[1]), day=int(date[2]))
        data = file_process.process_data(commit=False)
        file_process.commit_product_data(dataframe = data, date=date)
        # file_process.commit_brand_data(data = data)

        # file_process = ProcessSheetData(file_path=file_path, type="B", client=client)
        # file_process.process_data(commit=True)

        previous_url = request.META.get("HTTP_REFERER", None)
        if previous_url:
            return redirect(previous_url)
        return redirect('sheets:IndexView')