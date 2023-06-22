<?php

use Illuminate\Support\Facades\DB;
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('stock__codes', function (Blueprint $table) {
            $table->id();
            $table->string('name');
        });

        DB::table('stock__codes')->insert(
            array(['id'=>1,'name'=>'ACB'],['id'=>2,'name'=>'BCM'],['id'=>3,'name'=>'BID'],['id'=>4,'name'=>'BVH'],['id'=>5,'name'=>'CTG'],
                    ['id'=>6,'name'=>'FPT'],['id'=>7,'name'=>'GAS'],['id'=>8,'name'=>'GVR'],['id'=>9,'name'=>'HDB'],['id'=>10,'name'=>'HPG'])
        
        );

    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('stock__codes');
    }
};
