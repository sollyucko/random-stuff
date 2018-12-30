package com.solly.utils;


import android.util.Xml;

import org.xmlpull.v1.XmlPullParser;
import org.xmlpull.v1.XmlPullParserException;
import org.xmlpull.v1.XmlPullParserFactory;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;


public abstract class Utils {
	public abstract static class XML {
		public static XmlPullParser parse(File file) throws FileNotFoundException, XmlPullParserException {
			XmlPullParser parser = XMLPullParserFactory.newInstance().newPullParser();
			parser.setInput(new FileReader(file));
			return parser;
		}

		public static void skip(XmlPullParser parser) throws XmlPullParserException, IOException {
			if(parser.getEventType() != XmlPullParser.START_TAG) {
				throw new IllegalStateException();
			}
			int depth = 1;
			while(depth != 0) {
				switch(parser.next()) {
					case XmlPullParser.END_TAG:
						depth--;
						break;
					case XmlPullParser.START_TAG:
						depth++;
						break;
				}
			}
		}
	}
}
