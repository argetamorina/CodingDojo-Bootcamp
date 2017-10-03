angular.module('app')
  .controller('bucket-items', ['$scope', '$location', '$cookies', '$timeout', 'userFactory', 'bucketItemFactory', function ($scope, $location, $cookies, $timeout, userFactory, bucketItemFactory) {
    var user = userFactory.currentUser();

    if (!user) {
      $location.path('/');

      return;
    }

    $scope.currentUser = user;

    $scope.logout = userFactory.logout;

    $scope.users = [];

    $scope.showSuccessAlert = false;
    $scope.successTextAlert = null;
    $scope.errors = [];

    userFactory.getUsers(function (users) {
      $scope.users = users.filter(function (user) {
        if (user._id == $scope.currentUser._id) {
          $scope.currentUser.bucketItems = user.bucket_items;

          return false;
        }

        return true;
      });
    });

    $scope.createBucketItem = function (bucketItem) {
      if (!bucketItem) bucketItem = {};

      $scope.showSuccessAlert = false;
      $scope.successTextAlert = null;
      $scope.errors = [];

      bucketItem.owner = $scope.currentUser._id;
      if (bucketItem.tagged) {
        bucketItem.tagged = bucketItem.tagged._id;
      }

      bucketItemFactory.createBucketItem(bucketItem, function (createdBucketItem) {
        $scope.currentUser.bucketItems.push(createdBucketItem);

        bucketItem.title = null;
        bucketItem.description = null;
        bucketItem.tagged = null;

        $scope.showSuccessAlert = true;
        $scope.successTextAlert = 'Bucket item was created!';
      }, function (errors) {
        if (errors) {
          $scope.errors = errors;
        }
      });
    };

    $scope.toggleBucketItem = function (id) {
      bucketItemFactory.toggleBucketItem(id);
    };
  }]);
