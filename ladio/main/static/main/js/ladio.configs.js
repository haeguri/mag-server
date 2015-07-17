(function() {
    'use strict';
    
    angular.module('ladio.configs', [])

    .config(function(
            $interpolateProvider,
            $httpProvider,
            $resourceProvider
        )
        {
            $resourceProvider.defaults.stripTrailingSlashes = false;

            $interpolateProvider.startSymbol('{$');
            $interpolateProvider.endSymbol('$}');

            $httpProvider.interceptors.push(function($rootScope, $q, $cookies) {
              return {
                request: function(config) {

                    var pattern = /^https?:\/\/ladiobc.s3/.test(config.url);
                    if (pattern == true) {
                        delete config.headers.Authorization;
                    }

                  return config;
                },
                response: function(response) {

                 return response;
                }
             }
            });
        });
})();