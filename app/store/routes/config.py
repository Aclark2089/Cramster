from rest_framework import routers
from store.routes.viewsets import *

StoreApiRouter = routers.DefaultRouter()
StoreApiRouter.register(r'users', UserDetail)
StoreApiRouter.register(r'products', ProductDetail)
StoreApiRouter.register(r'orders', OrderDetail)
StoreApiRouter.register(r'suppliers', SupplierDetail)
