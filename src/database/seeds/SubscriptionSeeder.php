<?php

use Illuminate\Database\Seeder;

class SubscriptionSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        DB::table('subscription')->insert([
            'name' => 'Monthly',
            'user_id' => '3',
            'plan_id' => '1',
            'active' => true,
        ]);
        DB::table('subscription')->insert([
            'name' => 'Monthly',
            'user_id' => '5',
            'plan_id' => '1',
            'active' => true,
        ]);
        DB::table('subscription')->insert([
            'name' => 'Monthly',
            'user_id' => '1',
            'plan_id' => '1',
            'active' => true,
        ]);
        DB::table('subscription')->insert([
            'name' => 'Monthly',
            'user_id' => '4',
            'plan_id' => '2',
            'active' => true,
        ]);
        DB::table('subscription')->insert([
            'name' => 'Monthly',
            'user_id' => '2',
            'plan_id' => '2',
            'active' => true,
        ]);
        DB::table('subscription')->insert([
            'name' => 'Annual',
            'user_id' => '10',
            'plan_id' => '2',
            'active' => true,
        ]);
        DB::table('subscription')->insert([
            'name' => 'Annual',
            'user_id' => '6',
            'plan_id' => '1',
            'active' => true,
        ]);
        DB::table('subscription')->insert([
            'name' => 'Annual',
            'user_id' => '7',
            'plan_id' => '2',
            'active' => true,
        ]);
        DB::table('subscription')->insert([
            'name' => 'Annual',
            'user_id' => '8',
            'plan_id' => '1',
            'active' => true,
        ]);
        DB::table('subscription')->insert([
            'name' => 'Annual',
            'user_id' => '9',
            'plan_id' => '2',
            'active' => true,
        ]);
    }
}
