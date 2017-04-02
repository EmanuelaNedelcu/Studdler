package com.example.studdler;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }



    public void showNewExam(View view) {
        Intent intent = new Intent(this, NewExam.class);
        startActivity(intent);
    }

    public void showPastExams(View view) {
        Intent intent = new Intent(this, PastExams.class);
        startActivity(intent);
    }
}
