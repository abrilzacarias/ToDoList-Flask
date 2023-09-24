document.addEventListener("DOMContentLoaded", function () { //se utiliza cuando se cargo todo el html
    const enlaces = document.querySelectorAll(".nav a"); //selecciona todos los elementos <a> que estan dentro de un elemento nav

  // Función para resaltar el enlace activo
  function resaltarEnlaceActivo() {
    enlaces.forEach(function (enlace) {
      enlace.classList.remove("active");
    });

    const seccionActual = document.querySelector("section[style='display: block;']");
    const enlaceCorrespondiente = document.querySelector(`.nav a[href="#${seccionActual.id}"]`);
    
    if (enlaceCorrespondiente) {
      enlaceCorrespondiente.classList.add("active");
    }
  }

  // Agrega el evento "click" a los enlaces para cambiar el estilo
  enlaces.forEach(function (enlace) {
    enlace.addEventListener("click", function (event) {
      event.preventDefault();
      const seccionId = this.getAttribute("href").substring(1);
      mostrarSeccion(seccionId);
      resaltarEnlaceActivo();
    });
  });

  // Llama a la función para resaltar el enlace activo al cargar la página
  resaltarEnlaceActivo();
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
            const listItem = botonEditar.closest("li");
            const nombreActividad = listItem.querySelector("label[name='tareaEditar']");
            const inputEditar = listItem.querySelector("input#inputEditar");
            const botonGuardar = listItem.querySelector(".boton.guardar");
            const botonCancelar = listItem.querySelector(".boton.cancelar");
            
            nombreActividad.style.display = "none";
            inputEditar.style.display = "block";
            inputEditar.value = nombreActividad.textContent; // Establecer el valor del input como el nombre actual
            botonEditar.style.display = "none";
            botonGuardar.style.display = "inline-block";
            botonCancelar.style.display = "inline-block";

            // Agrega aquí el código para el botón "Cancelar"
            botonCancelar.addEventListener("click", function () {
                // Tu lógica para el botón "Cancelar" aquí
                nombreActividad.style.display = "block";
                inputEditar.style.display = "none";
                botonEditar.style.display = "inline-block";
                botonGuardar.style.display = "none";
                botonCancelar.style.display = "none";
            });
        });
    });

});
