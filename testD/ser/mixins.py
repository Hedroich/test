from .models import News

class LanguageMixin:
    def change_language(self, request):
        return News.objects.filter(lan=request.query_params['lan'])
