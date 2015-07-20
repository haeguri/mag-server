(function() {
    'use strict';

    angular.module('ladio.controllers')

    .controller('ContentDetailController', function(
        $scope,
        $http,
        $sce,
        $stateParams,
        $timeout,
        Content
    ) {

        $scope.content_detail = {};

        Content.get({
            'content_id':$stateParams.content_id
        }, function(data) {
            $scope.content_detail.content = data;
            $scope.content_detail.content.body = $sce.trustAsHtml(data.body);

            $scope.master.header_title = data.title;
            $scope.master.header_subtitle = data.created;
            $scope.master.header_image = {"background-image":"url('" + $scope.content_detail.content.thumb_img + "')"};
        }, function(data) {
            /* error */
        });

    });
})();