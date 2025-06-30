// Este script se ejecuta una vez que el contenido del DOM ha sido completamente cargado
document.addEventListener("DOMContentLoaded", () => {
  // Obtener el token de autenticación almacenado en el almacenamiento local del navegador
  const token = localStorage.getItem("token");

  /**
   * Función asincrónica para obtener la lista de paquetes desde el servidor
   * y actualizar la sección correspondiente en la página.
   */
  const fetchPackages = async () => {
    try {
      // Realizar una solicitud GET a la ruta "/packages" enviando el token en el encabezado de autorización
      const res = await fetch("/packages", {
        headers: { Authorization: `Bearer ${token}` }
      });
      // Convertir la respuesta en formato JSON
      const data = await res.json();

      // Obtener el contenedor en el DOM donde se mostrarán los paquetes
      const container = document.getElementById("packages");

      // Generar el HTML para cada paquete y actualizar el contenido del contenedor
      container.innerHTML = data.map(p => `
        <div class="card mb-2 p-2">
          <strong>${p.destination}</strong> | ${p.duration_days} días | $${p.price} | Cupo: ${p.capacity}
        </div>
      `).join("");
    } catch (error) {
      console.error("Error al obtener los paquetes:", error);
    }
  };

  /**
   * Evento que captura el envío del formulario para crear un nuevo paquete.
   * Previene el comportamiento por defecto del formulario y realiza una solicitud POST para crear el paquete.
   */
  document.getElementById("createPackageForm").addEventListener("submit", async e => {
    e.preventDefault(); // Evitar que la página se recargue al enviar el formulario

    // Crear un objeto con los datos del nuevo paquete, obtenidos desde los campos del formulario
    const newPkg = {
      destination: document.getElementById("destination").value,
      duration_days: parseInt(document.getElementById("duration").value),
      price: parseFloat(document.getElementById("price").value),
      capacity: parseInt(document.getElementById("capacity").value),
    };

    try {
      // Enviar una solicitud POST a "/packages" para crear un nuevo paquete
      await fetch("/packages", {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${token}`,
          "Content-Type": "application/json" // Indicar que el cuerpo de la solicitud es JSON
        },
        body: JSON.stringify(newPkg) // Convertir el objeto a una cadena JSON
      });

      // Actualizar la lista de paquetes después de crear uno nuevo
      await fetchPackages();
    } catch (error) {
      console.error("Error al crear el paquete:", error);
    }
  });

  // Cargar y mostrar los paquetes existentes al cargar la página
  fetchPackages();
});
