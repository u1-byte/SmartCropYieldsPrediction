package com.u1.capstoneproject.ui.splash

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.u1.capstoneproject.databinding.ActivityOnBoardingBinding
import com.u1.capstoneproject.ui.setup_location.LocationSetupActivity

class OnBoardingActivity : AppCompatActivity() {

    private lateinit var binding: ActivityOnBoardingBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)

        binding.btnNext.setOnClickListener {
            startActivity(Intent(this@OnBoardingActivity, LocationSetupActivity::class.java))
            finish()
        }
    }
}