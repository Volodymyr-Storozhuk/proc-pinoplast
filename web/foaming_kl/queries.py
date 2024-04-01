from foaming_kl.models import General
from django.db.models import Sum
import datetime as dt


def get_query_full(foaming: str, date_query: str):
    # start_date = str(dt.datetime.now().strftime("%Y-%m-%d")) + ' 08:00'
    # end_date = str((dt.datetime.today() + dt.timedelta(days=1)).strftime("%Y-%m-%d")) + ' 07:59'
    start_date = date_query + ' 07:00'
    end_date = str((dt.datetime.strptime(date_query, "%Y-%m-%d") + dt.timedelta(days=1)).strftime("%Y-%m-%d")) + ' 06:59'
    rows = General.objects.filter(datetimestart__gte=start_date,
                                  datetimestop__lte=end_date,
                                  productionline=foaming,
                                  rawmatweightactual__gt='0',
                                  ).order_by('loadfiletime')
    return rows


def get_query_total_sum_full(foaming: str, date_query: str):
    start_date = date_query + ' 07:00'
    end_date = str((dt.datetime.strptime(date_query, "%Y-%m-%d") + dt.timedelta(days=1)).strftime("%Y-%m-%d")) + ' 06:59'
    rows = General.objects.filter(datetimestart__gte=start_date,
                                  datetimestop__lte=end_date,
                                  productionline=foaming,
                                  rawmatweightactual__gt='0',
                                  ).values('rawmatweightactual').aggregate(Sum('rawmatweightactual'))
    return rows


def get_query_first(foaming: str, date_query: str):
    # start_date = str(dt.datetime.now().strftime("%Y-%m-%d")) + ' 08:00'
    # end_date = str((dt.datetime.today() + dt.timedelta(days=1)).strftime("%Y-%m-%d")) + ' 07:59'
    start_date = date_query + ' 07:00'
    end_date = str((dt.datetime.strptime(date_query, "%Y-%m-%d") + dt.timedelta(days=1)).strftime("%Y-%m-%d")) + ' 06:59'
    rows = General.objects.filter(datetimestart__gte=start_date,
                                  datetimestop__lte=end_date,
                                  productionline=foaming,
                                  r_mpurecipe='0',
                                  rawmatweightactual__gt='0',
                                  ).order_by('loadfiletime')
    return rows


def get_query_total_sum_first(foaming: str, date_query: str):
    start_date = date_query + ' 07:00'
    end_date = str((dt.datetime.strptime(date_query, "%Y-%m-%d") + dt.timedelta(days=1)).strftime("%Y-%m-%d")) + ' 06:59'
    rows = General.objects.filter(datetimestart__gte=start_date,
                                  datetimestop__lte=end_date,
                                  productionline=foaming,
                                  r_mpurecipe='0',
                                  rawmatweightactual__gt='0',
                                  ).values('rawmatweightactual').aggregate(Sum('rawmatweightactual'))
    return rows
