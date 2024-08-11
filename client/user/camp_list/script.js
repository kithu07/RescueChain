document.addEventListener('DOMContentLoaded', async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/get/camps');
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Fetched data:', data); // Debug: Check if data is fetched

        const campsContainer = document.getElementById('camps-container');
        if (data.camps && data.camps.length > 0) {
            data.camps.forEach(camp => {
                // Create a card element for each camp
                const campCard = document.createElement('div');
                campCard.className = 'box';
                campCard.innerHTML = `
                    <p><strong>${camp.camp_name}</strong></p>
                    <p>${camp.location}</p>
                    <p>Contact: ${camp.contact_no}</p>
                `;

                // Add click event to redirect to camp home page
                campCard.addEventListener('click', () => {
                    window.location.href = `../home/index.html`;
                });

                // Append the card to the container
                campsContainer.appendChild(campCard);
            });
        } else {
            campsContainer.innerHTML = '<p>No camps available</p>';
        }
    } catch (error) {
        console.error('Error fetching camps:', error);
    }
});
