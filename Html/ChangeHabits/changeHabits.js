window.onload = function() {
  createCheckboxes();
  advanceButton.style.display = 'none';
};

const checkboxes = document.querySelectorAll('.checkbox');
let checkedCount = 0;
const advanceButton = document.getElementById('advanceButton');

function createCheckboxes() {
  fetch('http://127.0.0.1:5000/getHabitsN', {
    method: 'GET'
  })
    .then(response => response.json())
    .then(data => {
      const checkboxFieldset = document.getElementById('checkboxFieldset');
      const checkboxes = [];

      Object.keys(data).forEach(key => {
        const item = data[key];

        const checkboxLabel = document.createElement('label');
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.className = 'checkbox';
        checkbox.name = 'phrase';
        checkbox.value = key; // Use the key as the value for each checkbox
        checkboxes.push(checkbox);

        checkboxLabel.appendChild(checkbox);
        checkboxLabel.appendChild(document.createTextNode(` ${item.habito}`)); // Display the "habito" property as checkbox text

        checkboxFieldset.appendChild(checkboxLabel);
        checkboxFieldset.appendChild(document.createElement('br'));
      });

      checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
          let checkedCount = checkboxes.filter(cb => cb.checked).length;

          checkboxes.forEach(cb => {
            if (!cb.checked) {
              if (checkedCount >= 3) {
                cb.parentNode.classList.add('disabled');
                advanceButton.style.display = 'block';
              } else {
                cb.parentNode.classList.remove('disabled');
                advanceButton.style.display = 'none';
              }
            }
          });

          if (checkedCount > 3) {
            this.checked = false;
          }
        });
      });
    })
    .catch(error => {
      console.error('Error fetching data:', error);
      // Handle errors, if any
    });
}

advanceButton.addEventListener('click', function() {
  const checkboxes = document.querySelectorAll('.checkbox'); // Selecting all checkboxes

  const selectedLabels = [];

  checkboxes.forEach(checkbox => {
    if (checkbox.checked) {
      const key = checkbox.value; // Get the value of the checkbox, which is the key
      selectedLabels.push(key); // Push the key into the selectedLabels array
    }
  });

  // Storing selected labels in session storage
  sessionStorage.setItem('selectedLabels', JSON.stringify(selectedLabels));

  // Redirecting to a new HTML page
  window.location.href = '../new_page.html'; // Replace 'new_page.html' with your desired URL
});
