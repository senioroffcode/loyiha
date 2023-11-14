from django.contrib import admin

urlpatterns = [
    path('get_home/', name="get_home"),
    path('create_order/', name="create_order"),
    path('get_ads/', name="get_ads"),
    path('get_product/', name="get_product"),
    path('get_prod/', name="get_prod"),
    path('get_company/', name="get_company"),
    path('get_question/', name="get_question"),
    path('get_method/', name="get_method"),
    path('get_fact/', name="get_fact"),

]