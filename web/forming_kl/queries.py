from forming_kl.models import Blockstorage
from django.db.models import Count
import datetime as dt


def get_query_full(forming: str, date_query: str):
    # start_date = str(dt.datetime.now(tz=get_current_timezone()).strftime("%Y-%m-%d")) + ' 08:00'
    # start_date = str(dt.datetime.now().strftime("%Y-%m-%d")) + ' 08:00'
    # end_date = str((dt.datetime.today() + dt.timedelta(days=1)).strftime("%Y-%m-%d")) + ' 07:59'
    start_date = date_query + ' 08:00'
    end_date = str((dt.datetime.strptime(date_query, "%Y-%m-%d") + dt.timedelta(days=1)).strftime("%Y-%m-%d")) + ' 07:59'
    rows = Blockstorage.objects.filter(dataczasprodukcji__range=(start_date, end_date),
                                       kodkreskowy__startswith=forming,
                                       ).order_by('dataczasprodukcji')
    # start_date = '2023-04-27 08:00:00'
    # end_date = '2023-04-28 07:59:59'
    # rows = Blockstorage.objects.filter(dataczasprodukcji__gte=start_date,
    #                                    dataczasprodukcji__lte=end_date,
    #                                    kodkreskowy__startswith=forming,
    #                                    ).order_by('dataczasprodukcji')
    return rows


def get_query_group_by_typbloku(forming: str, date_query: str):
    start_date = date_query + ' 08:00'
    end_date = str((dt.datetime.strptime(date_query, "%Y-%m-%d") + dt.timedelta(days=1)).strftime("%Y-%m-%d")) + ' 07:59'
    rows = Blockstorage.objects.filter(dataczasprodukcji__range=(start_date, end_date),
                                       kodkreskowy__startswith=forming,
                                       ).values('typbloku').annotate(count=Count('typbloku')).order_by('typbloku')
    return rows


def get_query_total_count_blocks(forming: str, date_query: str):
    start_date = date_query + ' 08:00'
    end_date = str((dt.datetime.strptime(date_query, "%Y-%m-%d") + dt.timedelta(days=1)).strftime("%Y-%m-%d")) + ' 07:59'
    rows = Blockstorage.objects.filter(dataczasprodukcji__range=(start_date, end_date),
                                       kodkreskowy__startswith=forming,
                                       ).aggregate(total_count=Count('typbloku'))
    return rows
