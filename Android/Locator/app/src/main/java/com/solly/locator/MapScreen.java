package com.solly.locator;


import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.widget.Toast;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;

import java.io.IOException;
import java.net.InetAddress;
import java.net.UnknownHostException;
import java.security.NoSuchAlgorithmException;

import javax.crypto.BadPaddingException;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;


public class MapScreen extends FragmentActivity implements OnMapReadyCallback {

	public DataFetcher dataFetcher;
	public GoogleMap map;

	@Override protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.new_activity_map_screen);
		// Obtain the SupportMapFragment and get notified when the map is ready to be used.
		SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager().findFragmentById(R.id.map);
		mapFragment.getMapAsync(this);

		try {
			this.dataFetcher = new DataFetcher(InetAddress.getByAddress(new byte[]{127, 0, 0, 1}), 0, 0); // TODO: add actual phone # and keys
		} catch(UnknownHostException e) {
			Toast.makeText(getApplicationContext(), "Invalid IP address", Toast.LENGTH_SHORT).show();
		}
	}

	/**
	 * Manipulates the map once available.
	 * This callback is triggered when the map is ready to be used.
	 * In this case, we add a marker at the spot where the other phone is, and center the map there.
	 * If Google Play services is not installed on the device, the user will be prompted to install
	 * it inside the SupportMapFragment. This method will only be triggered once the user has
	 * installed Google Play services and returned to the app.
	 */
	@Override public void onMapReady(GoogleMap googleMap) {
		map = googleMap;
	}

	public void updateLocation() throws IOException, IllegalBlockSizeException, BadPaddingException, NoSuchAlgorithmException, NoSuchPaddingException {
		if(map != null) {
			LatLng location = dataFetcher.getLocation();
			map.addMarker(new MarkerOptions().position(location)/*.title("")*/);
			map.moveCamera(CameraUpdateFactory.newLatLng(location));
		} else {
			Toast.makeText(getApplicationContext(), "Map not loaded, please try again when map loads", Toast.LENGTH_SHORT).show();
		}
	}
}
