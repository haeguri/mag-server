(function() {
    'use strict';

    angular.module('ladio.services')
        .factory('Authentication', function($cookies,$state, $http, $rootScope, UrlBundle) {
            var Authentication = {
                 /**y
                 * @name register
                 * @desc Try to register a new user
                 * @param {string} username The username entered by the user
                 * @param {string} password The password entered by the user
                 * @param {string} email The email entered by the user
                 * @returns {Promise}
                 * @memberOf ladio.authentication.services.Authentication
                 */
                register: function(email, password, nickname) {
                    return $http.post('/api/users/', {
                        nickname: nickname,
                        password: password,
                        email: email
                    }).then(function(data, status, headers, config) {
                        Authentication.login(email, password);
                    }, function(data, status, headers, config) {
                        console.log("Register Failer!", data)
                    })

                },

                login: function(email, password) {
                    console.log(email, password)
                    return $http.post('/api/auth/login/', {
                        email:email,
                        password:password
                    }).then(function(data, status, headers, config) {
                        Authentication.setAuthenticatedUser(data.data);
                        $state.go('index');
                        console.log("success login ", data);
                    }, function(data, status, headers, config) {
                        console.log("failed login ", data.data);
                    })
                },

                logout: function() {
                    return $http.post('/api/auth/logout/').then(function(data, status, headers, config) {
                        Authentication.unauthenticated();
                        $state.go('index');
                    }, function(data, status, headers, config) {
                        console.log("Error logout");
                    })
                },

                getAuthenticatedUser: function() {
                    if($cookies.get('authenticatedUser')) {
                        return;
                    }
                    return JSON.parse($cookies.get('authenticatedUser'));
                },

                isAuthenticated: function() {
                    return !!$cookies.get('authenticatedUser');
                },

                setAuthenticatedUser: function(user) {
                    $cookies.put('authenticatedUser', JSON.stringify(user));
                    $rootScope.authenticatedUser = user;
                },

                unauthenticated: function() {
                    $cookies.remove('authenticatedUser');
                    delete $rootScope.authenticatedUser;
                }


            };

            return Authentication;


        });

})();