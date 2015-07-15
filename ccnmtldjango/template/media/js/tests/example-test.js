/* jshint mocha: true */

var assert = require('assert');
var requirejs = require('requirejs');

describe('Array', function() {
    describe('#indexOf()', function() {
        it('should return -1 when the value is not present', function() {
            assert.equal(-1, [1, 2, 3].indexOf(5));
            assert.equal(-1, [1, 2, 3].indexOf(0));
        });
    });
});

describe('utils', function() {
    var utils = requirejs('../src/utils');
    describe('#isEven()', function() {
        it('should return true when given even numbers', function() {
            assert.equal(utils.isEven(2), true);
            assert.equal(utils.isEven(10), true);
        });

        it('should return false when given odd numbers', function() {
            assert.equal(utils.isEven(1), false);
            assert.equal(utils.isEven(5), false);
        });
    });
});
