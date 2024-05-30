from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins


# Data Models
from watch_list.models import WatchList, StreamPlatform, Review

# Importting the serializers
from watch_list.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer

#Review Model Views


#Experimental Code
class ReviewListConcrete(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
    

    
class ReviewDetailConcrete(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
    


class ReviewDetails(
 mixins.RetrieveModelMixin,
 generics.GenericAPIView,
 mixins.DestroyModelMixin,
 mixins.UpdateModelMixin    
):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'msg':'Reccord Deleted Successfully'
        },status=status.HTTP_200_OK)
    
    def patch(self,request,*args,**kwargs):
        if len(request.data) == 0:
            return Response({
                'status':'Failed'
            },status=status.HTTP_400_BAD_REQUEST)
        instance = self.get_object()
        serializer = self.get_serializer(instance,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data':serializer.data,
                'status':'success'
            },status=status.HTTP_200_OK)
        else:
            return Response({
                'status':'Failed'
            },status=status.HTTP_400_BAD_REQUEST)

class ReviewList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get(self, request, *args,**kwargs):
        
        reviews = self.list(request,*args,**kwargs)
        return Response({
            'status':'Success',
            'data':reviews.data
            
        },status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':'success',
                'data':serializer.data
            },status=status.HTTP_200_OK)
        else:
            return Response({
                'status':'Failed'
            },status=status.HTTP_400_BAD_REQUEST)
        
    




# Watch List Model Views
class WatchListAV(APIView):
    
    def get(self,request):
        
        try:
            if WatchList.objects.exists():
                
                watch_list = WatchList.objects.all()
                serialized = WatchListSerializer(watch_list,many=True)
                return Response({
                    'data':serialized.data
                },status=status.HTTP_200_OK)
            else:
                return Response({
                    'error':'Models Does Not Exist'
                },status=status.HTTP_204_NO_CONTENT)
                
                
        except:
            return Response({
                'Error':"Server Error"
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        
        try:
            if len(request.data) == 0:
                return Response({
                    'error':'No Data Provided'
                },status=status.HTTP_400_BAD_REQUEST)
            else:
                serialized = WatchListSerializer(data=request.data)
                if serialized.is_valid():
                    serialized.save()
                    return Response({
                        'data':serialized.data
                    },status=status.HTTP_200_OK)
                else:
                    return Response({
                        'error':'Invalid Format'
                    },status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({
                'errors':'Server Not Responding'
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class WatchListDetailsAv(APIView):
    
    def get(self,request,pk):
        
        try:
            if WatchList.objects.filter(pk=pk).exists():
                watch_list = WatchList.objects.get(pk=pk)
                serialized = WatchListSerializer(watch_list)
                return Response(serialized.data,status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self,request,pk):
        try:
            if WatchList.objects.filter(pk=pk).exists():
                watch_list = WatchList.objects.get(pk=pk)
                watch_list.delete()
                return Response({
                    'msg':'Deleted Successfully'
                },status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
          
   
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self,request,pk):
        
        try:
            if WatchList.objects.filter(pk=pk).exists():
                if len(request.data) == 0:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    watch_list = WatchList.objects.get(pk=pk)
                    serialized = WatchListSerializer(watch_list,data=request.data)
                    if serialized.is_valid():
                        serialized.save()
                        return Response({
                            'data':serialized.data,
                            'msg':'Updated Successfully'
                        },status=status.HTTP_200_OK)
                    else:
                        return Response({
                            'msg':'Update Failed'
                        },status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        
        try:
            if WatchList.objects.filter(pk=pk).exists():
                if len(request.data) == 0:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    watch_list = WatchList.objects.get(pk=pk)
                    serialized = WatchListSerializer(watch_list,data=request.data,partial=True)
                    if serialized.is_valid():
                        serialized.save()
                        return Response({
                            'data':serialized.data,
                            'msg':'Updated Successfully'
                        },status=status.HTTP_200_OK)
                    else:
                        return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
#StreamPlatform VIEWS
class StreamPlatformListAv(APIView):
    
    def get(self, request):
        
        try:
            if StreamPlatform.objects.exists():
                stream_platforms = StreamPlatform.objects.all()
                serialized = StreamPlatformSerializer(stream_platforms,many=True)
                return Response(serialized.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT) 
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self,request):
        
        try:
            if len(request.data) == 0:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                serialized = StreamPlatformSerializer(data=request.data)
                if serialized.is_valid():
                    serialized.save()
                    return Response(serialized.data,status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR) 


class StreamplatformDetailsAv(APIView):
    
    def get(self,request,pk):
        
        try:
            if StreamPlatform.objects.filter(pk=pk).exists():
                stream_platform = StreamPlatform.objects.get(pk=pk)
                serialized = StreamPlatformSerializer(stream_platform)
                return Response(serialized.data,status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self,request,pk):
        
        try:
            if StreamPlatform.objects.filter(pk=pk).exists():
                stream_platform = StreamPlatform.objects.get(pk=pk)
                stream_platform.delete()
                return Response({
                    'msg':'Deleted Successfully'
                },status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self,request,pk):
        
        try:
            if StreamPlatform.objects.filter(pk=pk).exists():
                if len(request.data) == 0:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    stream_platform = StreamPlatform.objects.get(pk=pk)
                    serialized = StreamPlatformSerializer(stream_platform,data=request.data)
                    if serialized.is_valid():
                        serialized.save()
                        return Response({
                            'data':serialized.data
                        },status=status.HTTP_200_OK)
                    else:
                        return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
              
        try:
            if StreamPlatform.objects.filter(pk=pk).exists():
                if len(request.data) == 0:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    stream_platform = StreamPlatform.objects.get(pk=pk)
                    serialized = StreamPlatformSerializer(stream_platform,data=request.data,partial=True)
                    if serialized.is_valid():
                        serialized.save()
                        return Response({
                            'data':serialized.data,
                            'msg':'Updated Successfully'
                        },status=status.HTTP_200_OK)
                    else:
                        return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    