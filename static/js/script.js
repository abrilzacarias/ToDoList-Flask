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