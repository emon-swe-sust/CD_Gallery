from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def apiOverview(request):
    api_urls = {
        'API Overview'                      : 'api/v1/',

        'User Login'                        : 'api/v1/accounts/login/',
        'User Logout'                       : 'api/v1/accounts/logout/',
        'User Details'                      : 'api/v1/accounts/user/',
        'User Registration'                 : 'api/v1/accounts/registration/',

        'Customer List, Create'             : 'api/v1/customers/list_create/',
        'Customer Update, Delete'           : 'api/v1/customers/update_delete/',

        'Category List, Create'             : 'api/v1/Categories/list_create/',
        'Category Update, Delete'           : 'api/v1/Categories/update_delete/',
	}

    return Response(api_urls)
    