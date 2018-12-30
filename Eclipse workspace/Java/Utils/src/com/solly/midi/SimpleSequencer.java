package com.solly.midi;

import javax.sound.midi.InvalidMidiDataException;
import javax.sound.midi.MidiSystem;
import javax.sound.midi.MidiUnavailableException;
import javax.sound.midi.Sequence;
import javax.sound.midi.Sequencer;

public class SimpleSequencer {
	public Sequencer sequencer;
	public Sequence sequence;
	
	public SimpleSequencer(Sequencer sequencer, Sequence sequence) throws InvalidMidiDataException {
		this.sequencer = sequencer;
		this.sequence = sequence;
		this.sequencer.setSequence(this.sequence);
	}
	
	public SimpleSequencer(float divisionType, int resolution) throws InvalidMidiDataException, MidiUnavailableException {
		this(MidiSystem.getSequencer(), new Sequence(divisionType, resolution));
	}
	
	public SimpleSequencer(float divisionType, int resolution, int numTracks) throws InvalidMidiDataException, MidiUnavailableException {
		this(MidiSystem.getSequencer(), new Sequence(divisionType, resolution, numTracks));
	}
}








