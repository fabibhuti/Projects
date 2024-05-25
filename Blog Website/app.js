const express = require('express');
const morgan = require('morgan');
const mongoose = require('mongoose');
const blogRoutes = require('./routes/blogRoutes');

const app = express();

// connect to mongoDB
const dbURI = 'mongodb+srv://fabibhuti06:sjJhN0sQFEjKayIw@fanode1.3dzj4r5.mongodb.net/node-tuts?retryWrites=true&w=majority';
mongoose.connect(dbURI).then((result) => {
    console.log('connected to mongodb');
    app.listen(5000);
    }).catch((err) =>{
        console.log(err);
});

app.set('view engine', 'ejs');                      // register view engine
app.use(express.static('public'));                  // middleware & static files
app.use(express.urlencoded({ extended: true}));     // to get req.body
app.use(morgan('dev'));                             // to display req.path, req.method


// routes
// home
app.get('/', (req, res) => {
    res.redirect('/blogs');
})

// blog routes
app.use('/blogs', blogRoutes);

// about
app.get('/about', (req, res) => {
    res.render('about', {title: 'About'});
})

// 404 page
app.use((req, res) => {
    res.status(404).render('404', {title: 'Error'});
})
