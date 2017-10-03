var User = require('mongoose').model('User');
var BucketItem = require('mongoose').model('BucketItem');

var bucketItemsController = {
  create: function (req, res) {
    var owner = req.body.owner;
    var tagged = req.body.tagged;
    var title = req.body.title;
    var description = req.body.description;

    var errors = [];

    if (!title || title.length < 5) {
      errors.push('Title must have at least 5 characters');
    }

    if (!description || description.length < 10) {
      errors.push('Description must have at least 10 characters');
    }

    if (errors.length > 0) {
      return res.status(400).json(errors);
    }

    BucketItem.create({ owner, title, description })
      .then(function (bucketItem) {
        BucketItem.populate(bucketItem, 'owner', function (err) {
          bucketItemsController.addBucketItemToUser(owner, bucketItem._id, function () {
            if (tagged) {
              bucketItemsController.addBucketItemToUser(tagged, bucketItem._id, function () {
                return res.json(bucketItem);
              }, function (err) {
                return res.status(400).json(err);
              });
            } else {
              return res.json(bucketItem);
            }
          }, function (err) {
            return res.status(400).json(err);
          });
        });
      })
      .catch(function (err) {
        return res.status(400).json(err);
      });
  },
  toggle: function (req, res) {
    var bucketItemId = req.params.bucket_item_id;

    BucketItem.findById(bucketItemId)
      .then(function (bucketItem) {
        bucketItem.completed = !bucketItem.completed;

        bucketItem.save()
          .then(function () {
            return res.json();
          })
          .catch(function (err) {
            return res.status(500).json();
          });
      })
      .catch(function (err) {
        return res.status(500).json();
      });
  },
  addBucketItemToUser: function (userId, bucketItemId, callback, errcb) {
    User.findById(userId)
      .then(function (user) {
        if (!user) return errcb();

        user.bucket_items.push(bucketItemId);

        user.save()
          .then(function () {
            if (callback) callback();
          })
          .catch(function (err) {
            if (errcb) errcb(err);
          });
      })
      .catch(function (err) {
        if (errcb) errcb(err);
      });;
  }
};

module.exports = bucketItemsController;
