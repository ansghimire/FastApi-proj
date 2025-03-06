from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.common.exceptions import NotFoundException, UnauthorizedException, ForbiddenException, BadRequestException
from app.common.responses import SuccessResponse