import tkinter as tk

class HelpUIManager:
    def __init__(self, root_frame):
        self.root_frame = root_frame
        self.configure_window()
        self.create_help_content()

    def configure_window(self):
        # Window configurations
        self.root_frame.geometry("800x600")
        self.root_frame.configure(bg="#a9927d")

    def create_help_content(self):
        # Create a Text widget
        text_widget = tk.Text(self.root_frame, wrap=tk.WORD, bg="#a9927d", fg="#5c5241", font=("Helvetica", 12))
        
        # Define tags for styling
        text_widget.tag_configure("heading", font=("Helvetica", 16, "bold"))
        text_widget.tag_configure("subheading", font=("Helvetica", 14, "bold"))
        
        # Insert content with tags
        text_widget.insert(tk.END, "1. Environment Button:\n", "heading")
        text_widget.insert(tk.END, "Description:\n", "subheading")
        text_widget.insert(tk.END, "The first 4 buttons (top 4) are environment buttons to configure google tab links, apps to launch, and a Spotify playlist/album to play.\n\n")
        text_widget.insert(tk.END, "Configuration:\n", "subheading")
        text_widget.insert(tk.END, "- Change its name.\n")
        text_widget.insert(tk.END, "- Copy and paste hyperlinks to open up in your browser.\n")
        text_widget.insert(tk.END, "- Choose apps you'd like to auto-launch by clicking the 'Add' button.\n")
        text_widget.insert(tk.END, "- Copy and paste a Spotify link to play music.\n")
        text_widget.insert(tk.END, "- Edit or delete links or apps by double-clicking on them inside the list box.\n\n")
        
        text_widget.insert(tk.END, "2. Kill All Button:\n", "heading")
        text_widget.insert(tk.END, "Description:\n", "subheading")
        text_widget.insert(tk.END, "Force quits all common apps you keep open. If a specific app is not open when this app is clicked, it will not break anything. It'll just ignore that app since it doesn't see that it's active.\n\n")
        text_widget.insert(tk.END, "Configuration:\n", "subheading")
        text_widget.insert(tk.END, "- Click on 'Add App' to select the apps you'd like to force quit.\n\n")
        
        text_widget.insert(tk.END, "3. Clean Desktop:\n", "heading")
        text_widget.insert(tk.END, "Description:\n", "subheading")
        text_widget.insert(tk.END, "Moves all files to a 'trash_me' folder. You can select files and folders you specifically do not want to be moved or deleted.\n\n")
        text_widget.insert(tk.END, "Configuration:\n", "subheading")
        text_widget.insert(tk.END, "- Click 'Add File/Folder' to ignore and select which you are adding.\n\n")
        
        text_widget.insert(tk.END, "About the App:\n", "heading")
        text_widget.insert(tk.END, "The purpose of this app is to help you customize your environments. It aims to enhance productivity by cutting out repetitive tasks.\n\n")
        text_widget.insert(tk.END, "Known Issue:\n", "subheading")
        text_widget.insert(tk.END, "Spotify links will not play if your Spotify is not currently active. Open Spotify and play a song to register it as an active device.\n\n")
        
        text_widget.config(state=tk.DISABLED)
        text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Configure the root_frame to expand its child widgets
        self.root_frame.grid_rowconfigure(0, weight=1)
        self.root_frame.grid_columnconfigure(0, weight=1)
        
        # Use grid instead of pack for the Text widget and the Scrollbar
        text_widget.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        # Add a scrollbar
        scrollbar = tk.Scrollbar(self.root_frame, command=text_widget.yview)
        text_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")
