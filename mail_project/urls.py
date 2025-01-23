from django.contrib import admin
from django.urls import path
from au_app.views import ulogin, ulogout, usignup, uchangepw
from top_news_app.views import topNews
from mail_app.views import home, compose_mail
from calc_app.views import calc
from calendar_app.views import calendar
from weather_app.views import weather

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("topNews/", topNews, name="topNews"),
    path("calc/", calc, name="calc"),
    path("calendar/", calendar, name="calendar"),
    path("weather/", weather, name="weather"),
    path("compose_mail/", compose_mail, name="compose_mail"),
    path("ulogin/", ulogin, name="ulogin"),
    path("ulogout/", ulogout, name="ulogout"),
    path("usignup/", usignup, name="usignup"),
    path("uchangepw/", uchangepw, name="uchangepw"),
]
