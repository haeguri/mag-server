(function() {
    'use strict';


    angular.module('ladio.controllers')
        .controller('LoginController', function(
            $location,
            $scope,
            Authentication,
            $state
        )
        {
            $scope.login = {};

            $scope.login.email = 'staff2@ladio.co';
            $scope.login.password = 'ladio';

            activate();

            function activate() {
                if( Authentication.isAuthenticated()) {
                    $state.go('home');
                }
            }

            $scope.login.requestLogin = function() {
                Authentication.login($scope.login.email, $scope.login.password);
            }

            $scope.login.goRegister = function() {
                $state.go('register');
            }
        })
})();