<?php

namespace App\Model;

use Illuminate\Database\Eloquent\Model;

class transaction extends Model
{
    protected $table = "transaction";

    protected $fillable = [
        "transaction_id", "user_id", "plan_id", "subscription_id", "created_at", "updated_at",
    ];
}
