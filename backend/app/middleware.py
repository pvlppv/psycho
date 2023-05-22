from fastapi import Request
from fastapi.responses import RedirectResponse

async def locale(request: Request, call_next):
    accept_language = request.headers.get('accept-language')
    if accept_language and 'ru' in accept_language.lower():
        request.state.locale = 'ru'
    else:
        request.state.locale = 'en'

    if request.url.path == '/':
        new_url = f'/{request.state.locale}'
        return RedirectResponse(url=new_url)

    skip_prefix = ['/en', '/ru', '/admin', '/docs', '/redoc', '/openapi.json']
    if not any(request.url.path.startswith(prefix) for prefix in skip_prefix):
        new_url = f'/{request.state.locale}{request.url.path}'
        return RedirectResponse(url=new_url)

    response = await call_next(request)
    return response

