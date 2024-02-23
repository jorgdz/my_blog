from rest_framework import status
#from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import Post
from posts.api.serialize import PostSerializer
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

class PostModelViewSet(ModelViewSet):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

""" class PostViewSet (ViewSet):

    def list (self, req):
        posts = PostSerializer( Post.objects.all(), many = True )
        return Response( status = status.HTTP_200_OK, data = posts.data )
    
    def retrieve ( self, req, pk: int ):
        post = PostSerializer(Post.objects.get(pk = pk))
        return Response(status=status.HTTP_200_OK, data=post.data)

    def create ( self, req ):        
        serializer = PostSerializer( data = req.POST )

        serializer.is_valid( raise_exception=True)
        serializer.save()

        return Response (status = status.HTTP_200_OK, data = serializer.data) """
    
""" class PostApiView (APIView):

    # Listar los posts
    def get ( self, req ):
        posts = PostSerializer( Post.objects.all(), many = True )
        return Response( status = status.HTTP_200_OK, data = posts.data )
    
    # Crear un nuevo Post
    def post ( self, req ):
        #Post.objects.create( 
            #title = req.POST['title'], 
            #description = req.POST['description'], 
            #order = req.POST['order'] 
        #)
        
        serializer = PostSerializer( data = req.POST )

        serializer.is_valid( raise_exception=True)
        serializer.save()

        return Response (status = status.HTTP_200_OK, data = serializer.data) """