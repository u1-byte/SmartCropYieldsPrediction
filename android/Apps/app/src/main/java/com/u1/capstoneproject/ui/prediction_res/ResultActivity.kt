package com.u1.capstoneproject.ui.prediction_res

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.u1.capstoneproject.R
import com.u1.capstoneproject.databinding.ActivityResultBinding

class ResultActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_RES = "extra_res"
    }

    private lateinit var binding: ActivityResultBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityResultBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.totalRes.text = intent.getDoubleExtra(EXTRA_RES, 0.0).toString()
    }
}