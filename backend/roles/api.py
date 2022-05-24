from typing import List
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Body, Path, Router

from .schemas import RolOut, RolIn
from .models import RolModel

router = Router()

@router.get('/', response=List[RolOut])
def list_roles(request: HttpRequest):
    q_rol = RolModel.objects.all()
    return q_rol

@router.post('/', response=RolOut)
def create_rol(request: HttpRequest, payload: RolIn = Body(...)):
    q_rol = RolModel.objects.create(**payload.dict())
    q_rol.save()
    return q_rol

@router.put('/{id}', response=RolOut)
def update_rol(request: HttpRequest, payload: RolIn = Body(...), id: int = Path(...)):
    q_rol = get_object_or_404(RolModel, pk=id)
    q_rol.rol = payload.rol
    q_rol.save()
    return q_rol

@router.delete('/{id}')
def delete_rol(request: HttpRequest, id: int = Path(...)):
    q_rol = get_object_or_404(RolModel, id=id)
    q_rol.delete()
    return { 'success': True }