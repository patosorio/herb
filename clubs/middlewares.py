from django.http import HttpResponseForbidden
from .models import Club

class TierAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                club = Club.objects.get(owner=request.user)
                required_feature = self.url_to_required_feature(request.path)
                
                if required_feature and not club.has_feature(required_feature):
                    return HttpResponseForbidden("You don't have access to this feature.")
                
            except Club.DoesNotExist:
                pass  # If no club exists for this user, proceed normally
        
        return self.get_response(request)

    def url_to_required_feature(self, path):
        mapping = {
            '/members/view/': 'VIEW_MEMBERS',
            '/members/add/': 'ADD_MEMBERS',
            '/members/manage/': 'MEMBERS_MANAGEMENT',
            '/accounting/': 'ACCOUNTING',
            '/inventory/weed/': 'WEED_INVENTORY',
            '/inventory/bar/': 'BAR_INVENTORY',
            '/analytics/': 'ANALYTICS',
            # ... add more paths as per your URL structure
        }
        return mapping.get(path)
