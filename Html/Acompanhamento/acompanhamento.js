document.addEventListener('DOMContentLoaded', function() {
  // Reset current phase to "opening" whenever the page is loaded or refreshed
  localStorage.setItem('currentPhase', 'opening');

  handleOpeningPhase();

  const startButton = document.getElementById('startButton');
  if (startButton) {
    startButton.addEventListener('click', function() {
      getNextPhaseDialogue(); // Start fetching dialogue for the next phase
    });
  }
});

function getNextPhaseDialogue() {
  let currentPhase = localStorage.getItem('currentPhase');
  // console.log('Getting dialogue for phase:', currentPhase);
  fetch(`http://127.0.0.1:5000/getNextPhaseDialogue?currentPhase=${currentPhase}`, {
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
    // Extract the next phase from the response
    const nextPhase = data.nextPhase;
    // console.log('Next phase:', nextPhase);
    
    // Execute different functions based on the next phase
    switch (nextPhase) {
      case 'reviewTasks':
        handleReviewTasksPhase(data);
        break;
      case 'assess':
        handleAssessPhase(data);
        break;
      case 'assignTasks':
        handleAssignTasksPhase(data);
        break;
      case 'counselling':
        handleCounsellingPhase(data);
        break;
      case 'closing':
        handleClosingPhase(data);
        break;
      default:
        console.error('Unknown phase:', nextPhase);
    }

    // Update current phase in local storage
    localStorage.setItem('currentPhase', nextPhase);
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });
}

// Define different functions to handle each phase
function handleOpeningPhase() {
  console.log("ENTREI");
  // Fetch opening phase dialogue
  fetch('http://127.0.0.1:5000/getOpeningPhaseDialogue', {
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
    // Process opening phase data
    console.log('Handling opening phase:', data);
    // You can add logic here to handle the opening phase data
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });
}

function handleReviewTasksPhase(data) {
  // Your logic for handling the reviewTasks phase goes here
  const categoryElement = document.querySelector('.category p');
  if (categoryElement) {
    categoryElement.textContent = "Review Tasks";
  }
  
  console.log('Handling reviewTasks phase:', data.reviewTasks);
}

function handleAssessPhase(data) {
  // Your logic for handling the assess phase goes here
  const categoryElement = document.querySelector('.category p');
  if (categoryElement) {
    categoryElement.textContent = "Assess";
  }
  
  console.log('Handling assess phase:', data.assess);
}

function handleAssignTasksPhase(data) {
  // Your logic for handling the assignTasks phase goes here
  const categoryElement = document.querySelector('.category p');
  if (categoryElement) {
    categoryElement.textContent = "Assign Tasks";
  }
  
  console.log('Handling assignTasks phase:', data.assignTasks);
}

function handleCounsellingPhase(data) {
  // Your logic for handling the counselling phase goes here
  console.log('Handling counselling phase:', data.counselling);
  dialogosBarreiras()
}

function handleClosingPhase(data) {
  // Your logic for handling the closing phase goes here
  const categoryElement = document.querySelector('.category p');
  if (categoryElement) {
    categoryElement.textContent = "Closing";
  }

  console.log('Handling closing phase:', data.closing);
}

// ----------------------------------------- handleCounsellingPhase() -----------------------------------------

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
    console.log(data)
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