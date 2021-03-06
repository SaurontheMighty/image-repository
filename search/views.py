from django.shortcuts import render

results = [
    {
        'name': "/search/media/sloth_bear.jpg",
        'hash': "0XASKDFJ3IEWUY",
        'description': "An image of a cool sloth bear.",
        'portrait': "false",
        'B/W': "false",
        'Date_created': "Today"
    },
    {
        'name': "/search/media/small_sloth_bear.png",
        'hash': "0XASKDFJ3IEWGY",
        'description': "An image of a small sloth bear.",
        'portrait': "false",
        'B/W': "false",
        'Date_created': "Today"
    }
]

# Create your views here.
def home(request):

    context = {
        'results': results
    }

    return render(request, 'search/home.html', context)