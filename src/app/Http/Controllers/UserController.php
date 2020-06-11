<?php

namespace App\Http\Controllers;

use App\Model\User;
use App\Model\plan;
use App\Model\subscription;
use App\Model\transaction;
use Illuminate\Http\Request;
use Validator;
use Carbon\Carbon;

class UserController extends Controller
{
    public function plan() {
        return plan::all();
    }

    public function user() {
        return User::all();
    }

    public function create(Request $request) {
            $rules = [
                'name' => 'required',
                'email' => 'required|email',
            ];
    
            $validator = Validator::make($request->all(), $rules);
    
            if($validator->fails()){
                return response()->json($validator->errors(), 400);
            }
    
            $order = User::create($request->all());

            $user = new User;

            $user->save();
    
            return response()->json($order, 201);

    }

    public function subscribe(Request $request) {

        $rules = [
            'subscription_name' => 'required',
            'plan_id' => 'required',
            'user_id' => 'required',
            'active' => 'required',
            'start_time' => 'required',
            'subscription_cost' => 'required'
        ];

        $validator = Validator::make($request->all(), $rules);

        if($validator->fails()){
            return response()->json($validator->errors(), 400);
        }

        $sub = new subscription;

        $sub->subscription_name = $request->subscription_name;
        $sub->plan_id = $request->plan_id;
        $sub->user_id = $request->user_id;
        $sub->active = true;
        $date = $request->start_time;
        $sub->start_time = Carbon::createFromFormat('d-m-Y', $date)->format('Y-m-d');
        $sub->subscription_cost = $request->subscription_cost;

        if ($sub->save()) {

            if ($sub->active == 1) {
                $status = 'active';
            }

            else {
                $status = 'Expired';
            }

            $subExpire = Carbon::parse( $sub->start_time)->addDays(30);

            $expire = $subExpire->format('l jS \\of F Y h:i:s A');

            $sub_summary = ' Your subscription plan is active: 
                              with subscription plan: '.$sub->subscription_name.'
                              and cost: '.$sub->subscription_cost.'
                              Status: '.$status.'
                              Your subscription expires in: '.$expire.' ';

            $order = json_encode($sub_summary);

            return response()->json($sub_summary, 201);

        }

    }
}
