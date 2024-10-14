from fastapi import APIRouter

from api.models.responses.message_response import MessageResponse

router = APIRouter(prefix="/ping")

@router.get("")
async def ping() -> MessageResponse:
    return MessageResponse.create("Pong!")