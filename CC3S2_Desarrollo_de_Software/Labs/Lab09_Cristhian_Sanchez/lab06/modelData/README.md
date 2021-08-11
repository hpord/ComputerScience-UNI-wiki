# cc3s2 Lab06 Model Data


Dado que no tenemos un sistema de base de datos como backend para  obtener datos del modelo, almacenamos los datos del modelo en el DOM para que sean accesibles a las vistas. Agregamos una propiedad de objeto  llamada `cc3s2models` al DOM que contiene los datos del modelo para las diferentes vistas.


* `cc3s2models.exampleModel()` - El modelo para la tarea 1 - example view.
* `cc3s2models.statesModel()`  - El modelo para la tarea  2 - states view.

Estos modelos pueden accesarse por el controlador de la vista  bajo la propiedad window.
Por ejemplo:

    window.cc3s2models.statesModel()
    
accederá al arreglo de estados de la tarea 2 asi:

    window.cc3s2models.statesModel()[0] === 'Alabama'
