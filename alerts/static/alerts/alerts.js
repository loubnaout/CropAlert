const alertsContainer = document.getElementById('alerts-container');
const apiUrl = 'http://127.0.0.1:8000/api/alerts/?lat=34.02&lon=-6.84&radius=5';
const token = 'your-auth-token-here';

async function fetchAlerts() {
    try {
        const response = await fetch(apiUrl, {
            method: 'GET',
            headers: {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json',
            }
        });

        if (!response.ok) {
            alertsContainer.innerText = response.status === 401 || response.status === 403
                ? 'Access denied: Please log in with proper permissions.'
                : 'Failed to fetch alerts.';
            return;
        }

        const alerts = await response.json();

        alertsContainer.innerHTML = alerts.length === 0
            ? 'No alerts found in your area.'
            : '';

        alerts.forEach(alert => {
            const div = document.createElement('div');
            div.classList.add('alert-box');
            div.innerHTML = `
                <h3>${alert.title}</h3>
                <p><strong>Description:</strong> ${alert.description}</p>
                <p><strong>Agriculture type:</strong> ${alert.agriculture_type}</p>
                <p><strong>Location:</strong> (${alert.latitude}, ${alert.longitude})</p>
                <p><em>Created at: ${new Date(alert.created_at).toLocaleString()}</em></p>
            `;
            alertsContainer.appendChild(div);
        });

    } catch (error) {
        alertsContainer.innerText = 'Error fetching alerts: ' + error.message;
    }
}

fetchAlerts();