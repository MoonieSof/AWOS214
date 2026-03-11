from fastapi import FastAPI, status, HTTPException, Depends 
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
      raise HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED,
          detail="credenciales no autorizadas"
     )

     return credenciales.username

#endpoint para confirmar que sirve mi api 

@app.get("/", tags=["Inicio"])
async def bienvenido():
    return{"Mensaje": "Bienvenido al sisitema de tickets de soporte tecnico "}

#consulta ticket 
@app.get("/v1/ticket/{id}", tags=["Parametro obligatorio"])
async def consultaT(id: int):
    return{"Se encontro el ticket": id}

#crear ticket
@app.post("/v1/ticket/", tags=["CRUD"])
async def crear_ticket(ticket: ticket_create):

    for tckt in ticket:
        if tckt["id"] == ticket.id:

            raise HTTPException(
                status_code=400,
                detail="El id de este ticket ya existe"
            )
    ticket.append(ticket.dict())
    return{
        "mensaje": "ticket agregado",
        "ticket": ticket 
    }
#actualizar endpoint

@app.put("/v1/ticket/{id}", tags=["CRUD"])
async def actualizar_ticket(id: int, estado: dict, prioridad: dict):

    
    ticket["id"] = id
    
    for i in range(len(ticket)):

        if ticket[i]["id"] == id:

            ticket[i] = ticket 

            return {
                "mensaje": "ticket actualizado",
                "ticket": ticket
            }
    






