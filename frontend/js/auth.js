// Este evento se dispara cuando todo el contenido del DOM ha sido completamente cargado y analizado
document.addEventListener("DOMContentLoaded", () => {
    // Obtener referencias a los formularios de login y registro por sus IDs
    const loginForm = document.getElementById("loginForm");
    const registerForm = document.getElementById("registerForm");

    // Si existe el formulario de login en el DOM
    if (loginForm) {
        // Añadir un evento para manejar el envío del formulario de login
        loginForm.addEventListener("submit", async (e) => {
            e.preventDefault(); // Prevenir el comportamiento por defecto de envío del formulario

            // Obtener los valores ingresados por el usuario en los campos de email y contraseña
            const email = document.getElementById("email").value;
            const password = document.getElementById("password").value;

            try {
                // Realizar una petición POST al endpoint de login en el servidor
                const res = await fetch("/auth/login", {
                    method: "POST", // Método HTTP POST
                    headers: {
                        "Content-Type": "application/json" // Especificar que el contenido enviado es JSON
                    },
                    body: JSON.stringify({ email, password }) // Enviar los datos en formato JSON
                });

                // Parsear la respuesta recibida en formato JSON
                const data = await res.json();

                if (res.ok) {
                    // Si la respuesta es exitosa, guardar el token de acceso en localStorage
                    localStorage.setItem("token", data.access_token);
                    // Redirigir a otra página, por ejemplo, a la página de paquetes
                    window.location.href = "packages.html";
                } else {
                    // Si hubo un error, mostrar el mensaje de error en un elemento con id 'message'
                    document.getElementById("message").innerText = data.detail;
                }
            } catch (error) {
                // Manejar errores de red o excepciones inesperadas
                document.getElementById("message").innerText = "Error de red. Por favor, intenta nuevamente.";
                console.error("Error en el login:", error);
            }
        });
    }

    // Si existe el formulario de registro en el DOM
    if (registerForm) {
        // Añadir un evento para manejar el envío del formulario de registro
        registerForm.addEventListener("submit", async (e) => {
            e.preventDefault(); // Prevenir el comportamiento por defecto de envío del formulario

            // Obtener los valores ingresados por el usuario en los campos de email y contraseña
            const email = document.getElementById("email").value;
            const password = document.getElementById("password").value;

            try {
                // Realizar una petición POST al endpoint de registro en el servidor
                const res = await fetch("/auth/register", {
                    method: "POST", // Método HTTP POST
                    headers: {
                        "Content-Type": "application/json" // Especificar que el contenido enviado es JSON
                    },
                    body: JSON.stringify({ email, password }) // Enviar los datos en formato JSON
                });

                // Parsear la respuesta recibida en formato JSON
                const data = await res.json();

                // Mostrar el mensaje de éxito o error en un elemento con id 'message'
                document.getElementById("message").innerText = data.message || data.detail;
            } catch (error) {
                // Manejar errores de red o excepciones inesperadas
                document.getElementById("message").innerText = "Error de red. Por favor, intenta nuevamente.";
                console.error("Error en el registro:", error);
            }
        });
    }
});
