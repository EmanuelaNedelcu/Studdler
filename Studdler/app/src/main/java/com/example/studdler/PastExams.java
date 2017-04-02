package com.example.studdler;

import android.content.Context;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.List;

public class PastExams extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_past_exams);

        // Getting a reference to the listview in our layout
        ListView brandsList = (ListView) findViewById(R.id.brands_list);

        // create a collection of data that we want to show
        List<Brand> brands = new ArrayList<>();
        brands.add(new Brand("Apple"));
        brands.add(new Brand("Microsoft"));
        brands.add(new Brand("Google"));
        brands.add(new Brand("Facebook"));

        brandsList.setAdapter(new BrandsListAdapter(PastExams.this, brands));
    }

    // a java class that represents data for one row of a listview
    // the name = the name of the brand
    // the image integer = the reference to the drawable in the resource folder
    class Brand {
        private String name;

        Brand(String name) {
            this.name = name;
        }

        public String getName() {
            return name;
        }
    }

    // the adapter is the component that glues data and listview together
    class BrandsListAdapter extends ArrayAdapter<Brand> {

        private final List<Brand> data;

        public BrandsListAdapter(Context context, List<Brand> data) {
            super(context, 0, data);
            this.data = data;
        }

        // this method is called for each row of the listview
        @Override public View getView(int position, View convertView, ViewGroup parent) {
            // The layoutinflater "parses" the brands_row.xml layout so we can use give it to the listview
            LayoutInflater inflater = LayoutInflater.from(getContext());
            View row = inflater.inflate(R.layout.brands_row, parent, false);

            TextView brandsName = (TextView) row.findViewById(R.id.brands_name);

            // retrieve the item in our collection for the position that the listview is parsing right now
            Brand brand = data.get(position);
            // set the data to our views
            brandsName.setText(brand.getName());

            return row;
        }

        @Override public int getCount() {
            return data.size();
        }
    }
}
