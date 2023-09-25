document.addEventListener("DOMContentLoaded", function () { //se utiliza cuando se cargo todo el html
    const enlaces = document.querySelectorAll(".nav a"); //selecciona todos los elementos <a> que estan dentro de un elemento nav

  // función para resaltar el enlace activo
  function resaltarEnlaceActivo() {
    enlaces.forEach(function (enlace) {
      // elimina la clase active de todos los enlaces
      enlace.classList.remove("active");
    });

    const seccionActual = document.querySelector("section[style='display: block;']");
    // se utiliza para encontrar la seccion actual que se esta mostrando (la que tiene "display: block;")
    const enlaceCorrespondiente = document.querySelector(`.nav a[href="#${seccionActual.id}"]`);
    // encuentra el enlace correspondiente al ID de la sección actual
    if (enlaceCorrespondiente) {
      // agrega la clase active al enlace correspondiente
      enlaceCorrespondiente.classList.add("active");
    }
  }

  // agrega el evento "click" a los enlaces para cambiar el estilo
  enlaces.forEach(function (enlace) {
    enlace.addEventListener("click", function (event) {
      // previene el comportamiento predeterminado de los enlaces (evita que se cargue una nueva página)
      event.preventDefault();
      const seccionId = this.getAttribute("href").substring(1); //obtiene el ID de la seccion a la que se le hace clic 
      mostrarSeccion(seccionId); // llama a la funcion mostrarSeccion
      resaltarEnlaceActivo(); //resalta el enlace activo
    });
  });


});

    function mostrarSeccion(seccionId) {
        const secciones = document.querySelectorAll("section"); //selecciona todas las secciones del HTML
        secciones.forEach(function (section) { //iterar las secciones
            if (section.id === seccionId) { //compara el ID de cada seccion con el ID que queremos mostrar
                section.style.display = "block"; //si coinciden se establece su estilo para que se muestre con display:block
            } else {
                section.style.display = "none"; //si no coincide con el ID se oculta con display:none
            }
        });
    }

document.addEventListener("DOMContentLoaded", function () {
    
    const botonesEditar = document.querySelectorAll(".boton-editar");

    botonesEditar.forEach(function (botonEditar) {
        botonEditar.addEventListener("click", function () {
          //cuando se hace clic en un botonEditar
            const listItem = botonEditar.closest("li"); //encuentra el elemento li mas cercano al boton de editar
            const nombreActividad = listItem.querySelector("label[name='tareaEditar']"); //se busca dentro de listItem un elemento label que tenga el atributo name
            const inputEditar = listItem.querySelector("input#inputEditar"); //se busca un elemento input con un id igual a "inputEditar"
            const botonGuardar = listItem.querySelector(".boton.guardar");
            const botonCancelar = listItem.querySelector(".boton.cancelar");
            
            nombreActividad.style.display = "none"; //invisible
            inputEditar.style.display = "block"; //visible
            inputEditar.value = nombreActividad.textContent; // establece el valor del input como el nombre actual
            botonEditar.style.display = "none";
            botonGuardar.style.display = "inline-block";
            botonCancelar.style.display = "inline-block";

        
            botonCancelar.addEventListener("click", function () {
                
                nombreActividad.style.display = "block";
                inputEditar.style.display = "none";
                botonEditar.style.display = "inline-block";
                botonGuardar.style.display = "none";
                botonCancelar.style.display = "none";
            });
        });
    });

});
