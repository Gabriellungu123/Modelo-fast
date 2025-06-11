# Lo que tiene que tener el main 
from typing import Union
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
#Para añadir la carpeta data
from data.modelo.menu import Menu
from data.dao.dao_pcs import DaoPcs
from typing import Annotated
from data.database import database




#Para que funcione el Fastapi los css y los html
app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")
templates = Jinja2Templates(directory="templates")



#Pagina por defecto 
@app.get("/")
def read_root(request: Request): #- Recibe un parámetro request de tipo Request, que representa la solicitud HTTP del usuario
    menu = Menu(True, True) #Garantiza que las opciones del menu sean activas
    pcs = DaoPcs().get_all(database) # Se obtiene la lista de pcs desde la base de datos usando
    return templates.TemplateResponse( #- Se devuelve una respuesta renderizada con una plantilla HTML usando 
        request= request, #Se pasa la solicitud HTTP a la plantilla.
        name="default.html", #- Se indica que la plantilla a renderizar es "default.html".
        context={"menu": menu,"pcs": pcs} #- : Se envían variables a la plantilla, permitiendo que menu y pcs sean utilizados dentro de "default.html".
          )

#Pagina principal
@app.get("/database") #- Define una ruta HTTP GET en FastAPI #- Cuando un usuario accede a "/database", se ejecutará la función get_pcs
def get_pcs(request: Request): #maneja las solicitudes a /database, - Recibe un parámetro request de tipo Request, que representa la solicitud HTTP del usuario.
    menu = Menu(True, True)#Garantiza que las opciones del menu sean activas
    pcs = DaoPcs().get_all(database) #Se obtiene la lista de pcs desde la base de datos usando
    return templates.TemplateResponse( #Se devuelve una respuesta renderizada con una plantilla HTML usando
        request=request,#Se pasa la solicitud HTTP a la plantilla.
        name="database.html", #- Se indica que la plantilla a renderizar es "default.html".
        context={"menu": menu,"pcs": pcs} #- : Se envían variables a la plantilla, permitiendo que menu y pcs sean utilizados dentro de "database.html".
    )

##################   Añadir Pcs  ##################
@app.get("/formaddpcs") #Define una ruta HTTP GET en FastAPI #- Cuando un usuario accede a "/formaddpcs", se ejecutará la función form_add_pcs
def form_add_pcs(request: Request): #maneja las solicitudes a /formaddpcs, - Recibe un parámetro request de tipo Request, que representa la solicitud HTTP del usuario.
    menu = Menu(True, True) # Activa las opciones del menú
    pcs = DaoPcs().get_all(database) # Obtiene la lista de PCs desde la base de datos
    return templates.TemplateResponse( # Devuelve la plantilla del formulario
        request=request, #Se pasa la solicitud HTTP a la plantilla.
        name="formaddpcs.html", #- Se indica que la plantilla a renderizar es "formaddpcs.html".
        context={"menu": menu, "pcs": pcs} #- : Se envían variables a la plantilla, permitiendo que menu y pcs sean utilizados dentro de "formaddpcs.html".
    )

@app.post("/addpcs")
def add_pcs( #- Se define una función llamada add_alumnos, que se ejecutará cuando alguien envíe datos a "/addpcs".
    request: Request, # Representa la solicitud del usuario (como el formulario que envió).
    marca: Annotated[str, Form()], #-  Indica que el usuario enviará una marca en el formulario.
    tipo: Annotated[int, Form()],   #-  Indica que el usuario enviará un tipo en el formulario.
    sistema: Annotated[str, Form()], #-  Indica que el usuario enviará un sistema en el formulario.
    procesador: Annotated[str, Form()] #-  Indica que el usuario enviará un procesador en el formulario.
):
    dao = DaoPcs() #-  Se crea un objeto de la clase DaoPcs que maneja la base de datos.
    dao.insert(database, marca, tipo, sistema, procesador) #-  Se llama a la función insert para guardar el pc en la base de datos.

    pcs = dao.get_all(database) #- Después de agregar el nuevo pc, se obtiene la lista completa de pcs desde la base de datos. - dao.get_all(database) → Recupera todos los pcs guardados.
    menu = Menu(True, True)
    return templates.TemplateResponse(#Se devuelve una respuesta renderizada con una plantilla HTML usando
        request=request, #Se pasa la solicitud HTTP a la plantilla.
        name="addpcs.html", #- Se indica que la plantilla a renderizar es "addpcs.html".
         context={"menu": menu, "pcs": pcs} #Se envían variables a la plantilla, permitiendo que menu y pcs sean utilizados dentro de "addpcs.html".
    )
    
  ################## ELIMINAR ALUMNOS ##############################


@app.get("/fromdelpcs") # Muestra el formulario para eliminar PCs
def form_del_pcs(request: Request):
    menu = Menu(True, True)# Activa las opciones del menú
    dao = DaoPcs() # Crea un objeto de la clase DaoPcs
    pcs = dao.get_all(database) # Obtiene la lista de PCs desde la base de datos
    return templates.TemplateResponse(
        request=request,
        name="formdelpc.html",
        context={"menu": menu, "pcs": pcs}
    )

@app.post("/delpcs") # Procesa el formulario para eliminar PCs
def del_pcs(request: Request, pc_marca: Annotated[str, Form()]): # Recibe la marca del PC a eliminar
    dao = DaoPcs() # Crea un objeto de la clase DaoPcs
    dao.delete(database, pc_marca) ## Elimina el PC de la base de datos
    pcs = dao.get_all(database)
    menu = Menu(True, True)
    return templates.TemplateResponse(
        request=request,
        name="delpcs.html",
        context={"menu": menu, "pcs": pcs}
    )

############## ACTUALIZAR #########################


@app.get("/formupdatesistema")
def form_update_sistema(request: Request): # Representa la solicitud del usuario.
    dao = DaoPcs() #- Crea un objeto de la clase DaoPcs, que maneja la base de datos de computadoras.
    pcs = dao.get_all(database) #- Obtiene todas las computadoras almacenadas en la base de datos.
    menu = Menu(True, True) #indicar que ciertas opciones del menú están activadas.
    return templates.TemplateResponse( #-  Se usa para mostrar una página web con los datos de las computadoras.
        request=request, #Se pasa la solicitud HTTP actual a la plantilla.
        name="formupdatesistema.html", #Se indica que la plantilla que se va a mostrar es 
        context={"menu": menu, "pcs": pcs} # Se envían datos a la plantilla para que puedan ser usados en el HTML.
    )

@app.post("/update_sistemas")
def update_sistemas(
    request: Request,  #Representa la solicitud del usuario.
    marca: Annotated[str, Form()], # Son los datos que el usuario envió en el formulario.
    tipo: Annotated[int, Form()], # Son los datos que el usuario envió en el formulario.
    sistema: Annotated[str, Form()], # Son los datos que el usuario envió en el formulario.
    procesador: Annotated[str, Form()] # Son los datos que el usuario envió en el formulario.
):
    dao = DaoPcs() #- Crea un objeto de la clase DaoPcs, que maneja la base de datos de computadoras.
    dao.update(database, marca, tipo, sistema, procesador) # Actualiza la información de una computadora en la base de datos.

    pcs = dao.get_all(database) #Después de actualizar la computadora, se obtiene la lista completa de computadoras desde la base de datos.
    menu = Menu(True, True)
    return templates.TemplateResponse(
        request=request,
        name="updatesistemas.html",
        context={"menu": menu, "pcs": pcs} 
    )
     
