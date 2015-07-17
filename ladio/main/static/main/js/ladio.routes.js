(function () {
    'use strict';
    
    angular.module('ladio.routes', [])
    
    .config(function(
            $stateProvider,
            $urlRouterProvider,
            StaticUrl
        ) 
        {
            $stateProvider
                .state('index', {
                    url: "/",
                    templateUrl: StaticUrl + "static/main/partials/content/content.list.html",
                    controller: "ContentListController"
                })
                .state('content_detail', {
                    url: "/contents/:content_id",
                    templateUrl: StaticUrl + "static/main/partials/content/content.detail.html",
                    controller: "ContentDetailController"
                })
                .state('register', {
                    url: "/register",
                    templateUrl: StaticUrl + "static/main/partials/auth/register.html",
                    controller: "RegisterController"
                })

                .state('login', {
                    url: "/login",
                    templateUrl: StaticUrl + "static/main/partials/auth/login.html",
                    controller: "LoginController"
                });

            $urlRouterProvider.otherwise('/');
        });
})();