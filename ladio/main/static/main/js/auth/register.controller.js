(function() {
    'use strict';

    angular.module('ladio.controllers')
        .controller('RegisterController', function(
            $location,
            $scope,
            Authentication,
            $state
        ) {
            $scope.register = {};

            activate();

            function activate() {
                if(Authentication.isAuthenticated()) {
                    $state.go('home');
                }
            }

            $scope.register.requestRegister = function() {
                Authentication.register($scope.register.email, $scope.register.password, $scope.register.nickname);
            }

        })
})();