from django.urls import path, include
from .views import RoomListView, BookingListView, RoomDetailView, CancelBookingView

app_name = 'booking'

urlpatterns = [ 
    path('', RoomListView, name='RoomListView'),
    path('booking_list', BookingListView.as_view(), name='BookingListView'),
    path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking/cancel/<pk>', CancelBookingView.as_view(), 
        name= 'CancelBookingView')
] 