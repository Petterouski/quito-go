// frontend/js/reservations.js

// Este script maneja la carga, creación y cancelación de reservas de paquetes turísticos.
// Se ejecuta una vez que el DOM esté completamente cargado para asegurar que todos los elementos HTML estén disponibles.

// Escucha el evento 'DOMContentLoaded' para inicializar funciones y eventos asociados a la DOM
document.addEventListener("DOMContentLoaded", () => {
  // Obtiene el token de autenticación almacenado en localStorage
  const token = localStorage.getItem("token");

  /**
   * Función para obtener y mostrar la lista de paquetes turísticos disponibles.
   * Realiza una solicitud GET a la API en la ruta '/packages'.
   * Utiliza el token de autenticación en los encabezados.
   * Renderiza los datos en el contenedor con id 'packages'.
   */
  const fetchPackages = async () => {
    try {
      // Realiza la petición GET a la API para obtener los paquetes
      const res = await fetch("/packages", {
        headers: { Authorization: `Bearer ${token}` }
      });
      
      // Verifica si la respuesta fue exitosa
      if (!res.ok) {
        throw new Error(`Error al obtener paquetes: ${res.status}`);
      }

      // Convierte la respuesta en formato JSON
      const data = await res.json();

      // Selecciona el contenedor en el HTML donde se mostrarán los paquetes
      const container = document.getElementById("packages");

      // Inserta en el HTML una lista de divs, cada uno representando un paquete
      container.innerHTML = data.map(p => `
        <div class="border p-2 mb-1">
          <strong>ID: ${p.id}</strong> - ${p.destination} (${p.duration_days} días, $${p.price}) - Cupo: ${p.capacity}
        </div>
      `).join("");
    } catch (error) {
      console.error("Error fetching packages:", error);
    }
  };

  /**
   * Función para obtener y mostrar la lista de reservas existentes.
   * Realiza una solicitud GET a la API en la ruta '/reservations'.
   * Incluye el token de autenticación en los encabezados.
   * Renderiza los datos en el contenedor con id 'reservations'.
   */
  const fetchReservations = async () => {
    try {
      // Solicitud GET para obtener las reservas
      const res = await fetch("/reservations", {
        headers: { Authorization: `Bearer ${token}` }
      });
      
      // Verifica si la respuesta fue exitosa
      if (!res.ok) {
        throw new Error(`Error al obtener reservas: ${res.status}`);
      }

      // Parsear la respuesta JSON
      const data = await res.json();

      // Selecciona el contenedor donde se mostrarán las reservas
      const container = document.getElementById("reservations");

      // Renderiza cada reserva en un div con detalles
      container.innerHTML = data.map(r => `
        <div class="border p-2 mb-1">
          <strong>ID: ${r.id}</strong> - Paquete ${r.package_id} - Usuario ${r.user_id} - Estado: ${r.status}
        </div>
      `).join("");
    } catch (error) {
      console.error("Error fetching reservations:", error);
    }
  };

  /**
   * Evento que maneja el envío del formulario para crear una nueva reserva.
   * Envía una solicitud POST a '/reservations' con los datos del usuario y paquete.
   * Después de crear la reserva, actualiza la lista de reservas.
   */
  document.getElementById("reserveForm").addEventListener("submit", async e => {
    e.preventDefault(); // Previene el comportamiento por defecto del formulario
    
    // Construye el payload con los datos del formulario
    const payload = {
      user_id: parseInt(document.getElementById("userId").value),
      package_id: parseInt(document.getElementById("packageId").value)
    };

    try {
      // Envía la solicitud POST para crear la reserva
      await fetch("/reservations", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
      });
      
      // Actualiza la lista de reservas tras la creación
      await fetchReservations();
      
      // Opcional: limpiar formulario después de enviar
      document.getElementById("reserveForm").reset();
    } catch (error) {
      console.error("Error al crear reserva:", error);
    }
  });

  /**
   * Evento que maneja el envío del formulario para cancelar una reserva.
   * Envía una solicitud POST a '/cancel-reservation/{id}' con la razón y usuario.
   * Luego, actualiza la lista de reservas.
   */
  document.getElementById("cancelForm").addEventListener("submit", async e => {
    e.preventDefault(); // Previene el comportamiento por defecto del formulario

    // Obtiene los valores del formulario
    const id = document.getElementById("reservationId").value;
    const reason = document.getElementById("reason").value;
    const user = document.getElementById("userCancel").value;

    try {
      // Envía la solicitud POST para cancelar la reserva específica
      await fetch(`/cancel-reservation/${id}`, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ reason, user })
      });

      // Actualiza la lista de reservas
      await fetchReservations();

      // Opcional: limpiar formulario después de cancelar
      document.getElementById("cancelForm").reset();
    } catch (error) {
      console.error("Error al cancelar reserva:", error);
    }
  });

  // Carga inicial de datos: obtiene y muestra paquetes y reservas
  fetchPackages();
  fetchReservations();
});
