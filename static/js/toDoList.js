document.addEventListener("DOMContentLoaded", function () { //se utiliza cuando se cargo todo el html
    const links = document.querySelectorAll("nav a"); //selecciona todos los elementos <a> que estan dentro de un elemento nav

    links.forEach(function (link) { //forEach itera cada elemento <a>
        // click es el tipo de evento 
        // se espera que ocurra un click en link 
        link.addEventListener("click", function (event) { //cuando alguien hace clic sobre algun elemento <a> se ejecuta la funcion (evento clic)
            //el evento click activa la funcion que se proporciona como segundo parametro
            //evento que se ejecuta
            event.preventDefault();  //lleva al navegador a una nueva pagina
            const seccionId = this.getAttribute("href").substring(1); // obtiene el atributo href del enlace donde se hizo clic 
            //utiliza subtring(1) para eliminar el primer caracter que es el # 
            mostrarSeccion(seccionId); //llama a la funcion mostrarSeccion y se le pasa el ID de la seccion como argumento
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
});

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
