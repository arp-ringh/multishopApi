from apps.product.models import Category, Subcategory


def bulk_categories(request):
    categories = Category.objects.all()[0:8]

    return {'bulk_categories': categories}


def bulk_subcategories(request):
    subcategories = Subcategory.objects.all()[0:4]

    return {'bulk_subcategories': subcategories}
