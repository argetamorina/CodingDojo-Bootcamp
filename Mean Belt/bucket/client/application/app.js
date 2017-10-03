angular.module('app', ['ngRoute', 'ngCookies'])
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'partials/_login.html',
        controller: 'login'
      })
      .when('/dashboard', {
        templateUrl: 'partials/_dashboard.html',
        controller: 'bucket-items'
      })
      .when('/user/:id', {
        templateUrl: 'partials/_user.html',
        controller: 'users'
      });
  }]);
