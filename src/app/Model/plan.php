<?php

namespace App\Model;

use Illuminate\Database\Eloquent\Model;

class plan extends Model
{
    protected $table = "plan";

    protected $fillable = [
        "plan_id", "plan_type", "plan_name", "annual_discount", "cost",
    ];
}
