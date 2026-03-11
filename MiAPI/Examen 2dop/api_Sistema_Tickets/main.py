from fastapi import FastAPI, status, HTTPExceptions, Depends 
from pydantic import BaseModel 
import asyncio
from pydantic import BaseModel, Field 
from fastapi.security import HTTPBasic,  HTTPBasicCredentials
import secrets


app = FastAPI(
    title= "Sistema de tickets de soporte técnico"
)


# BD FICTICIA 

usuarios = [
    {"id:": 1, "Nombre": "Jorge",},
    {"id": 2, "Nombre": "pablo"},
    {"id:": 3, "Nombre": "Juan"},
    {"id": 4, "Nombre": "pepe"},   
]

ticket = [
    {"id:": 5, "Estado": "Pendiente","Prioridad": "Alta,baja,media"},
    {"id": 6, "Estado": "Pendiente","Prioridad": "Alta,baja,media"},
    {"id:": 7, "Estado": "Pendiente","Prioridad": "Alta,baja,media"},
    {"id": 8, "Estado": "pendiente","Prioridad": "Alta,baja,media"},   
]




#ENDPOINTS

class usuario_create(BaseModel):
    id: int = Field (...,gt=0, description= "identificador de usuario")
    nombre:str = Field (...,min_length=5, description= "nombre de usuario")
    descripcion:str = Field (...,min_length=26, max_length=200, description="descripcion del problema")
 
class ticket_create(BaseModel):
     id: int = Field (...,gt=0, description= "identificador de ticket")
     estado: str = Field (..., gt=0, description= "estado del ticket ")
     prioridad: str = Field (...,gt=0, description=  "prioridad del ticket ")


security = HTTPBasic()
#endpoint protegido 
def verificar_Peticion(credenciales: HTTPBasicCredentials = Depends(security)): 
     userAuth = secrets.compare_digest(credenciales.username, "soporte")
     passAuth = secrets.compare_digest(credenciales.password, "4321")
    
     if not(userAuth and passAuth):
      raise HTTPExceptions(
          status_code=status.HTTP_401_UNAUTHORIZED,
          detail="credenciales no autorizadas"
     )

     return credenciales.username

#endpoint para confirmar que sirve 



@app.get("/v1/ticket/", tags=["CRUD HTTP"])
async def leer_ticket():
     


@app.post("/v1/ticket/", tags=["CRUD HTTP"])
async def crear_ticket(ticket: ticket_create): 
     for tk in ticket :
          if tk["id"] == 