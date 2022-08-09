# CATALOG NOW
Catalogo para publicar listado de productos

## Contenido
1. [Información general](#información-general)
2. [Tecnología](#tecnología)
3. [Setup](#setup)
4. [Mapa del usuario](#mapa-del-usuario)
5. [Casos de prueba](#casos-de-prueba)
6. [Colaboradores](#colaboradores)
7. [Video app de la aplicación](#video-app-catalog-now)



## Información general
<p>Trabaja tu catalogo online y publicalo a todos tus clientes con Django.</p>
<p>Algunas funciones en las que trabajamos.</p>

- Lista de productos
- Detalle de producto
- Panel de administración de catalogo de productos (Crear, Actualizar y borrar productos)
- login
- logout
- Registración

## Tecnología
<p>Proyecto creado con:</p>

- Python 3.10.5
- Djnago: 4.0.5
- Bootstrap: 5.2.x    

## Setup
<p>Instalar dependiencias</p>

```bash
> pip install -r requirements.txt
```

### Ajuste para correr Django
<p>**Creación de la Base de datos**</p>

Linux:
```bash
> python manage.py migrate 
```
Windows:
```bash
c:\> py manage.py migrate
```

### Crear superuser: 

Linux
```bash
> python manage.py createsuperuser
```

Windows
```bash
> py manage.py createsuperuser
```

```bash
> User: (usuario administrador)

> Email: (colocar email si es que lo desea)

> Pass: (Completar con un contraseña)
```

## Correr Servidor

```bash
> python manage.py runserver
```
####  Url de Acceso a la aplicación
```bash
> http://127.0.0.1:8000/
```
 
#### Url de Acceso al Panel de administración de la base de datos
```bash
> http://127.0.0.1:8000/admin 
```
<p>Si todo va bien, debería poder abrir el navegador y ver cómo se ejecuta la aplicación.</p>

## Administración de usuarios.
<p>Los usuarios podrán darse de alta ellos mismo desde (http://127.0.0.1:8000/panel/login). El usuario creado no tendrá permisos de crear, editar o eliminar catalogo o productos hasta que el administrador le otorgue. A su vez el usuario administrador deberá crear al nuevo usuario como "publisher" para poder crear productos bajo su username.</p>

PASOS:
1. Acceso al panel de administración de Django (http://127.0.0.1:8000/admin):
 para poder ingresar  al panel de administración sera con el superuser creado con anterioridad. 

2. Una vez ingresado al panel de administración de Django deberá agregar como Publisher
al usuario y luego  otorgales permisos para agregar, editar o eliminar según las pretenciones del mismo.

## Agregar Catalogo , Productos y editar perfil (Una vez registrado el usuario) 

1. Ingresar a -> http://127.0.0.1:8000/panel 

2. Loguearse con su usuario y contraseña.

3. Una vez registrado el usuario se va a encontrar con el panel de administración de productos en dónde  podrá 
elegir crear, agregar, editar o borrar un catalogo y/o productos según los permisos otorgados.

4. En el margen superior derecho se encontrará con el menu del ususario
el cual le permite acceder al Perfil, Panel de Administración o desloguearse.

## Mapa del usuario

[Miro - mapa de usuario](https://miro.com/app/board/uXjVOj_k2rg=/?share_link_id=399463018519).

## Casos de prueba

[Casos de prueba](https://docs.google.com/spreadsheets/d/1uEIr7sc-B0U5nE3B9Pu1qx707caib2q78oHCIwA6j8Q/edit?usp=sharing).


## Colaboradores

- Pablo Moreno
- César Costa

## Video app Catalog Now
https://drive.google.com/file/d/1R55iKyjhFPve3OpUtbytN1EdYW_Ro1Cu/view?usp=sharing
