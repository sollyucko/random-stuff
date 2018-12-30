package com.solly.gamesandpuzzles;


import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;


public class HomeScreen extends AppCompatActivity {
	@Override protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_home);
	}
	
	public void chessActivity(View v) {
		Intent intent = new Intent(this, ChessHomeActivity.class);
		startActivity(intent);
	}
	
	public void ticTacToeActivity(View v) {
		Intent intent = new Intent(this, TicTacToeActivity.class);
		startActivity(intent);
	}
}
