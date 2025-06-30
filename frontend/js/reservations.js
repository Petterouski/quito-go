// frontend/js/reservations.js
document.addEventListener("DOMContentLoaded", () => {
  const token = localStorage.getItem("token");

  const fetchPackages = async () => {
    const res = await fetch("/packages", {
      headers: { Authorization: `Bearer ${token}` }
    });
    const data = await res.json();
    const container = document.getElementById("packages");
    container.innerHTML = data.map(p => `
      <div class="border p-2 mb-1">
        <strong>ID: ${p.id}</strong> - ${p.destination} (${p.duration_days} días, $${p.price}) - Cupo: ${p.capacity}
      </div>
    `).join("");
  };

  const fetchReservations = async () => {
    const res = await fetch("/reservations", {
      headers: { Authorization: `Bearer ${token}` }
    });
    const data = await res.json();
    const container = document.getElementById("reservations");
    container.innerHTML = data.map(r => `
      <div class="border p-2 mb-1">
        <strong>ID: ${r.id}</strong> - Paquete ${r.package_id} - Usuario ${r.user_id} - Estado: ${r.status}
      </div>
    `).join("");
  };

  document.getElementById("reserveForm").addEventListener("submit", async e => {
    e.preventDefault();
    const payload = {
      user_id: parseInt(document.getElementById("userId").value),
      package_id: parseInt(document.getElementById("packageId").value)
    };
    await fetch("/reservations", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });
    await fetchReservations();
  });

  document.getElementById("cancelForm").addEventListener("submit", async e => {
    e.preventDefault();
    const id = document.getElementById("reservationId").value;
    const reason = document.getElementById("reason").value;
    const user = document.getElementById("userCancel").value;

    await fetch(`/cancel-reservation/${id}`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ reason, user })
    });
    await fetchReservations();
  });

  fetchPackages();
  fetchReservations();
});
