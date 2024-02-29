window.onload = function() {
    createForm();
};

function createForm() {
    fetch('http://127.0.0.1:5000/getAvaliation', {
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
            fieldset.append(p_fieldset);

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

            form.appendChild(div_question_parent);
        });

        const questionsDiv = document.getElementById('questionsDiv');
        questionsDiv.appendChild(form);

        const submitBtn = document.createElement('button'); // Change the button type
        submitBtn.type = 'button'; // Specify the button type
        submitBtn.textContent = 'Submit';
        submitBtn.classList.add('submit-btn');
        form.appendChild(submitBtn);

        submitBtn.addEventListener('click', function(event) {
            event.preventDefault();

            const formData = {};

            // Iterate through each fieldset in the form
            form.querySelectorAll('fieldset').forEach(fieldset => {
                const key = fieldset.querySelector('input[type="radio"]:checked').name; // Retrieve the key from the radio button name
                const selectedRadio = fieldset.querySelector('input[type="radio"]:checked');

                if (selectedRadio) {
                    formData[key] = selectedRadio.value;
                } else {
                    formData[key] = null; // or any default value if no option is selected
                }
            });

            fetch('http://127.0.0.1:5000/postAvaliation', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(result => {
                console.log('Response from POST request:', result);
                // Redirect to the specified href after processing the form
                window.location.href = '../ChangeHabits/changeHabits.html';
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