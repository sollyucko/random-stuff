package io.github.sollyucko.android;

import android.content.Context;
import android.content.Intent;
import android.content.res.Configuration;
import android.media.Ringtone;
import android.media.RingtoneManager;
import android.net.Uri;
import android.os.Bundle;
import android.support.v14.preference.PreferenceFragment;
import android.support.annotation.Nullable;
import android.support.v7.preference.*;
import android.text.TextUtils;
import android.view.MenuItem;

import org.jetbrains.annotations.NotNull;

import io.github.sollyucko.android.material_pixel_dungeon.R;
import io.github.sollyucko.android.material_pixel_dungeon.SettingsActivity;

import static io.github.sollyucko.Utils.callSuperMethod;

@SuppressWarnings("WeakerAccess")
public class Utils {
	public static boolean onOptionsItemSelectedPreferenceActivity(@NotNull PreferenceFragmentCompat thisValue, @NotNull MenuItem item) {
		if (item.getItemId() == android.R.id.home) {
			thisValue.startActivity(new Intent(thisValue.getActivity(), SettingsActivity.class));
			return true;
		}
		
		return (boolean) callSuperMethod(thisValue, "onOptionsItemSelectedPreferenceActivity", item);
	}
	
	public static void bindPreferenceSummaryToValue(Preference preference) {
		preference.setOnPreferenceChangeListener((Preference preference2, Object value) -> {
			preference2.setSummary(getDescription(preference2, value));
			return true;
		});
		
		preference.setSummary(PreferenceManager.getDefaultSharedPreferences(preference.getContext()).getString(preference.getKey(), ""));
	}
	
	public static void onCreatePreferenceActivityHelper(@NotNull PreferenceFragmentCompat thisValue, int preferenceFile, @NotNull String... preferenceKeys) {
		thisValue.addPreferencesFromResource(preferenceFile);
		thisValue.setHasOptionsMenu(true);
		
		for (String preferenceKey : preferenceKeys) {
			bindPreferenceSummaryToValue(thisValue.findPreference(preferenceKey));
		}
	}
	
	public static boolean isGivenSize(@NotNull Context context, int targetSize) {
		return (context.getResources().getConfiguration().screenLayout & Configuration.SCREENLAYOUT_SIZE_MASK) >= targetSize;
	}
	
	@Nullable
	public static String getDescription(@NotNull Preference preference, @NotNull Object value) {
		
		String stringValue = value.toString();
		
		if (preference instanceof ListPreference) {
			ListPreference listPreference = (ListPreference) preference;
			int index = listPreference.findIndexOfValue(stringValue);
			return index >= 0 ? String.valueOf(listPreference.getEntries()[index]) : null;
			
		} else if (preference instanceof RingtonePreference) {
			if (TextUtils.isEmpty(stringValue)) {
				return preference.getContext().getString(R.string.pref_ringtone_silent);
			} else {
				Ringtone ringtone = RingtoneManager.getRingtone(preference.getContext(), Uri.parse(stringValue));
				return ringtone == null ? null : ringtone.getTitle(preference.getContext());
			}
		} else {
			return stringValue;
		}
	}
	
	public static class PreferenceFragmentDefaults extends PreferenceFragmentCompat {
		public static int prefXML;
		public static String[] preferenceKeys;
		
		@Override
		public void onCreate(Bundle savedInstanceState) {
			super.onCreate(savedInstanceState);
			onCreatePreferenceActivityHelper(this, prefXML, preferenceKeys);
		}
		
		@Override
		public void onCreatePreferences(Bundle bundle, String s) {

		}
		
		public boolean onOptionsItemSelected(MenuItem item) {
			return onOptionsItemSelectedPreferenceActivity(this, item);
		}
	}
}
