/* global requirejs: true */

requirejs.config({
    baseUrl: '../../media/js/',
    paths: {
        'jquery': 'lib/jquery-3.2.1.min',
        'domReady': 'lib/require/domReady',
        'underscore': 'lib/underscore-min'
    },
    urlArgs: 'bust=' + (new Date()).getTime()
});

define([
    'jquery',
    'domReady',
    'src/utils'
], function($, domReady, utils) {
    domReady(function() {
    });
});
