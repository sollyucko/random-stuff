package com.solly.midi;

import javax.sound.midi.MidiEvent;
import javax.sound.midi.MidiMessage;
import javax.sound.midi.Sequence;
import javax.sound.midi.ShortMessage;
import javax.sound.midi.Track;

public class SimpleTrack {
	public Track track;
	
	public SimpleTrack(Track track) {
		this.track = track;
	}
	
	public SimpleTrack(Sequence sequence) {
		this(sequence.createTrack());
	}
	
	public void addEvent(MidiEvent event) {
		this.track.add(event);
	}
	
	public void addEvent(MidiMessage message, long tick) {
		this.addEvent(new MidiEvent(message, tick));
	}
}
