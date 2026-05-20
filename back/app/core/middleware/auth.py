from fastapi import Request
from app.core.security import decode_token

async def auth_middleware(request: Request, call_next):

    token = request.headers.get("Authorization")

    if token:
        try:
            decode_token(token.replace("Bearer ", ""))
        except:
            pass  # ou bloquear dependendo da regra

    return await call_next(request)