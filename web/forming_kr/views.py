from django.shortcuts import render
import datetime as dt
from django.contrib.auth.decorators import login_required
from django.db import DatabaseError
from .queries import (get_query_full,
                      get_query_group_by_typbloku,
                      get_query_total_count_blocks)


# date_query = dt.datetime.now().strftime("%Y-%m-%d")


def init_request_session(request):
    """ Init request.session for date_query variable"""

    if "date_query" not in request.session:
        request.session["date_query"] = dt.datetime.now().strftime("%Y-%m-%d")
    #     print(f'new date_query in session: {request.session["date_query"]}')
    #     print(f'new expiry session datetime: {request.session.get_expiry_date()}')
    # else:
    #     print(f'date_query from session: {request.session["date_query"]}')
    #     print(f'expiry session datetime: {request.session.get_expiry_date()}')

    return request.session["date_query"]


@login_required
def forming_full(request):
    context = {}
    try:
        # global date_query
        request.session["date_query"] = init_request_session(request)

        if request.method == 'POST':
            request.session["date_query"] = request.POST.get('date_query')
            # date_query = request.POST.get('date_query')

        context = {
            'rows_f3': get_query_full('3', request.session["date_query"]),
            'date_query': request.session["date_query"],
        }
        return render(request, 'forming_kr/full.html', context=context)

    except DatabaseError:
        return render(request, 'forming_kr/alert.html')


@login_required
def forming_full_3(request):
    context = {}
    try:
        # global date_query
        request.session["date_query"] = init_request_session(request)

        if request.method == 'POST':
            request.session["date_query"] = request.POST.get('date_query')
            # date_query = request.POST.get('date_query')

        context = {
            'rows_f3': get_query_full('3', request.session["date_query"]),
            'date_query': request.session["date_query"],
        }
        return render(request, 'forming_kr/full_3.html', context=context)

    except DatabaseError:
        return render(request, 'forming_kr/alert.html')


@login_required
def forming_group_by_typebloku(request):
    context = {}
    try:
        # global date_query
        request.session["date_query"] = init_request_session(request)

        if request.method == 'POST':
            request.session["date_query"] = request.POST.get('date_query')
            # date_query = request.POST.get('date_query')

        context = {
            # 'render_date': dt.datetime.now().strftime("%Y-%m-%d  %H:%M"),
            'rows_f3': get_query_group_by_typbloku('3', request.session["date_query"]),
            'rows_f3_total': get_query_total_count_blocks('3', request.session["date_query"]),
            'date_query': request.session["date_query"],
        }
        return render(request, 'forming_kr/group_typeblock.html', context=context)

    except DatabaseError:
        return render(request, 'forming_kr/alert.html')


@login_required
def forming_group_by_typebloku_3(request):
    context = {}
    try:
        # global date_query
        request.session["date_query"] = init_request_session(request)

        if request.method == 'POST':
            request.session["date_query"] = request.POST.get('date_query')
            # date_query = request.POST.get('date_query')

        context = {
            'rows_f3': get_query_group_by_typbloku('3', request.session["date_query"]),
            'rows_f3_total': get_query_total_count_blocks('3', request.session["date_query"]),
            'date_query': request.session["date_query"],
        }
        return render(request, 'forming_kr/group_typeblock_3.html', context=context)

    except DatabaseError:
        return render(request, 'forming_kr/alert.html')
