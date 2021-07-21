from django.urls import path

from store.views import SimpleView, InstrumentsView, AddInstrument

urlpatterns = [
    path('', InstrumentsView.as_view()),
    path('add_instrument', AddInstrument.as_view())
]
