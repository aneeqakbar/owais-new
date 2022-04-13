from datetime import datetime, timedelta
from django.http import Http404, HttpResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.forms import ClientCreateForm
from django.db.models import Count
from .models import Client, DataBrand, DataProduct
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

class IndexView(View):
    def get(self, request):
        labels = []
        values = []

        # for client in request.user.clients.all():
        #     labels.append(client.name)
        #     values.append(len(client.get_all_data))

        clients_data = {
            "labels": labels,
            "values": values
        }
        context = {
            "clients_data": clients_data
        }
        return render(request, "dashboard/index.html", context)


class ViewClientData(View):
    def get(self, request, client_id, data_type):
        fields = []

        order_filter = request.GET.get("o", None)
        
        page = request.GET.get("page", 1)
        template_name = 'dashboard/client_data_view.html'
        client = Client.objects.get(id = client_id)
        if not client.user == request.user:
            return HttpResponse("You cant access this client", status = 401)

        if data_type == "product":
            fields = [
                "id",
                "Product",
                "Entity",
                "Operation",
                "Campaign_Id",
                "Ad_Group_Id",
                "Portfolio_Id",
                "Ad_Id",
                "Keyword_Id",
                "Product_Targeting_Id",
                "Campaign_Name",
                "Ad_Group_Name",
                "Start_Date",
                "End_Date",
                "Targeting_Type",
                "State",
                "Daily_Budget",
                "SKU",
                "ASIN",
                "Ad_Group_Default_Bid",
                "Bid",
                "Keyword_Text",
                "Match_Type",
                "Bidding_Strategy",
                "placementProductPage",
                "placementTop",
                "Product_Targeting_Expression",
            ]
            template_name = 'dashboard/client_product_data_view.html'
            data = client.data_products.all().order_by("-id")
        elif data_type == "brand":
            fields = [
                "id",
                "Product",
                "Entity",
                "Operation",
                "Campaign_Id",
                "Draft_Campaign_Id",
                "Portfolio_Id",
                "Ad_Group_Id",
                "Keyword_Id",
                "Product_Targeting_Id",
                "Campaign_Name",
                "Start_Date",
                "End_Date",
                "State",
                "Budget_Type",
                "Budget",
                "Bid_Optimization",
                "Bid_Multiplier",
                "Bid",
                "Keyword_Text",
                "Match_Type",
                "Product_Targeting_Expression",
                "Ad_Format",
                "Landing_Page_URL",
                "Landing_Page_Asins",
                "Brand_Entity_Id",
                "Brand_Name",
                "Brand_Logo_Asset_Id",
                "Brand_Logo_URL",
            ]
            template_name = 'dashboard/client_brand_data_view.html'
            data = client.data_brands.all().order_by("-id")
        else:
            raise Http404()

        if order_filter:
            if str(order_filter).startswith("-"):
                data = data.order_by(f"{fields[int(order_filter)]}")
            else:
                data = data.order_by(f"-{fields[int(order_filter)]}")

        paginator = Paginator(data, 20)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        context = {
            "data_type": data_type,
            "client": client,
            "data": data
        }
        return render(request, template_name, context)


class ViewClientDataAnalytics(View):
    def get(self, request, client_id, data_type, field):
        page = request.GET.get("page", 1)
        order_filter = request.GET.get("o", None)
        fields = [
            "Entity",
            "Campaign_Id",
            "Ad_Group_Id",
            "Keyword_Id",
            "Product_Targeting_Id",
            "Keyword_Text",
            "Product_Targeting_Expression",
        ]
        template_name = 'dashboard/client_data_view.html'
        client = Client.objects.get(id = client_id)
        if data_type == "product":
            template_name = 'dashboard/client_product_field_data_view.html'
            data = client.data_products.all().order_by("-id")
        elif data_type == "brand":
            template_name = 'dashboard/client_brand_field_data_view.html'
            data = client.data_brands.all().order_by("-id")
        else:
            raise Http404()

        try:
            if order_filter:
                if str(order_filter).startswith("-"):
                    data = data.order_by(f"{fields[int(order_filter)]}")
                else:
                    data = data.order_by(f"-{fields[int(order_filter)]}")
        except:
            pass

        paginator = Paginator(data, 20)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        if not client.user == request.user:
            return HttpResponse("You cant access this client", status = 401)

        context = {
            "data_type": data_type,
            "client": client,
            "field": field,
            "data": data
        }
        return render(request, template_name, context)

class ViewDataChartAnalytics(View):
    def get(self, request, data_id, data_type, field):
        days = request.GET.get("days", 0)
        template_name = 'dashboard/client_product_chart_data_view.html'
        if data_type == "P":
            data = get_object_or_404(DataProduct, id = data_id)
        elif data_type == "B":
            data = get_object_or_404(DataBrand, id = data_id)

        if not data.client.user == request.user:
            return HttpResponse("You cant access this data", status = 401)

        days = int(days) or 30
        chart_data = data.get_chart_data(field_name=field, days=days)

        context = {
            "data_type": data_type,
            "field": field,
            "chart_data": chart_data,
            "data": data
        }
        return render(request, template_name, context)

class AddClientView(LoginRequiredMixin, View):
    def get(self, request):
        form = ClientCreateForm()

        context = {
            'heading': "Create a new client",
            'form': form,
        }

        return render(request, 'dashboard/render_form.html', context)

    def post(self, request):
        form = ClientCreateForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.user = request.user
            client.save()
            messages.success(request, f'Your account has been updated!')

            previous_url = request.META.get("HTTP_REFERER", None)

            if previous_url:
                return redirect(previous_url)
            return redirect('sheets:IndexView')
        context = {
            'form': form,
        }
        return render(request, 'dashboard/render_form.html', context)

class UpdateClientView(LoginRequiredMixin, View):
    def get(self, request, client_id):
        client = Client.objects.get(id = client_id)

        if not client.user == request.user:
            return HttpResponse("You cant edit this client", status = 401)

        form = ClientCreateForm(instance=client)

        context = {
            'heading': f"Editing client ({client.name})",
            'form': form,
        }

        return render(request, 'dashboard/render_form.html', context)

    def post(self, request, client_id):
        client = Client.objects.get(id = client_id)
        if not client.user == request.user:
            return HttpResponse("You cant edit this client", status = 401)

        form = ClientCreateForm(request.POST, instance=client)

        if form.is_valid():
            client = form.save(commit=False)
            client.user = request.user
            client.save()
            messages.success(request, f'Client has been updated!')
            return redirect('dashboard:ManageClientView')
        context = {
            'form': form,
        }
        return render(request, 'dashboard/render_form.html', context)


class ManageClientView(LoginRequiredMixin, View):
    def get(self, request):

        create_form = ClientCreateForm()

        context = {
            'heading': "Create a new client",
            'create_form': create_form,
        }

        return render(request, 'dashboard/manage_clients.html', context)

    def post(self, request):
        previous_url = request.META.get("HTTP_REFERER", None)
        action = request.POST.get("action", None)
        if action == "delete":
            client_id = request.POST.get("client_id", None)
            client = Client.objects.get(id = client_id)
            if not client.user == request.user:
                return HttpResponse("You dont have permission", status = 401)
            client.delete()
            messages.success(request, f'Client has been deleted!')
            if previous_url:
                return redirect(previous_url)
            return redirect('sheets:IndexView')
        else:
            form = ClientCreateForm(request.POST)
            if form.is_valid():
                client = form.save(commit=False)
                client.user = request.user
                client.save()
                messages.success(request, f'Client has been created!')
                
                
                if previous_url:
                    return redirect(previous_url)
                return redirect('sheets:IndexView')
        context = {
            'form': form,
        }
        return render(request, 'dashboard/render_form.html', context)
