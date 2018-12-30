package com.solly.locator;


import java.net.InetAddress;
import java.net.NetworkInterface;
import java.net.SocketException;
import java.util.Enumeration;
import java.util.HashSet;
import java.util.Set;


/**
 * Sends this phone's location.
 */

public class DataSender extends Data {


	public Set<InetAddress> getIPAddresses() throws SocketException {
		Set<InetAddress> ips = new HashSet<>();
		for(Enumeration<NetworkInterface> netInts = NetworkInterface.getNetworkInterfaces(); netInts.hasMoreElements();) {
			for(Enumeration<InetAddress> netIntIps = netInts.nextElement().getInetAddresses(); netIntIps.hasMoreElements();) {
				ips.add(netIntIps.nextElement());
			}
		}
		return ips;
	}
}
