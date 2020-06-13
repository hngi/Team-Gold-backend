"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_swagger_view(title="Subscriber API Documentation")
schema_view = get_schema_view(
    openapi.Info(
        title="Subscribers Api",
        default_version="v1",
        description="""Our API allows subscriptions to a saas app. We store user details, their plans, current subscriptions and all transactions. How To: 
        1. All GET requests are to get information(retrieve what has been previously stored). 
        2 all POST are to add information(create new users, transactions etc.) 
        3. All upt requests are to update stored data 
        4. Patch is to overwrite. 
        5. Delete deletes all stored data.
        E.g subscription.microapi.dev/api/plan/11/delete will delete a plan with the id 11.
        {ID} parameters relate to the id of a particular object. Every list, user, transaction and subscriptions are given ids. Use this to access them. Please note that two models can have the same id, since they exist as separate entities.
               To return data as json, please add /v1.json to the url. It also supports yaml.
               Also, a much more sophisticated doc is available by appending /redoc/. Thanks for using our microservice""",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path("docs/v1/", schema_view),
    path("admin/", admin.site.urls),
    path("api/v1/", include("base.urls", namespace="v1")),
    path("api-auth/", include("rest_framework.urls")),
]
urlpatterns += [
    re_path(
        r"^v1(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    path("rest-auth/", include("rest_auth.urls")),
]
