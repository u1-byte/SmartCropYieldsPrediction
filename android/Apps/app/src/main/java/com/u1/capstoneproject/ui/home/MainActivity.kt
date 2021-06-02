package com.u1.capstoneproject.ui.home

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.u1.capstoneproject.databinding.ActivityMainBinding
import com.u1.capstoneproject.ui.about.AboutActivity
import com.u1.capstoneproject.ui.setup_location.LocationSetupActivity

class MainActivity : AppCompatActivity() {

    private lateinit var binding : ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)

        binding.info.setOnClickListener {
            startActivity(Intent(this@MainActivity, AboutActivity::class.java))
        }

        binding.settings.setOnClickListener {
            startActivity(Intent(this@MainActivity, LocationSetupActivity::class.java))
        }


    }
}