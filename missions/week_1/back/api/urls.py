from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path(r'v1/authorization/', include('api.authorization.urls', 'authorization')),
    path(r'v1/user/', include('api.user.urls', 'user')),
    path(r'v1/product/', include('api.product.urls', 'product')),
    path(r'v1/help/', include('api.help.urls', 'help')),
]