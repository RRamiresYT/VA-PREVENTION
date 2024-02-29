window.onload = function() {
    createCheckboxes();
  };
  
  const checkboxes = document.querySelectorAll('.checkbox');
  const advanceButton = document.getElementById('advanceButton');
  
  function createCheckboxes() {
    fetch('http://127.0.0.1:5000/getBarriersT', {
      method: 'GET'
    })
      .then(response => response.json())
      .then(data => {
        const checkboxFieldset = document.getElementById('checkboxFieldset');
  
        Object.keys(data).forEach(key => {
          const item = data[key];
  
          const checkboxLabel = document.createElement('label');
          const checkbox = document.createElement('input');
          checkbox.type = 'checkbox';
          checkbox.className = 'checkbox';
          checkbox.name = 'barrier';
          checkbox.value = key; // Use the key as the value for each checkbox
          checkboxLabel.appendChild(checkbox);
          checkboxLabel.appendChild(document.createTextNode(` ${item.barreira}`)); // Display the "barreira" property as checkbox text
  
          checkboxFieldset.appendChild(checkboxLabel);
          checkboxFieldset.appendChild(document.createElement('br'));
        });
  
        checkboxes.forEach(checkbox => {
          checkbox.addEventListener('change', function() {
            const checkedCount = [...checkboxes].filter(cb => cb.checked).length;
  
            if (checkedCount >= 3) {
              advanceButton.style.display = 'block';
              checkboxes.forEach(cb => {
                if (!cb.checked) {
                  cb.disabled = true;
                }
              });
            } else {
              advanceButton.style.display = 'none';
              checkboxes.forEach(cb => {
                cb.disabled = false;
              });
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
    const selectedBarriers = [...checkboxes]
      .filter(checkbox => checkbox.checked)
      .map(checkbox => checkbox.value);
  
    sessionStorage.setItem('selectedBarriers', JSON.stringify(selectedBarriers));
  
    // Redirecting to a new HTML page
    window.location.href = '../new_page.html'; // Replace 'new_page.html' with your desired URL
  });
  