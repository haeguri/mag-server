(function() {

    'use strict';

    angular.module('ladio.services')

        .factory('Content', function(RootUrl, $resource) {
            return $resource(
                RootUrl + 'api/contents/:content_id',
                null,
                { }
            );
        });

})();