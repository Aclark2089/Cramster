from rest_framework import routers
from store.routes.viewsets import *

StoreApiRouter = routers.DefaultRouter()
StoreApiRouter.register(r'authusers', AuthUserViewSet)
StoreApiRouter.register(r'storeusers', StoreUserViewSet)
StoreApiRouter.register(r'products', ProductViewSet)
StoreApiRouter.register(r'orders', OrderViewSet)
StoreApiRouter.register(r'suppliers', SupplierViewSet)
