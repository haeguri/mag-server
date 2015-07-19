(function () {
    'use strict';
    
    angular.module('ladio.routes', [])
    
    .config(function(
            $stateProvider,
            $urlRouterProvider,
            StaticUrl,
            UrlBundle
        ) 
        {
            UrlBundle = UrlBundle();

            $stateProvider
                .state('index', {
                    url: "/",
                    templateUrl: function() {
                        return  UrlBundle.StaticUrl + "static/main/partials/content/content.list.html"
                    },
                    controller: "ContentListController"
                })
                .state('content_detail', {
                    url: "/contents/:content_id",
                    //templateUrl: UrlBundle.StaticUrl + "static/main/partials/content/content.detail.html",
                    templateUrl: StaticUrl + "static/main/partials/content/content.detail.html",
                    controller: "ContentDetailController"
                })
                .state('register', {
                    url: "/register",
                    //templateUrl: UrlBundle.StaticUrl + "static/main/partials/auth/register.html",
                    templateUrl: StaticUrl + "static/main/partials/auth/register.html",
                    controller: "RegisterController"
                })
                .state('login', {
                    url: "/login",
                    //templateUrl: UrlBundle.StaticUrl + "static/main/partials/auth/login.html",
                    templateUrl: StaticUrl + "static/main/partials/auth/login.html",
                    controller: "LoginController"
                });

            $urlRouterProvider.otherwise('/');
        });
})();