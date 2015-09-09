"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

YOUR_INFO = {
    'name' : 'Geoffrey Sechter',
    'bio' : 'Django NYC co-organizer, Django Girls Support team',
    'email' : 'geoffrey.sechter@gmail.com', # Leave blank if you'd prefer not to share your email with other conference attendees
    'twitter_username' : 'gsechter', # No @ symbol, just the handle.
    'github_username' : "lightstrike", 
    'headshot_url' : 'https://pbs.twimg.com/profile_images/593959225149140992/_oEj27YJ_400x400.jpg', # Link to your GitHub, Twitter, or Gravatar profile image.
}
    
def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/base.html',
        context_instance = RequestContext(request,
            {
                'attendee' : YOUR_INFO,    
                'year': datetime.now().year,
            })
    )
