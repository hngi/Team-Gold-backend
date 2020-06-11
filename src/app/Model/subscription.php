<?php

namespace App\Model;

use Illuminate\Database\Eloquent\Model;

class subscription extends Model
{
    protected $table = "subscription";

    protected $fillable = [
        "subscription_id", "subscription_name", "plan_id", "user_id", "active", "start_time", "end_time", 
    ];

    public function user() {
        return $this->belongsTo('App\Model\User', 'user_id');
    }
}
