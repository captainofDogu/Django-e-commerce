from product.models import Category


# context_processors olduguna göre artık tüm categorileri alanları iptal ediyoruz
def nav_data(request):
    context =dict()
    context['categories'] = Category.objects.filter(
        status = "published"
    ).order_by('title')
    context['pages'] = Page.objects.filter(
        status=STATUS
    ).order_by('title')
    return context

  