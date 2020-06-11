<?php

use Illuminate\Database\Seeder;

class PlanSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        DB::table('plan')->insert([
            'plan_name' => 'Basic',
            'annual_discount' => 40,
            'cost' => 40,
        ]);
        DB::table('plan')->insert([
            'plan_name' => 'Premium',
            'annual_discount' => 90,
            'cost' => 1500,
        ]);
    }
}
