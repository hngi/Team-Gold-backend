<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:api')->get('/user', function (Request $request) {
    return $request->user();
});

Route::group(['prefix' => 'v1'], function () {

    /*Get all Plan*/
    Route::get('plan', 'UserController@plan');

    /*Get all Users*/
    Route::get('user', 'UserController@user');

    /*Run subscriptions for users*/
    Route::post('subscribe', 'UserController@subscribe');

    /*Create Users*/
    Route::post('create', 'UserController@create');

});
