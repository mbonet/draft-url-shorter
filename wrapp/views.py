# -*- coding: utf-8 *-*
import random
import string

from django.shortcuts import render
from django.core.cache import cache
from django.shortcuts import redirect


CACHE_TIMEOUT = 2592000  # 30 days cache


def _generate_short():
    choices = string.ascii_uppercase + string.digits
    return u''.join(random.choice(choices) for i in range(6))


def create_short_to_cache(url):
    key = _generate_short()
    cache.set(key, url, CACHE_TIMEOUT)
    return key


def homepage(request):
    context = {'url': request.POST.get('url', ''), 'short': ''}
    if context['url']:
        short = create_short_to_cache(context['url'])
        context['short'] = "http://wrapp.no-ip.org:9000/wrapp/%s" % short
    return render(request, 'index.html', context)


def resolve(request, key):
    try:
        url = cache.get(key)
        if url and not url.count('http://'):
            url = u'http://'+url
        return redirect(url)
    except:
        return render(request, '404.html')
