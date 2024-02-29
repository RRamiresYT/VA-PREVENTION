document.addEventListener('DOMContentLoaded', function() {
    const startButton = document.getElementById('startButton');
    if (startButton) {
        startButton.addEventListener('click', function() {
            dialogosBarreiras();
            startButton.style.display = 'none'; // Hide the startButton after clicking it
        });
    }
});

function dialogosBarreiras() {
    fetch('http://127.0.0.1:5000/getDialogosBarreiras', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
        // Add any additional headers if needed
      }
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      updateCategoryText(data);
    })
    .catch(error => {
      console.error('There was a problem with the fetch operation:', error);
    });
}

function updateCategoryText(data) {
    const categoryDiv = document.querySelector('.category p');
    const buttonsDiv = document.querySelector('.buttonsSolucoes');

    if (categoryDiv && buttonsDiv) {
        const category = data.category;
        const barrier = data.barrier;
        categoryDiv.textContent = category + " - " + barrier;

        const solutions = data.solutions;
        Object.keys(solutions).forEach(solutionKey => {
            const solution = solutions[solutionKey];
            const button = document.createElement('button');
            button.textContent = solutionKey;
            button.addEventListener('click', function() {
                // Handle button click event here
                handleButtonClick(solution);
            });
            buttonsDiv.appendChild(button);
        });
    }
}

let currentItemIndex = 0;
let currentSolution = null;

function handleButtonClick(solution) {
    const buttonsDiv = document.querySelector('.buttonsSolucoes');
    const itemsDiv = document.createElement('div');

    // Store the current solution and reset the item index
    currentSolution = solution;
    currentItemIndex = 0;

    // Hide the buttons
    buttonsDiv.style.display = 'none';

    // Show the first item initially
    displayCurrentItem(itemsDiv);

    // Append the items to the main element
    const mainElement = document.querySelector('main');
    mainElement.appendChild(itemsDiv);

    // Add "Voltar" and "Continuar" buttons
    const backButton = document.createElement('button');
    backButton.textContent = 'Voltar';
    backButton.addEventListener('click', function() {
        // Navigate to the previous item
        currentItemIndex = Math.max(0, currentItemIndex - 1);
        displayCurrentItem(itemsDiv);
    });
    mainElement.appendChild(backButton);

    const continueButton = document.createElement('button');
    continueButton.textContent = 'Continuar';
    continueButton.addEventListener('click', function() {
        // Navigate to the next item
        currentItemIndex = Math.min(currentSolution.length - 1, currentItemIndex + 1);
        displayCurrentItem(itemsDiv);
    });
    mainElement.appendChild(continueButton);
}

function displayCurrentItem(itemsDiv) {
    // Clear the items div before displaying the current item
    itemsDiv.innerHTML = '';

    // Show the current item
    const itemParagraph = document.createElement('p');
    itemParagraph.textContent = currentSolution[currentItemIndex];
    itemsDiv.appendChild(itemParagraph);
}