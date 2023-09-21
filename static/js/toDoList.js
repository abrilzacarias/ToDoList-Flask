
console.log("hola")
document.addEventListener("DOMContentLoaded", function () {
    const todoForm = document.getElementById("todo-form");
    const inputTarea = document.getElementById("inputTarea");
    const responseElement = document.getElementById("response");

    todoForm.addEventListener("submit", function (event) {
        event.preventDefault(); // Evita el envío automático del formulario

        const taskText = inputTarea.value;

        // Envía la tarea al servidor Flask como una cadena usando AJAX
        fetch("/", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: `task=${encodeURIComponent(taskText)}`
        })
        .then(response => response.text())
        .then(data => {
            console.error("exito:", data);
        })
        .catch(error => {
            console.error("Error:", error);
        });

        inputTarea.value = ""; // Limpia el input después de enviar la tarea
    });
});

