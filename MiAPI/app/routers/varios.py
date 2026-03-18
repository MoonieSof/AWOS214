from typing import Optional
import asyncio
from app.data.database import usuarios
from fastapi import APIRouter

router= APIRouter(tags=['Varios'])

@router.get("/", tags=["Inicio"])
async def bienvenido():
    return {"Mensaje": "Bienvenido a mi API"}


@router.get("/Hola Mundo", tags=["Bienvenida Asincrona"])
async def Hola():

    await asyncio.sleep(7)

    return {"Mensaje": "Bienvenido a mi API"}


@router.get("/v1/usuario/{id}", tags=["Parametro Obligatorio"])
async def consultaUno(id: int):

    return {"Se encontro usuario": id}


@router.get("/v1/usuarios/buscar", tags=["Parametro Opcional"])
async def consultaTodos(id: Optional[int] = None):

   
    if id is not None:

        for usuario in usuarios:

            if usuario["id"] == id:
                return {
                    "mensaje": "usuario encontrado",
                    "usuario": usuario
                }

     
        return {
            "mensaje": "usuario no encontrado",
            "usuario": id
        }

    else:

        return {
            "mensaje": "No se proporcionó id"
        }
