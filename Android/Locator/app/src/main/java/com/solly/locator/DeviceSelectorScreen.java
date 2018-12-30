package com.solly.locator;


import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;


public class DeviceSelectorScreen extends AppCompatActivity {
	View rootView;

/*	public void addRow(View v) {
		this.addRow();
	}

	public void addRow() {
		//this.addContentView(new EditText(this));
		LinearLayout newRow = new LinearLayout(this);
		((LinearLayout) this.rootView).addView(newRow);
		LinearLayout inputs = new LinearLayout(this);
		newRow.addView(inputs);
		ImageButton deleteButton = new ImageButton(this);
		newRow.addView(deleteButton);
	}

	public void addRow(String name, long ip, double latKey, double longKey) {

	}*/

	@Override protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		this.setContentView(R.layout.activity_device_selector_screen);
		this.rootView = this.findViewById(android.R.id.content);
	}
}
