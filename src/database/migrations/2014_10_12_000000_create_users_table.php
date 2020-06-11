<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateUsersTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::disableForeignKeyConstraints();

        Schema::create('users', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('email')->unique();
            $table->timestamp('email_verified_at')->nullable();
            $table->string('password');
            // $table->unsignedBigInteger('plan_id');
            // $table->unsignedBigInteger('subscription_id');
            $table->rememberToken();
            $table->timestamps();

            // $table->foreign('plan_id')->references('id')->on('plan');
            // $table->foreign('subscription_id')->references('id')->on('subscription');
            // $table->foreign('transaction_id')->references('id')->on('transaction');
            // $table->softDeletes();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('users');
    }
}
