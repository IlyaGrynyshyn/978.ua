from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from cart.cart import Cart
from cart.views import cart_detail
from specs.models import ProductFeatures
from .models import *
from main_slider.models import Slider

class BaseListView(ListView):
    model = Product
    template_name = "mainapp/base.html"
    context_object_name = 'products'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['top_sale'] = Product.objects.all()[:12]
        context['cart'] = Cart(self.request)
        context['sliders'] = Slider.objects.all()
        return context


def search_page(request):
    if 'q' in request.GET:
        q = request.GET.get('q')
        categories = Category.objects.all()
        data = Product.objects.filter(title__contains=q)
    context = {
        'products': data,
        'categories': categories
    }
    return render(request, 'mainapp/product-category.html', context)


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def search(request):
    if is_ajax(request=request):
        product = request.POST.get('product')
        res = None
        qs = Product.objects.filter(title__icontains=product)
        if len(qs) > 0 and len(product) > 0:
            data = []
            for pos in qs:
                item = {
                    'url': pos.get_absolute_url(),
                    'title': pos.title,
                    'price': pos.price,
                    'img': str(pos.img.url)
                }

                data.append(item)

            res = data
        else:
            res = 'За вашим запитом нічого не знайдено...'
        return JsonResponse({'data': res})
    return JsonResponse({})


# class CategoryDetailView(ListView):
#     model = Product
#     template_name = 'mainapp/category-list.html'
#     context_object_name = 'products'
#     paginate_by = 2
#     slug_url_kwarg = 'category_slug'
#
#     def get_queryset(self):
#         return Product.objects.filter(category__slug=self.kwargs['category_slug'])
#
#     def get_context_data(self, **kwargs):
#         content = super().get_context_data(**kwargs)
#         content['cart'] = cart_detail
#         content['categories'] = Category.objects.all()
#         # content['products'] = Product.objects.all()
#         return content
from django.views.generic.list import MultipleObjectMixin


class CategoryDetailView(DetailView, MultipleObjectMixin):
    model = Category
    paginate_by = 2
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'mainapp/category-list.html'
    slug_url_kwarg = 'category_slug'

    def get_context_data(self, **kwargs):
        object_list = Product.objects.filter(category__slug=self.kwargs['category_slug'])
        context = super().get_context_data(object_list=object_list, **kwargs)
        query = self.request.GET.get('search')
        category = self.get_object()
        # context['products'] = Product.objects.filter(category__slug=self.kwargs['category_slug'])
        context['categories'] = self.model.objects.all()
        context['cart'] = Cart(self.request)
        if not query and not self.request.GET:
            context['category_products'] = category.product_set.all()
            return context
        if query:
            products = category.product_set.filter(Q(title__icontains=query))
            context['category_products'] = products
            return context
        url_kwargs = {}
        for item in self.request.GET:
            if len(self.request.GET.getlist(item)) > 1:
                url_kwargs[item] = self.request.GET.getlist(item)
            else:
                url_kwargs[item] = self.request.GET.get(item)
        q_condition_queries = Q()
        for key, value in url_kwargs.items():
            if isinstance(value, list):
                q_condition_queries.add(Q(**{'value__in': value}), Q.OR)
            else:
                q_condition_queries.add(Q(**{'value': value}), Q.OR)
        pf = ProductFeatures.objects.filter(
            q_condition_queries
        ).prefetch_related('product', 'feature').values('product_id')
        products = Product.objects.filter(id__in=[pf_['product_id'] for pf_ in pf])
        context['category_products'] = products
        # pagination
        # activities = self.get_related_activities()
        # context['related_activities'] = activities
        # context['page_obj'] = activities
        return context

    # def get_related_activities(self):
    #     queryset = Product.objects.filter(category__slug=self.kwargs['category_slug'])
    #     paginator = Paginator(queryset, 2)  # paginate_by
    #     page = self.request.GET.get('page')
    #     activities = paginator.get_page(page)
    #     return activities





class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    # template_name = 'mainapp/product_detail.html'
    template_name = 'mainapp/product.html'
    slug_url_kwarg = 'product_slug'
    extra_context = {'title': "Каталог продуктів"}

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.get_object().category.__class__.objects.all()
        context['cart'] = Cart(self.request)
        context['top_sale'] = Product.objects.all()[:12]
        context['images'] = ProductImage.objects.filter(product__slug=self.kwargs['product_slug'])
        return context