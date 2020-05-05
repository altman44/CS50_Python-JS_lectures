const express = require('express');

const app = express();

const data = {
    ids: [1,2,3,4],
    info: [
        {
            id: 1,
            title: 'Think and Grow Rich',
            author: 'Napoleón Hill'
        },
        {
            id: 2,
            title: 'Harry Potter',
            author: 'J.K. Rowling'
        },
        {
            id: 3,
            title: 'The Lean Startup',
            author: 'Eric Ries'
        },
        {
            id: 4,
            title: 'How to win friends and influence people',
            author: 'Dale Carnegie'
        },
    ]
};

app.get('/', (req, res) => {
    res.end('Justo to get data from the API. Go to "/api"')
});

app.get('/api', (req, res) => {
    res.json(data);
});

app.listen(3000, () => {
    console.log('Server on port: 3000');
})