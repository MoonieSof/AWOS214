from fastapi import status, HTTPException, Depends, APIRouter
from app.models.usuario import usuario_create
from app.data.database import usuarios 
from app.security.auth import verificar_Peticion

router = APIRouter(
    prefix="/v1/usuarios", tags=["CRUD HTTP"] #prefijo, es lo que se repite en todos los endpoints "v1
)


@router.get("/", tags=["CRUD HTTP"])
async def leer_usuarios():

    return {
        "status": "200",
        "total": len(usuarios),
        "usuarios": usuarios
    }


# Endpoint para crear un usuario

@router.post("/", tags=["CRUD HTTP"], status_code=status.HTTP_201_CREATED)
async def crear_usuario(usuario: usuario_create): 

    # Se verifica que el ID no exista
    for usr in usuarios:

        if usr["id"] == usuario.id: 

            raise HTTPException(
                status_code=400,
                detail="El id ya existe"
            )

    # Se agrega el usuario a la lista
    usuarios.append(usuario.dict())

    return {
        "mensaje": "Usuario agregado",
        "Usuario": usuario
    }


# Endpoint para actualizar un usuario

@router.put("/{id}", tags=["CRUD HTTP"])
async def actualizar_usuario(id: int, usuario: dict):

    # Se asegura que el ID del body sea el mismo que el de la URL
    usuario["id"] = id
    
    for i in range(len(usuarios)):

        if usuarios[i]["id"] == id:

            usuarios[i] = usuario

            return {
                "mensaje": "Usuario actualizado",
                "Usuario": usuario
            }
    
    # si no se encuentra el usuario
    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )


# Endpoint para eliminar usuario


@router.delete("/{id}", tags=['CRUD HTTP'], status_code=status.HTTP_200_OK)
async def eliminar_usuario(id:int, userAuth:str= Depends(verificar_Peticion)):

    # Se busca el usuario por ID
    for index, usuario in enumerate(usuarios):

        if usuario["id"] == id:

            usuarios.pop(index)

            return{
                "messege":f"Usuario eliminado por: {userAuth}"
            }

    # si no existe
    raise HTTPException(
        status_code=400, 
        detail="Usuario no encontrado"
    )