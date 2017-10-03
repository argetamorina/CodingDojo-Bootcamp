angular.module('app')
  .factory('userFactory', ['$http', '$cookies', '$location', function ($http, $cookies, $location) {
    var factory = {};

    factory.currentUser = function () {
      return $cookies.getObject('user');
    };

    factory.login = function (name, callback) {
      $http.post('/login', { name })
        .then(function (res) {
          var user = res.data;

          delete user.bucket_items;

          $cookies.putObject('user', user);

          callback();
        });
    };

    factory.logout = function () {
      $cookies.remove('user');

      $location.path('/');
    };

    factory.getUser = function (id, callback) {
      $http.get(`/users/${id}`)
        .then(function (res) {
          var user = res.data;

          user.bucket_items = factory.normalizeBucketItems(user.bucket_items);

          callback(user);
        })
        .catch(function (err) {
          throw err;
        });
    };

    factory.getUsers = function (callback) {
      $http.get('/users')
        .then(function (res) {
          callback(factory.normalizeUsers(res.data));
        })
        .catch(function (err) {
          throw err;
        });
    };

    factory.normalizeUsers = function (users) {
      return users.map(function (user) {
        user.bucket_items = factory.normalizeBucketItems(user.bucket_items);

        return user;
      });
    };

    factory.normalizeBucketItems = function (bucketItems) {
      return bucketItems.map(function (bucketItem) {
        var _id = bucketItem._id;
        var owner = bucketItem.owner;
        var title = bucketItem.title;
        var description = bucketItem.description;
        var completed = bucketItem.completed;
        var createdAt = moment(bucketItem.createdAt).format('MMMM D, YYYY');

        return { _id, owner, title, description, completed, createdAt };
      });
    };

    return factory;
  }]);
