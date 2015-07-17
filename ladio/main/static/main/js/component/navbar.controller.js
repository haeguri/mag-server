/**
 * Created by haegyun on 7/17/15.
 */
(function() {
    angular.module('ladio.controllers')

        .controller('NavBarController', function($scope, $state, Authentication) {
            $scope.navbar = {};

            $scope.navbar.email = 'staff2@ladio.co';
            $scope.navbar.password = 'ladio';

            activate();

            function activate() {
                if( Authentication.isAuthenticated()) {
                    $state.go('index');
                }
            }

            $scope.navbar.goLoginPage = function() {
                $state.go('login');
            };

            $scope.navbar.goRegisterPage = function() {
                $state.go('register');
            };

            $scope.navbar.requestLogin = function() {
                Authentication.login($scope.logout.email, $scope.logout.password);
            };

            $scope.navbar.requestLogout = function() {
                Authentication.logout();
            };

            $scope.navbar.goIndex = function() {
                $state.go('index');
            }
        })
})();