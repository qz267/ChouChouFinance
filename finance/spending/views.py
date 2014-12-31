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
    # add_item = SpendingRecords()
    # content = request.POST['content']
    # add_item.spending_date = content['date']
    # add_item.spending_amount = content['spending_amount']
    # add_item.spending_note = content['spending_note']
    # add_item.spending_category_id = content['spending_category_id']
    # add_item.save()
    return render(
        request,
        'spending_new.html',
        # {
        #     'content': content,
        # }
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


def add_spending_success(request):
    pass