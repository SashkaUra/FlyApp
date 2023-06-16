from tkinter import *
#pip install tkintermapview
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import tkintermapview
import data_base_query as dbq

class App():
    
    win_width = 800
    win_height = 600
    bg_1 = "#d4ebf2"
    fg_1 = "#17414d"
        
    def __init__(self):
        self.win = Tk()
        self.win.title("Flyhack")
        self.screen_width = self.win.winfo_screenwidth()
        self.screen_height = self.win.winfo_screenheight()
        self.center_x = int(self.screen_width/2 - (App.win_width)/2)
        self.center_y = int(self.screen_height/2 - (App.win_height)/2)
        self.win.geometry(f'{App.win_width}x{App.win_height}+{self.center_x}+{self.center_y}')
        self.win.configure(bg = App.bg_1)
        self.win.resizable(True, True)
        self.win.iconbitmap("icon.ico")
        
        self.marker_list = []
        
        """ ============== Создание стилей для надписей ================ """
        
        self.label_style_general = ttk.Style()
        self.label_style_general.configure("General.TLabel", 
                                      font="verdana 10", 
                                      foreground=App.fg_1,
                                      background=App.bg_1)

        self.label_style_H1 = ttk.Style()
        self.label_style_H1.configure("H1.TLabel", 
                                 font="verdana 15",
                                 foreground=App.fg_1,
                                 background=App.bg_1)

        self.label_style_other = ttk.Style()
        self.label_style_other.configure("Other.TLabel",
                              font="verdana 7",
                              foreground=App.fg_1,
                              background=App.bg_1)



    def download(self):
        dwnld = dbq.download_data(float(self.min_lat_entry.get()),
                            float(self.max_lat_entry.get()),
                            float(self.min_lon_entry.get()),
                            float(self.max_lon_entry.get()))
        
        showinfo(title="Downloading", message="All data was downloaded on your computer")
        
    
        
    def create_table(self):
        lst_data = dbq.show_data(float(self.min_lat_entry.get()),
                            float(self.max_lat_entry.get()),
                            float(self.min_lon_entry.get()),
                            float(self.max_lon_entry.get()))
        
        heads = ['city', 'country', 'iata', 'latitude', 'longitude']
        table = ttk.Treeview(self.bottom_frame, show="headings")
        table['columns'] = heads
        
        for header in heads:
            table.heading(header, text=header, anchor="center")
            table.column(header, width=150, anchor="center")        
        for row in lst_data:
            table.insert("", END, values=row)
        
        table.pack(expand=1, fill=BOTH, side=BOTTOM)
        """ ============== Создание вкладок ============== """
    def create_tabs(self):
        tabs = ttk.Notebook()
        tabs.pack(expand=True, fill=BOTH)

        self.tab_1 = Frame(tabs, width=App.win_width, height=App.win_height, bg=App.bg_1)
        self.tab_2 = Frame(tabs, width=App.win_width, height=App.win_height, bg=App.bg_1)
        
        self.tab_1.pack(expand=True, fill=BOTH)
        self.tab_2.pack(expand=True, fill=BOTH)

        tabs.add(self.tab_1, text = "Find an airport")
        tabs.add(self.tab_2, text = "Map")
        
        """ ============== Наполнение вкладки 'Find airports' ============== """
        
        self.main_frame_1 = Frame(self.tab_1, bg = App.bg_1, height=App.win_height, width=App.win_width)
        self.main_frame_1.pack()
        
        self.top_frame = Frame(self.main_frame_1, bg = App.bg_1, width=App.win_width, height=200)
        self.top_frame.pack(side=TOP)

        self.bottom_frame = Frame(self.main_frame_1, bg = App.bg_1, width=App.win_width, height=400)
        self.bottom_frame.pack(side=BOTTOM)
        
        self.main_label = ttk.Label(self.top_frame, text ="Welcome to Flyhack - your guide to flight industry!",
                                 style="H1.TLabel")

        self.top_frame.grid_rowconfigure(0, weight=0)
        self.main_label.grid(column=0, row=0, columnspan=5, stick="wens", padx=5, pady=5)

        """ ============== Область для ввода значений широты и долготы ============== """
        
        self.label_lat = ttk.Label(self.top_frame, text ="Latitude", style="General.TLabel")

        self.label_lat.grid(column=1, row=1)

        ttk.Label(self.top_frame, text = "Minimal:", style="Other.TLabel").grid(row=2, column=1)
        self.min_lat_entry = Entry(self.top_frame)
        self.min_lat_entry.grid(row=3, column=1)
        self.min_lat_entry.delete(0, END)
        self.min_lat_entry.insert(0, "-90.0")

        ttk.Label(self.top_frame, text = "Maximal:", style="Other.TLabel").grid(row=4, column=1)
        self.max_lat_entry = Entry(self.top_frame)
        self.max_lat_entry.grid(row=5, column=1)
        self.max_lat_entry.delete(0, END)
        self.max_lat_entry.insert(0, "90.0")

        self.label_lon = ttk.Label(self.top_frame, text ="Longitude", style="General.TLabel")

        self.label_lon.grid(column=3, row=1)

        ttk.Label(self.top_frame, text = "Minimal:", style="Other.TLabel").grid(row=2, column=3)
        self.min_lon_entry = Entry(self.top_frame)
        self.min_lon_entry.grid(row=3, column=3)
        self.min_lon_entry.delete(0, END)
        self.min_lon_entry.insert(0, "-180.0")

        ttk.Label(self.top_frame, text = "Maximal:", style="Other.TLabel").grid(row=4, column=3)
        self.max_lon_entry = Entry(self.top_frame)
        self.max_lon_entry.grid(row=5, column=3)
        self.max_lon_entry.delete(0, END)
        self.max_lon_entry.insert(0, "180.0")

        self.button_download = Button(self.top_frame, text = "Download CSV file", 
                                    width=7, height=1, fg=App.bg_1, bg=App.fg_1, bd=2,
                                    command=self.download)
        self.button_download.grid(row=6, column=2, stick="wens", pady=5, padx=5)
        
        self.button_show = Button(self.top_frame, text = "Show info below", 
                                    width=7, height=1, fg=App.bg_1, bg=App.fg_1, bd=2,
                                    command=self.create_table)
        self.button_show.grid(row=7, column=2, stick="wens", pady=5, padx=5)
        
        """ ===== Создание виджета таблицы ===== """
        
        self.table = ttk.Treeview(self.bottom_frame)
        
        """ ============== Наполнение вкладки 'Map' ============== """
        
        self.main_frame_2 = Frame(self.tab_2, bg = App.bg_1, height=App.win_height, width=App.win_width)
        self.main_frame_2.pack()
        
        self.left_frame = Frame(self.main_frame_2, bg = App.bg_1, width=200, height=App.win_width)
        self.left_frame.pack(side=LEFT)

        self.right_frame = Frame(self.main_frame_2, bg = App.bg_1, width=400, height=App.win_height)
        self.right_frame.pack(side=RIGHT)
        
        """ ============== Левый фрейм ============== """

        

        """ ===== Добавление кнопки с возможностью выбора подложки карты ===== """

        self.left_frame.grid_rowconfigure(0, weight=1)
        self.left_frame.grid_rowconfigure(1, weight=1)
        self.left_frame.grid_rowconfigure(2, weight=1)
        self.left_frame.grid_columnconfigure(0, weight=0)
        self.left_frame.grid_columnconfigure(1, weight=1)
        self.left_frame.grid_columnconfigure(2, weight=0)
        
               
        self.tile_label = ttk.Label(self.left_frame, text="Choose tile server:", style="General.TLabel")
        self.tile_label.grid(row=1, column=1, sticky='s')
        self.option_list = ["OpenStreetMap", "Google normal", "Google satellite"]
        self.var = StringVar(self.left_frame)
        self.var.set(self.option_list[0])
        self.map_option_menu = OptionMenu(self.left_frame, self.var, *self.option_list, command=self.change_map)
        self.map_option_menu.grid(row=2, column=1, sticky='n')

        """ ============== Правый фрейм ============== """
                
        """ ===== Добавление виджета с картой ===== """

        self.right_frame.grid_rowconfigure(1, weight=1)
        self.right_frame.grid_rowconfigure(0, weight=0)
        self.right_frame.grid_columnconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(1, weight=0)
        self.right_frame.grid_columnconfigure(2, weight=1)

        self.map_widget = tkintermapview.TkinterMapView(self.right_frame, width=600, height=600, corner_radius=0)
        self.map_widget.grid(row=1, rowspan=1, column=0, columnspan=3, sticky="wens", padx=5, pady=5)

        self.map_widget.set_position(59.937500, 30.308611)  
        self.map_widget.set_zoom(3)
        
        """ ===== Добавление виджета с поиском города  ===== """


        self.city_entry = Entry(self.right_frame)
        self.city_entry.insert(END, "Type city")
        self.city_entry.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)
        self.city_entry.bind("<Return>", self.search_event)
        
        self.btn_search = Button(self.right_frame, text = "Search", 
                                 width=7, height=1, fg=App.bg_1, bg=App.fg_1, bd=2, 
                                 command=self.search_event)
        self.btn_search.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        
        self.button_find = Button(self.right_frame, text="Show airport", 
                                  fg=App.bg_1, bg=App.fg_1, bd=2,
                                  command=self.set_marker)
        self.button_find.grid(row=0, column=2, sticky="w", padx=5, pady=5)
       
    """ ===== Функция для поиска нужного города на карте по данным, которые вводит пользователь ===== """

    def search_event(self, event=None):
        self.map_widget.set_address(self.city_entry.get())
        
    """ ===== Функция для установки маркера с аэропортом ===== """
        
    def set_marker(self):
        city_lst = dbq.get_city(str(self.city_entry.get()).title())
        
        for row in city_lst:
            self.marker_list.append(self.map_widget.set_marker(row[3], row[4], text=row[2]))
    
    """ ===== Функция для изменения подложки карты ===== """
    
    def change_map(self, new_map: str):
        if new_map == "OpenStreetMap":
            self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google normal":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        elif new_map == "Google satellite":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

    def execute(self):
        self.create_tabs()
        self.win.mainloop()
        
        
if __name__ == '__main__':
    app = App()
    app.execute()        
        
