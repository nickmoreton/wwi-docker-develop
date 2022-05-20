from pages.models import Category, PostPage

try:
    from wagtail.models import Page
except ImportError:
    from wagtail.core.models import Page


class HomePage(Page):
    def get_context(self, request):
        ctx = super().get_context(request)
        if request.GET.get("cat"):
            posts = PostPage.objects.live().filter(
                categories__id=request.GET.get("cat")
            )
            # ctx["limit"] = "20"
        else:
            posts = PostPage.objects.live()
            # ctx["limit"] = "50"
        categories = Category.objects.all()
        ctx["posts"] = posts
        ctx["categories"] = categories

        return ctx
