angular.module('app')
  .controller('login', ['$scope', '$location', '$cookies', '$timeout', 'userFactory', function ($scope, $location, $cookies, $timeout, userFactory) {
    var user = userFactory.currentUser();

    if (user) {
      $location.path('/dashboard');

      return;
    }

    $scope.login = function (user) {
      userFactory.login(user, function () {
        $location.path('/dashboard');
      });
    };
  }]);
