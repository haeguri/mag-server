angular.module('ladio.services', [])
    .value('TestValue', {
        'test':'123123'
    })
    //.value('UrlBundle', {
    //    'StaticUrl':'staticurl',
    //    'RootUrl':'rooturl'
    //})
    .constant('ConstantTest',{
        'a':'123123',
        'b':'456456'
    })

    .constant('UrlBundle', function() {
        var current_url = window.location.href;
        var pattern = /^https?:\/\/127\.0\.0\.1|^https?:\/\/localhost/g.test(current_url);

        var StaticUrl = pattern ? '/' : 'https://ladiobc.s3-ap-northeast-1.amazonaws.com/';
        var RootUrl = pattern ? 'http://localhost:8000/' : 'http://ladio-test2-dev.elasticbeanstalk.com/';
        console.log("StaticUrl in UrlBundle", StaticUrl);
        console.log("RootUrl in UrlBundle", RootUrl);
        return {
            'StaticUrl':StaticUrl,
            'RootUrl':RootUrl
        };
    })
	.constant('RootUrl', 'http://localhost:8000/')
    //.constant('RootUrl', 'http://ladio-test2-dev.elasticbeanstalk.com/')
    //
    .constant('StaticUrl', '/');
    //.constant('StaticUrl', 'https://ladiobc.s3-ap-northeast-1.amazonaws.com/')