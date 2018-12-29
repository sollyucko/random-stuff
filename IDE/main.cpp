#include <wx/wxprec.h>

#ifndef WX_PRECOMP

	#include <wx/wx.h>

#endif

#include <wx/dirctrl.h>
#include <experimental/filesystem>

class MyFrame : public wxFrame {
	public:
		MyFrame(const wxString& title, const wxPoint& pos, const wxSize& size)
				: wxFrame(nullptr, wxID_ANY, title, pos, size) {
			auto* vbox = new wxBoxSizer(wxVERTICAL);
			auto* hbox = new wxBoxSizer(wxHORIZONTAL);
			hbox->Add(new wxGenericDirCtrl(this, -1, std::experimental::filesystem::current_path().string()), 1, wxEXPAND | wxALL, 10);
			hbox->Add(new wxTextCtrl(this, -1, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxTE_MULTILINE), 1, wxEXPAND | wxALL, 10);
			vbox->Add(hbox, 1, wxEXPAND | wxALL, 10);
			this->SetSizer(vbox);
			this->Center();
//			auto* menuFile = new wxMenu;
//			menuFile->Append(wxID_EXIT);
//			auto* menuHelp = new wxMenu;
//			menuHelp->Append(wxID_ABOUT);
//			auto* menuBar = new wxMenuBar;
//			menuBar->Append(menuFile, "&File");
//			menuBar->Append(menuHelp, "&Help");
//			SetMenuBar(menuBar);
//			CreateStatusBar();
//			SetStatusText("Welcome to wxWidgets!");
//
//			auto* sizer = new wxBoxSizer(wxHORIZONTAL);
//			auto* panel = new wxPanel(this);
//			sizer->Add(panel, 1, wxEXPAND | wxALL, 20);
//			this->SetSizer(sizer);
//			auto* textCtrl = new wxTextCtrl(this, -1, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxTE_MULTILINE);
//
//			Bind(wxEVT_COMMAND_MENU_SELECTED, [this](wxCommandEvent&) { Close(true); }, wxID_EXIT);
//			Bind(wxEVT_COMMAND_MENU_SELECTED, [](wxCommandEvent&) {
//				wxMessageBox("This is a wxWidgets' Hello world sample",
//				             "About Hello World", wxOK);
//			}, wxID_ABOUT);
		}
};

class MyApp : public wxApp {
	public:
		bool OnInit() override {
			MyFrame* frame = new MyFrame("Hello World", wxDefaultPosition, wxDefaultSize);
			frame->Show(true);
			return true;
		}
};

wxIMPLEMENT_APP(MyApp);