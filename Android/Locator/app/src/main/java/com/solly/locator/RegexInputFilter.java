package com.solly.locator;


import android.text.InputFilter;
import android.text.Spanned;

import java.util.regex.Pattern;


/**
 * Copied from http://onebigfunction.com/android/2015/09/01/regex-input-filter/, then modified.
 */

public class RegexInputFilter implements InputFilter {
	public Pattern mPattern;

	public RegexInputFilter(Pattern pattern) {
		this.mPattern = pattern;
	}

	@Override
	public CharSequence filter(CharSequence source, int start, int end, Spanned dest, int dstart, int dend) {
		return this.mPattern.matcher(source).matches() ? null : "";
	}
}