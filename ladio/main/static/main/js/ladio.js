(function () {
    'use strict';

    angular.module('ladio', [
        'ui.router',
        'ngResource',
        'ngCookies',
        'angularSpinner',
        'ladio.services',
        'ladio.routes',
        'ladio.configs',
        'ladio.controllers'
    ])

    .run(function($http,Authentication,$state, $rootScope, $cookies) {
            $http.defaults.xsrfHeaderName = 'X-CSRFToken';
            $http.defaults.xsrfCookieName = 'csrftoken';

            if(!$rootScope.authenticatedUser && Authentication.isAuthenticated()) {
                $rootScope.authenticatedUser = JSON.parse($cookies.get('authenticatedUser'));
            }

            activate();

            function activate() {
                if( Authentication.isAuthenticated()) {
                    $state.go('index');
                }
            }
        })
})();
