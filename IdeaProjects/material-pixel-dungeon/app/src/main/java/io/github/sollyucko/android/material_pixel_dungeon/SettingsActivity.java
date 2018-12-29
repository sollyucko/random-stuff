package io.github.sollyucko.android.material_pixel_dungeon;

import android.app.ActionBar;
import android.content.res.Configuration;
import android.os.Build;
import android.os.Bundle;
import android.preference.PreferenceActivity;
import android.widget.Toolbar;

import java.util.List;

import static io.github.sollyucko.android.Utils.isGivenSize;

public class SettingsActivity extends PreferenceActivity {
	@Override
	public boolean isValidFragment(String name) {
		return name.startsWith(this.getClass().getCanonicalName() + "$");
	}
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		
		ActionBar actionBar = this.getActionBar();
		
		if (actionBar == null && Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
			this.setActionBar(new Toolbar(this));
			actionBar = this.getActionBar();
		}
		
		if (actionBar != null) {
			actionBar.setDisplayHomeAsUpEnabled(true);
			actionBar.show();
		}
	}
	
	@Override
	public boolean onIsMultiPane() {
		return isGivenSize(this, Configuration.SCREENLAYOUT_SIZE_XLARGE);
	}
	
	@Override
	public void onBuildHeaders(List<Header> target) {
		this.loadHeadersFromResource(R.xml.pref, target);
	}

//	public static class GeneralPreferenceFragment extends PreferenceFragmentDefaults {
//		static {
//			prefXML = R.xml.pref_general;
//			preferenceKeys = new String[]{"example_text", "example_list"};
//		}
//	}
}
