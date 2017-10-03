angular.module('app')
  .factory('bucketItemFactory', ['$http', '$cookies', '$location', function ($http, $cookies, $location) {
    var factory = {};

    factory.createBucketItem = function (data, callback, error) {
      $http.post('/bucket-items', data)
        .then(function (res) {
          callback(res.data);
        })
        .catch(function (err) {
          if (error) error(err.data);
        });
    };

    factory.toggleBucketItem = function (id, callback) {
      $http.post(`/bucket-items/${id}/toggle`)
        .then(callback)
        .catch(function (err) {
          throw err;
        });
    };

    return factory;
  }]);
