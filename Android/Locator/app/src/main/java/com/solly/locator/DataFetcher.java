package com.solly.locator;


import com.google.android.gms.maps.model.LatLng;

import java.io.IOException;
import java.net.InetAddress;
import java.net.Socket;
import java.nio.ByteBuffer;
import java.nio.channels.SocketChannel;
import java.security.Key;
import java.security.NoSuchAlgorithmException;

import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;


/**
 * Retrieves the other phone's location.
 */

public class DataFetcher extends Data {
	public double latkey;
	public double longkey;
	public InetAddress ip;

	/**
	 * @param ip        the phone number of the phone that's being located
	 * @param latkey    the latitude encryption key
	 * @param longkey   the longitude encryption key
	 */
	public DataFetcher(InetAddress ip, double latkey, double longkey) {
		this.ip = ip;
		this.latkey = latkey;
		this.longkey = longkey;
	}

	/**
	 * @return the decoded data
	 */
	public LatLng getLocation() throws IOException, NoSuchAlgorithmException, NoSuchPaddingException, BadPaddingException, IllegalBlockSizeException {
		SocketChannel channel = new Socket(this.ip, Data.port).getChannel();
		ByteBuffer latBuffer = ByteBuffer.allocate(8); // 8 bytes in a double
		ByteBuffer longBuffer = ByteBuffer.allocate(8); // 8 bytes in a double
		channel.read(latBuffer);
		channel.read(longBuffer);
		return new LatLng(decodeLat(latBuffer.getDouble()), decodeLong(longBuffer.getDouble()));
	}

	/**
	 * @param encoded the encoded latitude
	 * @return the decoded latitude
	 */
	public double decodeLat(double encoded) throws NoSuchPaddingException, NoSuchAlgorithmException, BadPaddingException, IllegalBlockSizeException {
		Cipher cipher = Cipher.getInstance("DESede/CBC/NoPadding");
		cipher.init(Cipher.DECRYPT_MODE, new Key());
		cipher.doFinal(ByteBuffer.allocate(4).putDouble(encoded).array());
	}

	/**
	 * @param encoded the encoded longitude
	 * @return the decoded longitude
	 */
	public double decodeLong(double encoded) {
		if(this.longkey > encoded) {
			return (Double.MAX_VALUE - this.longkey) + encoded;
		}
		return encoded - this.longkey;
	}
}
