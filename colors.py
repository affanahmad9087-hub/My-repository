import tkinter as tk
import customtkinter as ctk
import pyperclip
import json
import os
import colorsys

# Performance Optimization: Global appearance settings
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class LuminaElite(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Window Configuration ---
        self.title("LUMINA ELITE // ULTIMATE DESIGN SYSTEM")
        self.geometry("1400x900")
        
        # --- State Management ---
        self.DATA_FILE = "lumina_elite_state.json"
        self.library = []
        self.current_hex = "#6366F1"
        self._debounce_id = None # Used to keep the UI smooth
        
        self.load_state()
        self.setup_ui()
        self.update_all_logic(force=True)

    def setup_ui(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- 1. PRO SIDEBAR (Left) ---
        self.sidebar = ctk.CTkFrame(self, width=350, corner_radius=0, fg_color=("#F5F5F7", "#0D0D0D"))
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        # Header
        ctk.CTkLabel(self.sidebar, text="LUMINA ELITE", font=("Inter", 24, "bold"), text_color="#6366F1").pack(pady=(40, 5))
        
        # Color Display (Glass Card)
        self.glass_card = ctk.CTkFrame(self.sidebar, height=200, width=280, corner_radius=20, 
                                       fg_color=("#FFFFFF", "#1A1A1A"), border_width=1)
        self.glass_card.pack(pady=20, padx=30)
        self.swatch = ctk.CTkFrame(self.glass_card, width=240, height=120, corner_radius=15)
        self.swatch.pack(pady=20, padx=20)

        # Hex Entry
        self.hex_entry = ctk.CTkEntry(self.sidebar, font=("JetBrains Mono", 22, "bold"), 
                                      justify="center", height=55, corner_radius=12)
        self.hex_entry.pack(fill="x", padx=30, pady=10)
        self.hex_entry.bind("<Return>", lambda e: self.update_from_hex())

        # Performance-Optimized Sliders
        self.slider_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        self.slider_frame.pack(fill="x", padx=30, pady=20)
        
        self.r_val, self.g_val, self.b_val = tk.IntVar(value=99), tk.IntVar(value=102), tk.IntVar(value=241)
        self.create_smooth_slider("R", self.r_val, "#FF4B4B")
        self.create_smooth_slider("G", self.g_val, "#2ECC71")
        self.create_smooth_slider("B", self.b_val, "#3498DB")

        # System Controls
        self.theme_toggle = ctk.CTkSegmentedButton(self.sidebar, values=["Dark", "Light"], command=self.change_theme)
        self.theme_toggle.set("Dark")
        self.theme_toggle.pack(pady=20)

        self.save_btn = ctk.CTkButton(self.sidebar, text="ADD TO PROJECT", height=50, corner_radius=12,
                                     font=("Inter", 14, "bold"), command=self.add_to_library)
        self.save_btn.pack(side="bottom", fill="x", padx=30, pady=40)

        # --- 2. MAIN WORKSPACE (Right) ---
        self.workspace = ctk.CTkTabview(self, corner_radius=20, fg_color="transparent")
        self.workspace.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        
        self.tab_viz = self.workspace.add("Visualizer")
        self.tab_theory = self.workspace.add("Palette Builder")
        self.tab_lib = self.workspace.add("Library & Export")

        self.setup_visualizer_tab()
        self.setup_theory_tab()
        self.setup_library_tab()

    def create_smooth_slider(self, label, var, color):
        f = ctk.CTkFrame(self.slider_frame, fg_color="transparent")
        f.pack(fill="x", pady=5)
        ctk.CTkLabel(f, text=label, width=20, font=("JetBrains Mono", 12)).pack(side="left")
        s = ctk.CTkSlider(f, from_=0, to=255, variable=var, button_color=color, 
                         button_hover_color=color, command=self.on_slider_move)
        s.pack(side="right", fill="x", expand=True, padx=(10, 0))

    def on_slider_move(self, _):
        # Debouncing: If a previous update is scheduled, cancel it.
        if self._debounce_id:
            self.after_cancel(self._debounce_id)
        # Schedule the UI update for 10ms later to keep the slider movement smooth
        self._debounce_id = self.after(10, self.update_all_logic)

    def update_all_logic(self, force=False):
        r, g, b = self.r_val.get(), self.g_val.get(), self.b_val.get()
        new_hex = f"#{r:02x}{g:02x}{b:02x}".upper()
        self.current_hex = new_hex

        # Visual Feedback (Immediate)
        self.swatch.configure(fg_color=new_hex)
        self.hex_entry.delete(0, tk.END)
        self.hex_entry.insert(0, new_hex)
        
        # Batch update sub-components
        self.update_mockup(new_hex, r, g, b)
        self.update_harmonies(r, g, b)

    def update_mockup(self, hex_c, r, g, b):
        # Mockup dynamic colors
        self.mock_cta.configure(fg_color=hex_c)
        self.mock_badge.configure(fg_color=hex_c)
        
        # Calculate contrast for text
        lum = (0.299 * r + 0.587 * g + 0.114 * b) / 255
        text_color = "black" if lum > 0.6 else "white"
        self.mock_cta.configure(text_color=text_color)

    def setup_visualizer_tab(self):
        # Component Gallery
        scroll = ctk.CTkScrollableFrame(self.tab_viz, fg_color="transparent")
        scroll.pack(fill="both", expand=True)

        ctk.CTkLabel(scroll, text="SYSTEM COMPONENTS", font=("Inter", 18, "bold")).pack(anchor="w", pady=20)
        
        self.viz_container = ctk.CTkFrame(scroll, corner_radius=20, fg_color=("#FFFFFF", "#141414"), border_width=1)
        self.viz_container.pack(fill="x", padx=10, pady=10)

        # Mockup Elements
        self.mock_badge = ctk.CTkLabel(self.viz_container, text="NEW FEATURE", corner_radius=10, 
                                       font=("Inter", 10, "bold"), text_color="white", width=100)
        self.mock_badge.pack(pady=(30, 10))

        self.mock_title = ctk.CTkLabel(self.viz_container, text="Interface Preview", font=("Inter", 32, "bold"))
        self.mock_title.pack()

        self.mock_cta = ctk.CTkButton(self.viz_container, text="Primary Action", height=45, corner_radius=10)
        self.mock_cta.pack(pady=30)

    def setup_theory_tab(self):
        self.theory_scroll = ctk.CTkScrollableFrame(self.tab_theory, fg_color="transparent")
        self.theory_scroll.pack(fill="both", expand=True)
        self.harmony_grid = ctk.CTkFrame(self.theory_scroll, fg_color="transparent")
        self.harmony_grid.pack(fill="x", pady=20)

    def update_harmonies(self, r, g, b):
        for widget in self.harmony_grid.winfo_children():
            widget.destroy()
        
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        
        # Harmony Definitions
        schemes = [
            ("Complementary", (h + 0.5) % 1.0),
            ("Analogous L", (h - 0.08) % 1.0),
            ("Analogous R", (h + 0.08) % 1.0),
            ("Triadic L", (h + 0.33) % 1.0),
            ("Triadic R", (h + 0.66) % 1.0)
        ]

        for i, (name, hue) in enumerate(schemes):
            rgb = colorsys.hsv_to_rgb(hue, s, v)
            hex_c = '#%02x%02x%02x' % (int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))
            
            card = ctk.CTkFrame(self.harmony_grid, width=180, corner_radius=15)
            card.grid(row=0, column=i, padx=10, pady=10)
            ctk.CTkFrame(card, height=100, width=150, fg_color=hex_c, corner_radius=10).pack(pady=10, padx=10)
            ctk.CTkLabel(card, text=name, font=("Inter", 12, "bold")).pack()
            ctk.CTkButton(card, text=hex_c.upper(), font=("JetBrains Mono", 10), height=25, 
                          fg_color="transparent", command=lambda c=hex_c: pyperclip.copy(c)).pack(pady=10)

    def setup_library_tab(self):
        self.lib_scroll = ctk.CTkScrollableFrame(self.tab_lib, fg_color="transparent")
        self.lib_scroll.pack(fill="both", expand=True)
        
        header = ctk.CTkFrame(self.lib_scroll, fg_color="transparent")
        header.pack(fill="x", pady=10)
        ctk.CTkButton(header, text="Export JSON", command=self.export_json).pack(side="left", padx=5)
        ctk.CTkButton(header, text="Clear Project", fg_color="#FF4B4B", hover_color="#D13636", 
                      command=self.clear_lib).pack(side="left", padx=5)

        self.lib_grid = ctk.CTkFrame(self.lib_scroll, fg_color="transparent")
        self.lib_grid.pack(fill="both", expand=True)

    def update_from_hex(self):
        val = self.hex_entry.get().strip()
        if val.startswith('#'): val = val[1:]
        try:
            r, g, b = int(val[0:2], 16), int(val[2:4], 16), int(val[4:6], 16)
            self.r_val.set(r); self.g_val.set(g); self.b_val.set(b)
            self.update_all_logic()
        except:
            self.hex_entry.delete(0, tk.END)
            self.hex_entry.insert(0, "INVALID")

    def add_to_library(self):
        if self.current_hex not in self.library:
            self.library.insert(0, self.current_hex)
            if len(self.library) > 100: self.library.pop()
            self.render_library()
            self.save_state()

    def render_library(self):
        for widget in self.lib_grid.winfo_children():
            widget.destroy()
        for i, h in enumerate(self.library):
            row, col = divmod(i, 6)
            card = ctk.CTkFrame(self.lib_grid, corner_radius=12)
            card.grid(row=row, column=col, padx=8, pady=8)
            ctk.CTkButton(card, text="", fg_color=h, width=120, height=60, corner_radius=8, 
                          command=lambda v=h: pyperclip.copy(v)).pack(padx=5, pady=5)
            ctk.CTkLabel(card, text=h, font=("JetBrains Mono", 10)).pack()

    def change_theme(self, mode):
        ctk.set_appearance_mode(mode)

    def export_json(self):
        pyperclip.copy(json.dumps(self.library))
        
    def clear_lib(self):
        self.library = []
        self.render_library()
        self.save_state()

    def save_state(self):
        with open(self.DATA_FILE, "w") as f:
            json.dump(self.library, f)

    def load_state(self):
        if os.path.exists(self.DATA_FILE):
            try:
                with open(self.DATA_FILE, "r") as f:
                    self.library = json.load(f)
            except: self.library = []
        self.after(200, self.render_library)

if __name__ == "__main__":
    app = LuminaElite()
    app.mainloop()