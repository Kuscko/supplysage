# supplysage/inventory/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from .models import Item
from .forms import ItemForm
import csv
from django.http import HttpResponse

# Create your views here.
@login_required
def item_list_view(request):
    query = request.GET.get('q')
    category_filter = request.GET.get('category')

    items = Item.objects.all()

    if query:
        items = items.filter(name__icontains=query)

    if category_filter and category_filter != 'ALL':
        items = items.filter(category=category_filter)

    # Total inventory value (qty × price per item)
    item_value = ExpressionWrapper(F('quantity') * F('price'), output_field=DecimalField())
    total_value = items.annotate(total=item_value).aggregate(sum=Sum('total'))['sum'] or 0

    categories = Item.CATEGORY_CHOICES
    return render(request, 'inventory/item_list.html', {
        'items': items,
        'categories': categories,
        'selected_category': category_filter,
        'query': query,
        'total_value': total_value,
    })


@login_required
def item_create_view(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # Go back to list after creating
    else:
        form = ItemForm()
    return render(request, 'inventory/item_form.html', {'form': form})

@login_required
def item_update_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'inventory/item_form.html', {'form': form, 'item': item})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def item_delete_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'inventory/item_confirm_delete.html', {'item': item})

@login_required
def export_inventory_csv(request):
    items = Item.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="inventory.csv"'
    writer = csv.writer(response)

    writer.writerow(['Name', 'Quantity', 'Price', 'Total Value'])
    total = 0

    for item in items:
        total_value = item.get_total_value()
        total += total_value
        writer.writerow([item.name, item.quantity, item.price, f"{total_value:.2f}"])

    writer.writerow([])
    writer.writerow(['', '', 'Total Inventory Value', f"{total:.2f}"])

    return response
