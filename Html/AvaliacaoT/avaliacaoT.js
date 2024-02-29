window.onload = function() {
    createForm();
};

function createForm() {
    fetch('http://127.0.0.1:5000/getAvaliationT', {
        method: 'GET'
    })
    .then(response => response.json())
    .then(data => {
        const form = document.createElement('form');
        form.classList.add('form-ema');

        let questionCount = 0;

        Object.keys(data).forEach(key => {
            const questionData = data[key];
            questionCount++;

            const div_question_parent = document.createElement('div');
            div_question_parent.classList.add('question-block');

            const number_question_child = document.createElement('div');
            number_question_child.classList.add('number-question-div');

            const question_answers_div = document.createElement('div');
            question_answers_div.classList.add('question-answers-div');

            div_question_parent.appendChild(number_question_child);
            div_question_parent.appendChild(question_answers_div);

            const p_question_number = document.createElement('p');
            p_question_number.textContent = "Q" + questionCount;
            number_question_child.appendChild(p_question_number);

            const fieldset = document.createElement('fieldset');
            fieldset.classList.add('question-fieldset');

            question_answers_div.appendChild(fieldset);

            const p_fieldset = document.createElement('p');
            p_fieldset.textContent = questionData.pergunta;
            fieldset.appendChild(p_fieldset);

            // Check if the number of options is between 3 and 8
            if (questionData.resposta.length >= 3 && questionData.resposta.length <= 8) {
                // Create dropdown for options
                const dropdown = document.createElement('select');
                dropdown.name = key;

                questionData.resposta.forEach(optionText => {
                    const option = document.createElement('option');
                    option.value = optionText;
                    option.text = optionText;
                    dropdown.appendChild(option);
                });

                fieldset.appendChild(dropdown);
            } else if (questionData.resposta.length > 8) {
                // If more than 8 options, create two dropdowns
                // One for original options and one for numbers from 0 to 60
                const dropdownOriginal = document.createElement('select');
                dropdownOriginal.name = key;

                questionData.resposta.forEach(optionText => {
                    const option = document.createElement('option');
                    option.value = optionText;
                    option.text = optionText;
                    dropdownOriginal.appendChild(option);
                });

                fieldset.appendChild(dropdownOriginal);

                const dropdownNumbers = document.createElement('select');
                dropdownNumbers.name = key + '_numbers';

                for (let i = 0; i <= 60; i++) {
                    const option = document.createElement('option');
                    option.value = i.toString();
                    option.text = i.toString();
                    dropdownNumbers.appendChild(option);
                }

                // Add both dropdowns to a container div
                const dropdownContainer = document.createElement('div');
                dropdownContainer.appendChild(dropdownOriginal);
                dropdownContainer.appendChild(dropdownNumbers);

                fieldset.appendChild(dropdownContainer);
            } else {
                // If less than or equal to 3 options, create radio buttons
                questionData.resposta.forEach(optionText => {
                    const optionLabel = document.createElement('label');
                    optionLabel.textContent = optionText;

                    const radio = document.createElement('input');
                    radio.type = 'radio';
                    radio.name = key; // Use the key from the initial data
                    radio.value = optionText;

                    optionLabel.appendChild(radio);
                    fieldset.appendChild(optionLabel);
                });
            }

            form.appendChild(div_question_parent);
        });

        const questionsDiv = document.getElementById('questionsDiv');
        questionsDiv.appendChild(form);

        const submitBtn = document.createElement('button'); // Change the button type
        submitBtn.type = 'button'; // Specify the button type
        submitBtn.textContent = 'Submit';
        submitBtn.classList.add('submit-btn');
        form.appendChild(submitBtn);




        // POST METHOD COMEÇA AQUI
        submitBtn.addEventListener('click', function(event) {
            // Collect form data
            const formData = {};
            const formElements = form.elements;
        
            for (let i = 0; i < formElements.length; i++) {
                const element = formElements[i];
        
                if (element.type !== 'button') {
                    formData[element.name] = element.value;
                }
            }
        
            // POST request
            fetch('http://127.0.0.1:5000/postAvaliationAF', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            })
            .then(response => response.json())
            .then(data => {
                // Handle the response if needed
                console.log('Submission successful:', data);
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error: ' + error);
            });
        });
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error: ' + error);
    });
}