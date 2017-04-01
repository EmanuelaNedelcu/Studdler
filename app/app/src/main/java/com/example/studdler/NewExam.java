package com.example.studdler;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Toast;

public class NewExam extends AppCompatActivity {


    private String[] arraySpinner;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_new_exam);

        this.arraySpinner = new String[] {
                "Easy", "Medium", "Hard"
        };
        Spinner s = (Spinner) findViewById(R.id.spinner);
        ArrayAdapter<String> adapter = new ArrayAdapter<String>(this,
                android.R.layout.simple_spinner_item, arraySpinner);
        s.setAdapter(adapter);
    }


    public void saveNewExam(View view) {


        EditText name_field   = (EditText)findViewById(R.id.editText);
        EditText grade_field   = (EditText)findViewById(R.id.editText2);
        EditText min_field   = (EditText)findViewById(R.id.min_hours);
        EditText max_field   = (EditText)findViewById(R.id.max_hours);
        Spinner s = (Spinner)findViewById(R.id.spinner);


        String difficulty = s.getSelectedItem().toString();
        String name = name_field.getText().toString();
        String grade = grade_field.getText().toString();
        String min = min_field.getText().toString();
        String max = max_field.getText().toString();


        Toast toast = Toast.makeText(NewExam.this, "Saved!", Toast.LENGTH_SHORT);
        toast.show();

        Intent intent = new Intent(this, MainActivity.class);
        startActivity(intent);
    }
}
