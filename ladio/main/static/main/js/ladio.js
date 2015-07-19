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

    //.value('UrlBundle', {
    //        'StaticUrl':'staticurl',
    //        'RootUrl':'rooturl'
    //    })

    .run(function($http,Authentication,$state, $rootScope, $cookies, StaticUrl, RootUrl, $location) {
            $http.defaults.xsrfHeaderName = 'X-CSRFToken';
            $http.defaults.xsrfCookieName = 'csrftoken';

            //var current_url = $location.absUrl();
            //var pattern = /^https?:\/\/127\.0\.0\.1|^https?:\/\/localhost/g.test($location.absUrl());

            //UrlBundle.StaticUrl = pattern ? '/' : 'https://ladiobc.s3-ap-northeast-1.amazonaws.com/';
            //UrlBundle.RootUrl = pattern ? 'http://localhost:8000/' : 'http://ladio-test2-dev.elasticbeanstalk.com/';

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
