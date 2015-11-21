from rest_framework import routers
from store.routes.viewsets import *

StoreApiRouter = routers.DefaultRouter()
StoreApiRouter.register(r'users', UserViewSet)
StoreApiRouter.register(r'products', ProductViewSet)
StoreApiRouter.register(r'orders', OrderViewSet)
StoreApiRouter.register(r'suppliers', SupplierViewSet)
StoreApiRouter.register(r'productorders', ProductOrderViewSet)
