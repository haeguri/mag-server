angular.module('ladio.controllers')

.controller('ContentListController', function(
        $scope,
        $http,
        $rootScope,
        $sce,
        $state,
        usSpinnerService,
        Content
    ) {

        $scope.index = {};

        $scope.index.printTestValue = function() {
            //console.log("TestValue in index", TestValue);
        }

        Content.query({

        }, function(data) {
            console.log("Success content query", data);
            $scope.index.content_list = data;
        }, function(data) {
            console.log("Fail content query", data);
        });

        $scope.index.goContentDetail = function(content_id) {
            console.log("Go Detail", content_id);
            $state.go('content_detail', { content_id : content_id });
        }

    });