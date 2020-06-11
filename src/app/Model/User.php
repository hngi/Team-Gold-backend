<?php

namespace App\Model;

use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    protected $table = "user";

    protected $fillable = [
        'name', 'email', 
    ];

    public function subscription()
    {
        return $this->hasMany('App\model\subscription', 'subscripton_id');
    }
}
