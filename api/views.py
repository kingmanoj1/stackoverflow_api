from http import HTTPStatus
from ratelimit.decorators import ratelimit

from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.cache import cache_page

from api.service import GetStackOverflow

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
@ratelimit(key='ip', rate='1/h')
@ratelimit(key='ip', rate='100/d')
def get_all_question(request):
    was_limited = getattr(request, 'limited', False)
    if was_limited:
        return JsonResponse({"error": 'limit crossed'},
                            status=HTTPStatus.BAD_REQUEST)
    stackoverflow = GetStackOverflow()
    res = stackoverflow.get_all_questions(request)
    return JsonResponse(res)


@ratelimit(key='ip', rate='5/m')
@ratelimit(key='ip', rate='100/d')
@cache_page(CACHE_TTL)
def answer_search(request, qid):
    was_limited = getattr(request, 'limited', False)
    if was_limited:
        return JsonResponse({"error": 'limit crossed'},
                            status=HTTPStatus.BAD_REQUEST)
    stackoverflow = GetStackOverflow()
    res = stackoverflow.answer_search(qid)
    return JsonResponse(res)


@cache_page(CACHE_TTL)
@ratelimit(key='ip', rate='1/h')
@ratelimit(key='ip', rate='100/d')
def get_all_article(request):
    was_limited = getattr(request, 'limited', False)
    if was_limited:
        return JsonResponse({"error": 'limit crossed'},
                            status=HTTPStatus.BAD_REQUEST)
    stackoverflow = GetStackOverflow()
    res = stackoverflow.get_all_articles(request)
    return JsonResponse(res)


@ratelimit(key='ip', rate='5/m')
@ratelimit(key='ip', rate='100/d')
@cache_page(CACHE_TTL)
def article_search(request, aid):
    was_limited = getattr(request, 'limited', False)
    if was_limited:
        return JsonResponse({"error": 'limit crossed'},
                            status=HTTPStatus.BAD_REQUEST)
    stackoverflow = GetStackOverflow()
    res = stackoverflow.article_search(aid)
    return JsonResponse(res)
