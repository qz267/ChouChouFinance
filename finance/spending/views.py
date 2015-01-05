from django.http import HttpResponse
from django.shortcuts import render
from spending.models import SpendingRecords


def list_spending(request):
    spending_list = SpendingRecords.objects.all()
    return render(
        request,
        'spending_list.html',
        {'spending_records_list': spending_list}
    )


def new_spending(request):
    return render(
        request,
        'spending_new.html',
    )


def add_spending(request):
    # and 'spending_amount' in request.GET and 'spending_category_id' in request.GET and 'spending_note' in request.GET
    if 'spending_date' in request.GET:
        spending_date = request.GET['spending_date']
        return render(
            request,
            'spending_add.html',
            {'spending_date': spending_date,}
        )


def edit_spending(request):
    pass


def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        sp_records = SpendingRecords.objects.filter(spending_amount=q)
        return render(
            request,
            'search_results.html',
            {'spending_records': sp_records, 'query': q}
        )
    else:
        return HttpResponse('Please submit a search term.')


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append(('<tr><td>%s</td><td>%s</td></tr>' % (k, v)).encode('utf-8'))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
