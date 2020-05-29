document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#form').onsubmit = () => {
        const id_book = document.querySelector('#id_book');        
        // Initialize new request
        // XMLHttpRequest creates an object that allows me to make an AJAX request to some other web server
        const request = new XMLHttpRequest();
        request.open('POST', '/getDataFromBook');
        
        // Callback function for when request completes
        request.onload = () => {
            // Extract JSON data from request
            const data = JSON.parse(request.responseText);
            let msg = "There was an error.";
            
            // Update the result div
            if (data.success) {
                id_book.value = "";
                msg = `
                    ID: ${data.book.id}<br>
                    Title: ${data.book.title}<br>
                    Author: ${data.book.author}`;
            } else {
                
                if (data.error){
                    msg = data.error;
                } else {
                    msg = 'There was an error.';
                }
            }
            document.querySelector('#result').innerHTML = msg;
        }

        // Add data to send with request
        const data = new FormData();
        data.append('id_book', id_book.value);

        // Send request
        request.send(data);
        return false;
    }
})