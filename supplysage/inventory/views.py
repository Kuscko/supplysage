# supplysage/inventory/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Item
from .forms import ItemForm

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

    categories = Item.CATEGORY_CHOICES
    return render(request, 'inventory/item_list.html', {
        'items': items,
        'categories': categories,
        'selected_category': category_filter,
        'query': query
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
