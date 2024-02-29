// Fetch selected labels from session storage
const selectedLabels = JSON.parse(sessionStorage.getItem('selectedLabels'));
const questionsDiv = document.getElementById('questionsDiv');
let jsonData = {};

// Fetch data from Flask API
fetch('http://127.0.0.1:5000/getAvaliation')
    .then(response => response.json())
    .then(data => {
        jsonData = data;

        console.log(jsonData)

        // Check if selectedLabels exist and create divs for each item
        if (selectedLabels && Array.isArray(selectedLabels)) {
            selectedLabels.forEach((label, index) => {
                // Retrieve question and barreiras for the current label from JSON data
                const { pergunta, barreiras } = jsonData[label];

                // Create a div for each label
                const div = document.createElement('div');
                div.classList.add('question');

                // Create a title for the label
                const title = document.createElement('p');
                title.textContent = `Pergunta ${index + 1}: ${pergunta}`;
                div.appendChild(title);

                // Create buttons/options for the barreiras
                barreiras.forEach(barreira => {
                    const button = document.createElement('button');
                    button.textContent = barreira;
                    div.appendChild(button);
                });

                // Append the div to questionsDiv
                questionsDiv.appendChild(div);
            });
        }
    })
    .catch(error => console.error('Error fetching data:', error));
