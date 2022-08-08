# catalog-now
Catalogo para publicar listado de productos

## Contenido
1. Información general
2. Tecnología
3. Setup
4. Colaboradores

## Información general
<p>Trabaja tu catalogo online y publicalo a todos tus clientes en Django.</p>
<p>Algunas funciones en las que trabajamos.</p>

- Lista de productos
- Detalle de producto
- Panel de administración de catalogo de productos (Crear, Actualizar y borrar productos)
- login
- logout
- Registracion

## Tecnología
<p>Proyecto creado con:</p>

- Python 3.10.5
- Djnago: 4.0.5
- Bootstrap: 5.2.x    

## Setup
<p>Instalar dependiencias</p>

```bash
- > pip install -r requirements.txt
```

### Ajuste para correr Django
<p>**Creación de la Base de datos**</p>

```bash
- > python mananage.py migrate 

- > c:\> py mananage.py migrate (Windows)
```

### Crear superuser: 

```bash
- > python mananage.py createsuperuser

- > User: (crear usuario)

- > Email: (colocar email si es que lo desea)

- > Pass: (Completar con un contraseña)
```

## Correr Servidor

```bash
- > python mananage.py runserver

###  Url de Acceso a la aplicación
 - > http://127.0.0.1:8000/
 
### Url de Acceso al Panel de administración de la base de datos
- > http://127.0.0.1:8000/admin 
```
<p>Si todo va bien, debería poder abrir el navegador y ver cómo se ejecuta la aplicación.</p>

## Administración de usuarios. 
```bash
1. Acceso al panel de administración de Djnago (- > http://127.0.0.1:8000/admin ):
 para poder ingresar  al panel de administración sera con el superuser creado con anterioridad. 
```

```bash
2. Una vez ingresado al panel de administración de Djnago deberá  agregar como Publisher
al usuario y luego  otorgales permisos para agregar, editar o eliminar según las pretenciones del mismo.
```

## Agregar Catalogo , Productos y editar perfil (Una vez registrado el usuario) 

```bash
1. -Ingresar a  - > http://127.0.0.1:8000/panel 

2. -Loguearse con su usuario y contraseña.

3. -Una vez registrado el usuario se  va a  encontrar con el panel de administración de productos en dónde  podrá 
elegir crear, agregar, editar o borrar un catalogo y/o  productos.

4. En el margen superior derecho se encontrará con el menu del ususario
el cual le permite acceder al Profile, Panel de Admin o desloguearse
```
## Mapa del usuario

[Miro - mapa de usuario](https://miro.com/app/board/uXjVOj_k2rg=/?share_link_id=399463018519).

