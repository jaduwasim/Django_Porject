from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from testapp.serializers import UserRegistrationSerilizer, UserLoginSerializer
from django.contrib.auth import authenticate
from testapp.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken


# Generate Token Manually.
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistration(APIView):
    renderer_classes = [UserRenderer,]
    def post(self, request, format=None):
        serializer = UserRegistrationSerilizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'msg':'Registration Succesfull', 'token':token}, status=status.HTTP_201_CREATED)
        return Response({'msg':'Restration Succes!!'}, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    renderer_classes = [UserRenderer,]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)  
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            token = get_tokens_for_user(user)
            if user is not None:
                return Response({'msg':'Login Success', 'token':token}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)