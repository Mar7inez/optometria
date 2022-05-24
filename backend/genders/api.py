from typing import List
from django.http import HttpRequest
from ninja import Router

from .schemas import GenderOut, GenderIn
from .models import GenderModel

router = Router()

@router.get('/', response=List[GenderOut])
def list_genders(request: HttpRequest):
    q_gender = GenderModel.objects.all()
    return q_gender

@router.post('/', response=GenderOut)
def create_gender(request: HttpRequest, payload: GenderIn):
    q_gender = GenderModel.objects.create(type=payload.type)
    q_gender.save()
    return q_gender