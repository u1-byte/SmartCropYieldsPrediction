package com.u1.capstoneproject.ui.home

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.activity.viewModels
import com.u1.capstoneproject.databinding.ActivityMainBinding
import com.u1.capstoneproject.ui.about.AboutActivity
import com.u1.capstoneproject.ui.prediction_res.ResultActivity
import com.u1.capstoneproject.ui.setup_location.LocationSetupActivity

class MainActivity : AppCompatActivity() {

    private lateinit var binding : ActivityMainBinding

    private val viewModel: MainViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.info.setOnClickListener {
            startActivity(Intent(this@MainActivity, AboutActivity::class.java))
        }

        binding.settings.setOnClickListener {
            startActivity(Intent(this@MainActivity, LocationSetupActivity::class.java))
        }

        binding.btnCalc.setOnClickListener {
            binding.apply {
                val param1 = input1.text.toString()
                val param2 = input2.text.toString()
                val param3 = input3.text.toString()
                val param4 = input4.text.toString()
                val param5 = input5.text.toString()
                val param6 = input6.text.toString()
                val param7 = input7.text.toString()
                val param8 = input8.text.toString()
                val param9 = input9.text.toString()
                val param10 = input10.text.toString()
                val param11 = input11.text.toString()
                val param12 = input12.text.toString()
                val param13 = input13.text.toString()
                val param14 = input14.text.toString()

                when {
                    param1.isEmpty() -> {
                        input1.error = "Masih Kosong"
                    }
                    param2.isEmpty() -> {
                        input2.error = "Masih Kosong"
                    }
                    param3.isEmpty() -> {
                        input3.error = "Masih Kosong"
                    }
                    param4.isEmpty() -> {
                        input4.error = "Masih Kosong"
                    }
                    param5.isEmpty() -> {
                        input5.error = "Masih Kosong"
                    }
                    param6.isEmpty() -> {
                        input6.error = "Masih Kosong"
                    }
                    param7.isEmpty() -> {
                        input7.error = "Masih Kosong"
                    }
                    param8.isEmpty() -> {
                        input8.error = "Masih Kosong"
                    }
                    param9.isEmpty() -> {
                        input9.error = "Masih Kosong"
                    }
                    param10.isEmpty() -> {
                        input10.error = "Masih Kosong"
                    }
                    param11.isEmpty() -> {
                        input11.error = "Masih Kosong"
                    }
                    param12.isEmpty() -> {
                        input12.error = "Masih Kosong"
                    }
                    param13.isEmpty() -> {
                        input13.error = "Masih Kosong"
                    }
                    param14.isEmpty() -> {
                        input14.error = "Masih Kosong"
                    }
                    else -> {
                        viewModel.calculate(
                                param1, param2, param3, param4, param5, param6, param7,
                                param8, param9, param10, param11, param12, param13, param14)
                        getResult()
                    }
                }
            }
        }
    }

    private fun getResult(){
        alreadySet(false, 0.0)

        viewModel.getResult().observe(this,{
            val result = it.Produksi
            alreadySet(true, result)
        })
    }

    private fun alreadySet(state: Boolean, res: Double){
        if (state){
            val intent = Intent(this@MainActivity, ResultActivity::class.java)
            intent.putExtra(ResultActivity.EXTRA_RES, res)
            startActivity(intent)
        }
    }
}