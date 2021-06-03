package com.u1.capstoneproject.ui.setup_location

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.u1.capstoneproject.R
import com.u1.capstoneproject.databinding.ActivityLocationSetupBinding

class LocationSetupActivity : AppCompatActivity() {

    private lateinit var binding : ActivityLocationSetupBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityLocationSetupBinding.inflate(layoutInflater)
        setContentView(binding.root)
    }
}