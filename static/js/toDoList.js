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
