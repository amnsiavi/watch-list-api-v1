from django.urls import path
from watch_list.api.views import WatchListAV, WatchListDetailsAv, StreamPlatformListAv, StreamplatformDetailsAv, ReviewList, ReviewDetails



urlpatterns = [
    # WatchList Url Patterns
    path('list/',WatchListAV.as_view(),name='watch-list-all'),
    path('<int:pk>/',WatchListDetailsAv.as_view(),name='watch-list-details'),
    
    # StreamPlatform URL Patterns
    path('stream-platform/list',StreamPlatformListAv.as_view(),name='streamplatform-list'),
    path('stream-platform/<int:pk>',StreamplatformDetailsAv.as_view(),name='stream-platform-detail'),
    
    
    #Review List Paths
    path('reviews/list',ReviewList.as_view(),name='review-list'),
    path('reviews/<int:pk>', ReviewDetails.as_view(),name='review-detail')
    
]
