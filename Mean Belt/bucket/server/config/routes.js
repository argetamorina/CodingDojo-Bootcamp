var users = require('../controllers/users');
var bucketItems = require('../controllers/bucket-items');

module.exports = function (app) {
  app.get('/users', users.all);
  app.get('/users/:user_id', users.one);
  app.post('/login', users.login);

  app.post('/bucket-items', bucketItems.create);
  app.post('/bucket-items/:bucket_item_id/toggle', bucketItems.toggle);
};
