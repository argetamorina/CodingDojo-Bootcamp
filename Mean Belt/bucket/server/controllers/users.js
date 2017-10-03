var User = require('mongoose').model('User');

module.exports = {
  all: function (req, res) {
    User.find()
      .populate({
        path: 'bucket_items',
        model: 'BucketItem',
        populate: {
          path: 'owner',
          model: 'User'
        }
      })
      .then(function (users) {
        res.json(users);
      })
      .catch(function (err) {
        res.status(404);
      });
  },
  one: function (req, res) {
    User.findById(req.params.user_id)
      .populate({
        path: 'bucket_items',
        model: 'BucketItem',
        populate: {
          path: 'owner',
          model: 'User'
        }
      })
      .then(function (user) {
        res.json(user);
      })
      .catch(function (err) {
        res.status(404);
      });
  },
  login: function(req, res) {
    var name = req.body.name;

    User.findOne({ name }, '_id name')
      .then(function(user) {
        if (user) {
          return res.json(user);
        } else {
          user = User.create({ name })
            .then(function (user) {
              return res.json({
                _id: user._id,
                name: user.name
              });
            })
            .catch(function (err) {
              return res.status(400).json(err);
            });
        }
      })
      .catch(function (err) {
        return res.status(500).json(err);
      });
  }
};
