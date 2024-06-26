const Blog = require('../models/blog')

const blog_index = (req, res) => {
    Blog.find().sort({ createdAt: -1 })
    .then((result) => {
        res.render('index', {title: 'Home', blogs: result})
    }).catch((err) => {
        console.log(err);
    })
}

const blog_details = (req, res) => {
    const id = req.params.id;
    Blog.findById(id).then((result) => {
        res.render('details', { title: 'Blog Details', blog: result })
    }).catch((err) => {
        res.render('404', { title: 'Not Found' })
    })
}

const blog_create_get = (req, res) => {
    res.render('create', {title: 'Create'})
}

const blog_create_post = (req, res) => {
    const blog = new Blog(req.body);
    blog.save().then((result) => {
        res.redirect('/blogs')
    }).catch((err) => {
        console.log(err);
    })
}

const blog_update_get = (req, res) => {
    const id = req.params.id;
    Blog.findById(id).then((result) => {
        res.render('update', { title: 'Update', blog: result })
    }).catch((err) => {
        res.render('404', { title: 'Not Found' })
    })
}

const blog_update = (req, res) => {
    const id = req.params.id;
    Blog.updateOne({ _id: id }, { $set: req.body }).then((result) => {
        res.redirect(`/blogs/${id}`);
    }).catch(err => {
        console.log(err);
    })
}

const blog_delete = (req, res) => {
    const id = req.params.id;
    Blog.findByIdAndDelete(id).then((result) => {
        res.json({ redirect: '/blogs' });
    }).catch((err) => {
        console.log(err);
    })
}


module.exports = {
    blog_index,
    blog_details,
    blog_create_get,
    blog_create_post,
    blog_update_get,
    blog_update,
    blog_delete
}