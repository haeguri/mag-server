(function() {

    'use strict';

    angular.module('ladio.controllers', [])

    .controller('MasterController', function (
            $rootScope,
            $scope
        ) {

            $scope.master = {};
            $rootScope.user = {};

            $rootScope.$on('$stateChangeSuccess', function(event, toState, toParams, fromState, fromParams) {
                $scope.master.header_image = {
                    "background-image": "url(" + "'http://ironsummitmedia.github.io/startbootstrap-clean-blog/img/home-bg.jpg'" + ')'
                };
                $scope.master.header_title = "Fashions, maketh, us";
                $scope.master.header_subtitle = "라됴";
            });

    });

})();



//$scope.master.normalLoginRequest = function() {
//     $http({
//        url: RootUrl + 'rest-auth/login/',
//        method:'POST',
//        data:{
//            'email':'admin@admin.com',
//            'password':'82307201'
//        }
//    }).then(function(response) {
//        console.log("Success normal login", response);
//        $http.defaults.headers.common['Authorization'] = 'Token ' + response.data.key;
//        $cookies.token = response.data.key;
//        $rootScope.user = response.data.user;
//        $rootScope.user.authenticated = true;
//    }, function(response) {
//        console.log("Failed common login", response);
//    });
//}
//
//// 페이습 로그인 버튼을 클릭하면 아래의 이벤트 핸들러 함수가 실행된다.
//$scope.master.facebookLoginRequest = function() {
//    // FB.login()은 페이스북 javascript SDK에 내장된 함수이다.
//    // 페이스북 로그인 다이얼로그 창이 열리고 로그인이 되면 사용자의 리소스에 접근할 수 있는 access_token을 받아올 수 있다.
//    FB.login(function(response){
//        if ( response.status == 'connected') {
//            $http({
//                // 아래의 url은 장고 써드파티 라이브러리인 rest-auth가 제공하는 뷰로 연결된다.
//                url: RootUrl + 'rest-auth/facebook/',
//                method:'POST',
//                // 페이스북 서버에서 받아온 access_token을 data로 해서 장고 서버에 로그인 요청을 한다.
//                data:{
//                    'access_token':response.authResponse.accessToken
//                }
//            /* 성공 콜백함수 */
//            }).then(function(response) {
//                console.log("Success fb login", response);
//                // 서버에서 로그인 처리가 정상 완료되면 response 인자를 통해 서버로부터 응답이 전달된다.
//                /*
//                response: {
//                        config: { ... },
//                        data: {
//                            ‘user’:{ ... },
//                            ‘token’:’ ... '
//                        },
//                    }
//                */
//                // response.data 에는 사용자 인스턴스, 그리고 토큰이 담겨있다.
//                // 이 토큰의 값을 REST framework에서 요구하는 형태의 문자열로 다시 조립해야한다.
//                var token_str = 'Token ' + response.data.key;
//
//                // 조립한 문자열을 Authorization 헤더에 추가한다.
//                // 앞으로의 모든 HTTP 요청에는 토큰 정보가 담긴 Authorization 헤더가 추가되어 전송된다.
//                $http.defaults.headers.common.Authorization = token_str;
//
//                // Authorization 헤더를 통해 장고 서버는 이 사용자가 인증된 유저인지 아닌지 구별하게 된다.
//
//                $cookies.token = response.data.key;
//                $rootScope.user = response.data.user;
//                $rootScope.user.authenticated = true;
//            }, function(response) {
//                console.log("Failed fb login Data!!", response.data);
//            });
//        } else {
//            console.log("요청 오류입니다. 다시 시도해주세요.");
//        }
//    }, {scope:'public_profile, email'});
//
//};
