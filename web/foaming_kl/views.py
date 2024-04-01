from django.shortcuts import render
import datetime as dt
from django.contrib.auth.decorators import login_required
from django.db import DatabaseError
from django.db.models import F
# from django.http import HttpResponse
from .queries import (get_query_first,
                      get_query_full,
                      get_query_total_sum_full,
                      get_query_total_sum_first)
from .models import General
from .serializators import GeneralSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# date_query = dt.datetime.now().strftime("%Y-%m-%d")


def init_request_session(request):
    """
    Init request.session for date_query variable
    """
    if "date_query" not in request.session:
        request.session["date_query"] = dt.datetime.now().strftime("%Y-%m-%d")
    return request.session["date_query"]


@login_required
def foaming_view(request):
    context = {}
    if request.GET.get('date_query') is not None:
        date_query = request.GET.get('date_query')
        request.session["date_query"] = date_query
    else:
        date_query = init_request_session(request)

    try:
        if request.method == 'GET':
            context = {
                'rows_v1': get_query_full('V1', date_query),
                'rows_v1_total': get_query_total_sum_full('V1', date_query),
                'rows_v2': get_query_full('V2', date_query),
                'rows_v2_total': get_query_total_sum_full('V2', date_query),
                'date_query': date_query,

            }
        return render(request, 'foaming_kl/full.html', context=context)

    except DatabaseError:
        return render(request, 'foaming_kl/alert.html')


@login_required
def foaming_line_1_view(request):
    context = {}
    if request.GET.get('date_query') is not None:
        date_query = request.GET.get('date_query')
        request.session["date_query"] = date_query
    else:
        date_query = init_request_session(request)

    try:
        if request.method == 'GET':
            context = {
                'rows_v1': get_query_full('V1', date_query),
                'rows_v1_total': get_query_total_sum_full('V1', date_query),
                'date_query': date_query,
            }

        return render(request, 'foaming_kl/full_1.html', context=context)

    except DatabaseError:
        return render(request, 'foaming_kl/alert.html')


@login_required
def foaming_line_2_view(request):
    context = {}
    if request.GET.get('date_query') is not None:
        date_query = request.GET.get('date_query')
        request.session["date_query"] = date_query
    else:
        date_query = init_request_session(request)

    try:
        if request.method == 'GET':
            context = {
                'rows_v2': get_query_full('V2', date_query),
                'rows_v2_total': get_query_total_sum_full('V2', date_query),
                'date_query': date_query,
            }

        return render(request, 'foaming_kl/full_2.html', context=context)

    except DatabaseError:
        return render(request, 'foaming_kl/alert.html')


@login_required
def foaming_cycle_0_view(request):
    context = {}
    if request.GET.get('date_query') is not None:
        date_query = request.GET.get('date_query')
        request.session["date_query"] = date_query
    else:
        date_query = init_request_session(request)

    try:
        if request.method == 'GET':
            context = {
                'rows_v1': get_query_first('V1', date_query),
                'rows_v1_total': get_query_total_sum_first('V1', date_query),
                'rows_v2': get_query_first('V2', date_query),
                'rows_v2_total': get_query_total_sum_first('V2', date_query),
                'date_query': date_query,
            }

        return render(request, 'foaming_kl/first.html', context=context)

    except DatabaseError:
        return render(request, 'foaming_kl/alert.html')


@login_required
def foaming_line_1_cycle_0_view(request):
    context = {}
    if request.GET.get('date_query') is not None:
        date_query = request.GET.get('date_query')
        request.session["date_query"] = date_query
    else:
        date_query = init_request_session(request)

    try:
        if request.method == 'GET':
            context = {
                'rows_v1': get_query_first('V1', date_query),
                'rows_v1_total': get_query_total_sum_first('V1', date_query),
                'date_query': date_query,
            }

        return render(request, 'foaming_kl/first_1.html', context=context)

    except DatabaseError:
        return render(request, 'foaming_kl/alert.html')


@login_required
def foaming_line_2_cycle_0_view(request):
    context = {}
    if request.GET.get('date_query') is not None:
        date_query = request.GET.get('date_query')
        request.session["date_query"] = date_query
    else:
        date_query = init_request_session(request)

    try:
        if request.method == 'GET':
            context = {
                'rows_v2': get_query_first('V2', date_query),
                'rows_v2_total': get_query_total_sum_first('V2', date_query),
                'date_query': date_query,
            }

        return render(request, 'foaming_kl/first_2.html', context=context)

    except DatabaseError:
        return render(request, 'foaming_kl/alert.html')


# @api_view(["GET"])
# def selected_cycle_list(request, date_query, cycle):
#     # print(f'request url: {request}')
#     # print(f'request param: {date_query}, {cycle}')
#     try:
#         start_date = date_query + ' 07:30'
#         end_date = str((dt.datetime.strptime(date_query, "%Y-%m-%d") + dt.timedelta(days=1)).strftime("%Y-%m-%d")) + ' 07:59'
#         rows = General.objects.filter(datetimestart__gte=start_date,
#                                       datetimestop__lte=end_date,
#                                       r_mpurecipe=cycle,
#                                       rawmatweightactual__gt='0',
#                                       ).order_by('loadfiletime')
#         # print(f'start date: {start_date}')
#         # print(f'end date: {end_date}')
#         # print('ROWS:')
#         # print(rows)

#         if request.method == "GET":
#             serializer = GeneralSerializer(rows, many=True)
#             # print('SERIALIZER:')
#             # print(serializer)
#             # print('SERIALIZER DATA:')
#             # print(serializer.data)
#             return Response(serializer.data, status=status.HTTP_200_OK)

#     except DatabaseError:
#         return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)


# @api_view(["GET"])
# def cycle_list(request, date_query):

#     try:
#         start_date = date_query + ' 07:30'
#         end_date = str((dt.datetime.strptime(date_query, "%Y-%m-%d") + dt.timedelta(days=1)).strftime("%Y-%m-%d")) + ' 07:59'
#         rows = General.objects.filter(datetimestart__gte=start_date,
#                                       datetimestop__lte=end_date,
#                                       rawmatweightactual__gt='0',
#                                       ).order_by('loadfiletime')

#         if request.method == "GET":
#             serializer = GeneralSerializer(rows, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)

#     except DatabaseError:
#         return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)


# @api_view(["GET"])
# def cycle_list(request, date_query, cycle=None):
#     # print(f'request url: {request}')
#     # print(f'request param: {date_query}, {cycle}')
#     try:
#         start_date = date_query + ' 07:30'
#         end_date = str((dt.datetime.strptime(date_query, "%Y-%m-%d")
#                         + dt.timedelta(days=1)).strftime("%Y-%m-%d")) + ' 07:59'
#         # if cycle:
#         #     rows = General.objects.filter(datetimestart__gte=start_date,
#         #                                   datetimestop__lte=end_date,
#         #                                   r_mpurecipe=cycle,
#         #                                   rawmatweightactual__gt='0',
#         #                                   ).order_by('loadfiletime')
#         # else:
#         #     rows = General.objects.filter(datetimestart__gte=start_date,
#         #                                   datetimestop__lte=end_date,
#         #                                   rawmatweightactual__gt='0',
#         #                                   ).order_by('loadfiletime')
#         rows = General.objects.filter(datetimestart__gte=start_date,
#                                       datetimestop__lte=end_date,
#                                       r_mpurecipe=cycle if cycle is not None else F('r_mpurecipe'),
#                                       rawmatweightactual__gt='0',
#                                       ).order_by('loadfiletime')

#         if request.method == "GET":
#             serializer = GeneralSerializer(rows, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)

#     except DatabaseError:
#         return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)


@api_view(["GET"])
def cycle_list(request):
    date_query = request.GET.get("date_query")
    cycle = request.GET.get("cycle")

    try:
        start_date = date_query + ' 07:00'
        end_date = str((dt.datetime.strptime(date_query, "%Y-%m-%d")
                        + dt.timedelta(days=1)).strftime("%Y-%m-%d")) + ' 06:59'
        rows = General.objects.filter(datetimestart__gte=start_date,
                                      datetimestop__lte=end_date,
                                      r_mpurecipe=cycle if cycle is not None else F('r_mpurecipe'),
                                      rawmatweightactual__gt='0',
                                      ).order_by('loadfiletime')

        if request.method == "GET":
            serializer = GeneralSerializer(rows, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    except DatabaseError:
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
