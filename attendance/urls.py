from django.urls import path
from .views import (fingerscan,
                    break_view,
                    checkout_view,
                    user_attend_log,
                    user_attend_search,
                )


urlpatterns = [
    path('fingerscan/', fingerscan, name='fingerscan'),
    path('step/two/', break_view, name='t-break'),
    path('check/out/', checkout_view, name='check-out'),
    path('user/log/', user_attend_log, name='log'),
    path('user/search/', user_attend_search, name='search'),
]