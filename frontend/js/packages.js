document.addEventListener("DOMContentLoaded", () => {
  const token = localStorage.getItem("token");

  const fetchPackages = async () => {
    const res = await fetch("/packages", {
      headers: { Authorization: `Bearer ${token}` }
    });
    const data = await res.json();
    const container = document.getElementById("packages");
    container.innerHTML = data.map(p => `
      <div class="card mb-2 p-2">
        <strong>${p.destination}</strong> | ${p.duration_days} días | $${p.price} | Cupo: ${p.capacity}
      </div>
    `).join("");
  };

  document.getElementById("createPackageForm").addEventListener("submit", async e => {
    e.preventDefault();
    const newPkg = {
      destination: document.getElementById("destination").value,
      duration_days: parseInt(document.getElementById("duration").value),
      price: parseFloat(document.getElementById("price").value),
      capacity: parseInt(document.getElementById("capacity").value),
    };

    await fetch("/packages", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${token}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify(newPkg)
    });

    await fetchPackages();
  });

  fetchPackages();
});
