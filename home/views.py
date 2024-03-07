from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import TodoSerializer
from rest_framework import status
from .models import TodoModel
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.paginator import Paginator
# Create your views here.

class BlogView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self,request):
        try:
            data = request.data
            data['user']=request.user.id
            serializer = TodoSerializer(data=data)

            if not serializer.is_valid():

                if not serializer.is_valid():
                    return Response({

                        "data":serializer.errors,
                        "message":"validation error"

                    },status=status.HTTP_400_BAD_REQUEST)
                
            serializer.save()

            return Response({

                        "data":serializer.data,
                        "message":"Todo work added successfully"

                    },status=status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
            return Response({

                        "data":{},
                        "message":"something went wrong"

                    },status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request):

        try:
            todos = TodoModel.objects.filter(user = request.user)
            
            if request.GET.get('search'):
                search = request.GET.get('search')
                todos = todos.filter(title__icontains=search)

            page_naumber = request.GET.get('page',1)
            paginator=  Paginator(todos,1)

            serializer = TodoSerializer(paginator.page(page_naumber),many=True)

            return Response({

                "data":serializer.data,
                "message":"Your blogs fetched successfully"

            },status=status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response({

                    "data":{},
                    "message":"something went wrong"

                },status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request):

        try:
             
            data = request.data
            todo = TodoModel.objects.filter(uid=data['uid'])

            if not todo.exists():
                    return Response({

                        "data":{},
                        "message":"no such task exist"

                    },status=status.HTTP_204_NO_CONTENT)
            
            serializer = TodoSerializer(todo[0],data=data,partial=True)

            if not serializer.is_valid():
                    return Response({

                        "data":serializer.errors,
                        "message":"validation error"

                    },status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()

            return Response({

                    "data":serializer.data,
                    "message":"Your todo updated successfully"

                },status=status.HTTP_200_OK)
        
        except Exception as e:
             print(e)
             return Response({

                    "data":{},
                    "message":"something went wrong"

                },status=status.HTTP_400_BAD_REQUEST)
        
         
    def delete(self,request):
            
        try:
            data = request.data
            todo = TodoModel.objects.filter(uid=data.get('uid'))

            if not todo.exists():
                    return Response({

                    "data":{},
                    "message":"no such blog uid"

                },status=status.HTTP_204_NO_CONTENT)
            
            todo.delete()

            return Response({

                    "data":{},
                    "message":"deleted successfully"

                },status=status.HTTP_200_OK)

        except Exception as e:
            
             return Response({

                    "data":{},
                    "message":"something went wrong"

                },status=status.HTTP_400_BAD_REQUEST)
                    
    