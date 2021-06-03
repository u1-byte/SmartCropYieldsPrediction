package com.u1.capstoneproject.ui.setup_location

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.u1.capstoneproject.R
import com.u1.capstoneproject.databinding.ActivityLocationSetupBinding
import com.u1.capstoneproject.ui.home.MainActivity
import com.u1.capstoneproject.ui.home.MainPremiumActivity

class LocationSetupActivity : AppCompatActivity() {

    private lateinit var binding : ActivityLocationSetupBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityLocationSetupBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.btnFree.setOnClickListener {
            startActivity(Intent(this@LocationSetupActivity, MainActivity::class.java))
            finish()
        }

        binding.btnPremium.setOnClickListener {
            startActivity(Intent(this@LocationSetupActivity, MainPremiumActivity::class.java))
            finish()
        }
    }
}