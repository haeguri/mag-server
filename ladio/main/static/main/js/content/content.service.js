(function() {

    'use strict';

    angular.module('ladio.services')

        .factory('Content', function(UrlBundle, $resource) {

            return $resource(
                UrlBundle.RootUrl + 'api/contents/:content_id',
                null,
                { }
            );
        });

})();