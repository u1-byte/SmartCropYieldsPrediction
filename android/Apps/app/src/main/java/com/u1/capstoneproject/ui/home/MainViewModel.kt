package com.u1.capstoneproject.ui.home

import android.util.Log
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.u1.capstoneproject.network.api.ApiHelper
import com.u1.capstoneproject.network.data.ResponseData
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class MainViewModel: ViewModel() {

    var result = MutableLiveData<ResponseData>()

    private val apiInstance = ApiHelper.instance

    fun calculate(
            param1: String,
            param2: String,
            param3: String,
            param4: String,
            param5: String,
            param6: String,
            param7: String,
            param8: String,
            param9: String,
            param10: String,
            param11: String,
            param12: String,
            param13: String,
            param14: String
    ){
        apiInstance.getResult(
                param1.toDouble(), param2.toDouble(), param3.toDouble(), param4.toDouble(), param5.toDouble(), param6.toDouble(), param7.toDouble(),
                param8.toDouble(), param9.toDouble(), param10.toDouble(), param11.toDouble(), param12.toDouble(), param13.toDouble(), param14.toDouble()
        ).enqueue(object :Callback<ResponseData>{
            override fun onResponse(call: Call<ResponseData>, response: Response<ResponseData>) {
                if (response.isSuccessful){
                    result.postValue(response.body())
                }
            }

            override fun onFailure(call: Call<ResponseData>, t: Throwable) {
                Log.e("Fail", t.message.toString())
            }
        })
    }

    fun getResult(): LiveData<ResponseData>{
        return result
    }
}