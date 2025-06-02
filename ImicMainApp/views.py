# pages/views.py

from django.http import HttpResponse

def home_page_view(request):
    """
    リクエストを受け取り、簡単なHTMLメッセージを含むHTTPレスポンスを返す関数
    """
    return HttpResponse("<h1>Pages App Home</h1><p>これはPagesアプリケーションのトップページです。</p>")