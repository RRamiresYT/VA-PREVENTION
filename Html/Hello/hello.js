function fetchData() {
    fetch('http://127.0.0.1:5000/testeHello', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data && data.message) {
            document.getElementById('response').innerText = data.message;
        } else {
            document.getElementById('response').innerText = JSON.stringify(data, null, 2);
        }
    })
    .catch(error => console.error('Error:', error));
}

window.onload = fetchData;
