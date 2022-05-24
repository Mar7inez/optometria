from typing import List
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Body, Path, Router

from genders.models import GenderModel

from .schemas import PatientIn, PatientOut
from .models import PatientModel

router = Router()

@router.get('/', response=List[PatientOut])
def list_patients(request: HttpRequest):
    q_patient = PatientModel.objects.all()
    return q_patient

@router.post('/', response=PatientOut)
def create_patient(request: HttpRequest, payload: PatientIn = Body(...)):
    gender_id = payload.gender
    gender = get_object_or_404(GenderModel, pk=gender_id)

    obj = payload.dict()
    obj["gender"] = gender
    q_patient = PatientModel.objects.create(**obj)
    q_patient.save()
    return q_patient

@router.put('/{id}', response=PatientOut)
def update_patient(request: HttpRequest, payload: PatientIn = Body(...), id: int = Path(...)):
    q_patient = get_object_or_404(PatientModel, pk=id)
    for key, value in payload.dict().items():
        if key == "gender":
            gender_id = payload.gender
            gender = get_object_or_404(GenderModel, pk=gender_id)
            setattr(q_patient, key, gender)
        else:    
            setattr(q_patient, key, value)
    q_patient.save()
    return q_patient

@router.delete('/{id}')
def delete_patient(request: HttpRequest, id: int = Path(...)):
    q_rol = get_object_or_404(PatientModel, pk=id)
    q_rol.delete()
    return { 'success': True }