from .models import Category


def menulinks(request):
    allcats=Category.objects.all()
    return dict(allcats=allcats)