angular.module('app')
  .controller('users', ['$scope', '$routeParams', '$location', 'userFactory', 'bucketItemFactory', function ($scope, $routeParams, $location, userFactory, bucketItemFactory) {
    var user = userFactory.currentUser();

    if (!user) {
      $location.path('/');

      return;
    }

    $scope.currentUser = user;

    $scope.logout = userFactory.logout;

    $scope.user = {};

    userFactory.getUser($routeParams.id, function (user) {
      $scope.user = user;
    });

    $scope.doneBucketItems = function () {
      if (!$scope.user.bucket_items) return [];

      return $scope.user.bucket_items.filter(function (bucketItem) {
        return bucketItem.completed;
      })
    };

    $scope.pendingBucketItems = function () {
      if (!$scope.user.bucket_items) return [];

      return $scope.user.bucket_items.filter(function (bucketItem) {
        return !bucketItem.completed;
      })
    };

    $scope.toggleBucketItem = function (id) {
      bucketItemFactory.toggleBucketItem(id);
    };
  }]);
