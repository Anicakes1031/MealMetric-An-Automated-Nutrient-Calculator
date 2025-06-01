from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition,FallOutTransition,RiseInTransition,WipeTransition
from kivy.graphics import Color, RoundedRectangle,Line,Rectangle
from kivy.animation import Animation
from kivy.properties import NumericProperty
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.video import Video
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.behaviors import ButtonBehavior, DragBehavior
from kivy.uix.gridlayout import GridLayout
from datetime import datetime, timedelta
from kivymd.uix.behaviors.hover_behavior import HoverBehavior
import sqlite3
from kivy.graphics import Canvas
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
Builder.load_file('main.kv')
Window.size = (800, 480)

FOOD_NUTRITION = {
    
  #added food chicken  
    'Chicken Breast': {'protein': 0.31, 'carbs': 0.00, 'calories': 1.7, 'fats': 0.07},
    'Chicken Tenderloins': {'protein': 0.31, 'carbs': 0.00, 'calories': 1.7, 'fats': 0.07},
    'Chicken Thigh\nw/o\nSkin': {'protein': 0.23, 'carbs': 0.00, 'calories': 1.7, 'fats': 0.07},
    'Chicken Thigh\nw/\nSkin': {'protein': 0.19, 'carbs': 0.00, 'calories': 2.3, 'fats': 0.12},
    'Chicken Drumstick\nw/\nSkin': {'protein': 0.19, 'carbs': 0.00, 'calories': 2.2, 'fats': 0.12},
    'Chicken Drumstick\nw/o\nSkin': {'protein': 0.20, 'carbs': 0.00, 'calories': 1.3, 'fats': 0.10},
    'Chicken Wings\nw/o\nSkin': {'protein': 0.21, 'carbs': 0.00, 'calories': 1.7, 'fats': 0.08},
    'Chicken Wings\nw/\nSkin': {'protein': 0.19, 'carbs': 0.00, 'calories': 2.3, 'fats': 0.14},
    'Chicken Skin': {'protein': 0.09, 'carbs': 0.00, 'calories': 4.3, 'fats': 0.38},
    'Chicken Gizzard': {'protein': 0.18, 'carbs': 0.00, 'calories': 1.1, 'fats': 0.02},
    'Chicken Egg': {'protein': 6.3, 'carbs': 0.6, 'calories': 70, 'fats': 5},
   
   #added food turkey
    'Turkey Breast': {'protein': 0.29, 'carbs': 0, 'calories': 1.4, 'fats': 0.10},
    'Turkey Tenderloins': {'protein': 0.28, 'carbs': 0, 'calories': 1.4, 'fats': 0.02},
    'Turkey Thigh': {'protein': 0.26, 'carbs': 0, 'calories': 1.5, 'fats': 0.07}, 
    'Turkey Drumstick': {'protein': 0.28, 'carbs': 0, 'calories': 1.6, 'fats': 0.07},

   #added food beef
   
    'Beef Sirloin': {'protein': 0.27, 'carbs': 0.00, 'calories': 2.14, 'fats': 0.106},
    'Beef Brisket': {'protein': 0.21, 'carbs': 0.00, 'calories': 2.3, 'fats': 0.21},
    'Beef Ribeye': {'protein': 0.22, 'carbs': 0, 'calories': 2.9, 'fats': 0.29},
    'Beef T-bone': {'protein': 0.26, 'carbs': 0, 'calories': 2.6, 'fats': 0.22},
    'Beef Porterhouse': {'protein': 0.23, 'carbs': 0, 'calories': 2.5, 'fats': 0.17},
    'Beef Short\nRibs': {'protein': 0.20, 'carbs': 0, 'calories': 2.4, 'fats': 0.21},
    'Beef Chuck': {'protein': 0.22, 'carbs': 0, 'calories': 2.3, 'fats': 0.19},
    'Beef New\nYork\nStrip': {'protein': 0.23, 'carbs': 0, 'calories': 2.3, 'fats': 0.15},
    'Beef Belly': {'protein': 0.19, 'carbs': 0, 'calories': 2.7, 'fats': 0.25},
    'Beef Oxtail': {'protein': 0.18, 'carbs': 0, 'calories': 2.3, 'fats': 0.20},
    'Beef Cheeks': {'protein': 0.22, 'carbs': 0, 'calories': 2.4, 'fats': 0.18},
    'Beef Marrow': {'protein': 0.03, 'carbs': 0, 'calories': 8.5, 'fats': 0.88},
    'Beef Liver': {'protein': 0.20, 'carbs': 0, 'calories': 1.3, 'fats': 0.04},
    'Beef Heart': {'protein': 0.22, 'carbs': 0, 'calories': 1.2, 'fats': 0.05},
    'Beef Tounge': {'protein': 0.18, 'carbs': 0, 'calories': 1.4, 'fats': 0.09},
    'Beef Suet': {'protein': 0, 'carbs': 0, 'calories': 9, 'fats': 0.97},
    'Beef Bone\nBroth': {'protein': 0.02, 'carbs': 0, 'calories': 0.6, 'fats': 0.05},
    'Beef Top\nSirloin': {'protein': 0.22, 'carbs': 0.00, 'calories': 1.6, 'fats': 0.09},
    'Beef Bottom\nSirloin': {'protein': 0.21, 'carbs': 0.00, 'calories': 1.7, 'fats': 0.09},
    'Beef Top\nRound': {'protein': 0.23, 'carbs': 0.00, 'calories': 1.3, 'fats': 0.06},
    'Beef Eye\nof\nRound': {'protein': 0.23, 'carbs': 0.00, 'calories': 1.4, 'fats': 0.07},
    'Beef Flank\nSteak': {'protein': 0.22, 'carbs': 0.00, 'calories': 1.5, 'fats': 0.09},
    'Beef Skirt\nSteak': {'protein': 0.22, 'carbs': 0.00, 'calories': 1.7, 'fats': 0.13},
    'Beef Hanger\nSteak': {'protein': 0.22, 'carbs': 0.00, 'calories': 1.6, 'fats': 0.12},
    'Beef Tenderloin\nSteak': {'protein': 0.23, 'carbs': 0.00, 'calories': 1.4, 'fats': 0.08},
    'Beef Bottom\nRound': {'protein': 0.23, 'carbs': 0.00, 'calories': 1.3, 'fats': 0.07},
    
        
  #added food pork
    'Pork Belly': {'protein': 0.09, 'carbs': 0.00, 'calories': 3.0, 'fats': 0.28},
    'Pork Loin': {'protein': 0.29, 'carbs': 0.00, 'calories': 2.42, 'fats': 0.14},
    'Pork Jowl': {'protein': 0.09, 'carbs': 0.00, 'calories': 3.1, 'fats': 0.29},
    'Pork Shoulder': {'protein': 0.29, 'carbs': 0.00, 'calories': 2.4, 'fats': 0.20},
    'Pork Neck': {'protein': 0.18, 'carbs': 0.00, 'calories': 2.6, 'fats': 0.23},
    'Pork Ribs': {'protein': 0.20, 'carbs': 0.00, 'calories': 2.6, 'fats': 0.22},
    'Pork Hock': {'protein': 0.18, 'carbs': 0.00, 'calories': 2.4, 'fats': 0.21},
    'Pork Trotters': {'protein': 0.14, 'carbs': 0.00, 'calories': 2.3, 'fats': 0.22},
    'Pork Back\nFat': {'protein': 0, 'carbs': 0.00, 'calories': 8.8, 'fats': 0.96},
    'Pork Liver': {'protein': 0.20, 'carbs': 0.00, 'calories': 1.1, 'fats': 0.04},
    'Pork Heart': {'protein': 0.22, 'carbs': 0.00, 'calories': 1.2, 'fats': 0.05},
    'Pork Skin': {'protein': 0.16, 'carbs': 0.00, 'calories': 4.2, 'fats': 0.37},
    'Pork Fat': {'protein': 0, 'carbs': 0.00, 'calories': 8.8, 'fats': 0.98},
    'Pork Loin': {'protein': 0.22, 'carbs': 0.00, 'calories': 1.3, 'fats': 0.04},
    'Pork Tenderloin': {'protein': 0.22, 'carbs': 0.00, 'calories': 1.2, 'fats': 0.03},
    'Pork Ham': {'protein': 0.20, 'carbs': 0.00, 'calories': 1.3, 'fats': 0.06},
    'Pork Leg': {'protein': 0.21, 'carbs': 0.00, 'calories': 1.4, 'fats': 0.07},
    'Pork Sirloin': {'protein': 0.22, 'carbs': 0.00, 'calories': 1.4, 'fats': 0.07},
            
   #added food seafood
    'Wild Salmon': {'protein': 0.22, 'carbs': 0, 'calories': 1.5, 'fats': 0.12},
    'Farmed Salmon': {'protein': 0.20, 'carbs': 0, 'calories': 1.5, 'fats': 0.13},
    'Farmed\nTuna': {'protein': 0.23, 'carbs': 0, 'calories': 1.1, 'fats': 0.05},
    'Fresh\nTuna': {'protein': 0.23, 'carbs': 0, 'calories': 1.2, 'fats': 0.5},
    'Canned Tuna\nin\nwater': {'protein': 0.23, 'carbs': 0, 'calories': 1.1, 'fats': 0.1},
    'Canned Tuna\nin\noil': {'protein': 0.23, 'carbs': 0, 'calories': 1.3, 'fats': 0.1},
    'Fresh\nSardines': {'protein': 0.2, 'carbs': 0, 'calories': 1.2, 'fats': 0.1},
    'Canned Sardines\nin\nwater': {'protein': 0.2, 'carbs': 0, 'calories': 1.2, 'fats': 0.1},
    'Canned Sardines\nin\noil': {'protein': 0.23, 'carbs': 0, 'calories': 1.1, 'fats': 0.1},
    'Mackerel': {'protein': 0.2, 'carbs': 0, 'calories': 1.2, 'fats': 0.1},
    'Galunggong': {'protein': 0.2, 'carbs': 0, 'calories': 1.1, 'fats': 0.1},
    'Shrimp': {'protein': 0.24, 'carbs': 0, 'calories': 1.1, 'fats': 0.05},
    'Crab': {'protein': 0.2, 'carbs': 0, 'calories': 1.0, 'fats': 0.1},
    'Oyster': {'protein': 0.1, 'carbs': 0, 'calories': 0.7, 'fats': 0.02},
   
   #added vegetables, grains, and nuts
    'Lentils': {'protein': 0.09, 'carbs': 0.18, 'calories': 1.1, 'fats': 0.02},
    'Chickpeas': {'protein': 0.09, 'carbs': 0.17, 'calories': 1.1, 'fats': 0.02},
    'Black\nBeans': {'protein': 0.08, 'carbs': 0.15, 'calories': 1.1, 'fats': 0.02},
    'Tofu': {'protein': 0.08, 'carbs': 0.12, 'calories': 1.1, 'fats': 0.05},
    'Tempeh': {'protein': 0.19, 'carbs': 0.11, 'calories': 1.7, 'fats': 0.10},
    'Edamame': {'protein': 0.12, 'carbs': 0.07, 'calories': 0.9, 'fats': 0.04},
    'Peanuts': {'protein': 0.25, 'carbs': 0.04, 'calories': 5.6, 'fats': 0.49},
    'Greek\nYogurt': {'protein': 0.10, 'carbs': 0.06, 'calories': 0.6, 'fats': 0},
    'Cottage\nCheese': {'protein': 0.11, 'carbs': 0.03, 'calories': 0.7, 'fats': 0.02},
    'Cheddar\nCheese': {'protein': 0.25, 'carbs': 0.03, 'calories': 4.0, 'fats': 0.33},
    'Quickmelt\nCheese': {'protein': 0.21, 'carbs': 0.03, 'calories': 3.5, 'fats': 0.25},
    'Cream\nCheese': {'protein': 0.10, 'carbs': 0.20, 'calories': 2.0, 'fats': 0.10},
    'Edam\nCheese': {'protein': 0.26, 'carbs': 0.03, 'calories': 4.0, 'fats': 0.33},
    'Filipino\nWhite\nCheese': {'protein': 0.10, 'carbs': 0.10, 'calories': 1.5, 'fats': 0.08},
    'Parmesan\nCheese': {'protein': 0.35, 'carbs': 0.02, 'calories': 4.0, 'fats': 0.30},
    'Mozzarella\nCheese': {'protein': 0.22, 'carbs': 0.03, 'calories': 3.0, 'fats': 0.22},
    'Gouda\nCheese': {'protein': 0.25, 'carbs': 0.03, 'calories': 4.0, 'fats': 0.33},
    'Blue\nCheese': {'protein': 0.21, 'carbs': 0.02, 'calories': 4.0, 'fats': 0.28},
    

    'Spinach': {'protein': 0.029, 'carbs': 0.036, 'calories': 0.23, 'fats': 0.004},
    'Kale': {'protein': 0.029, 'carbs': 0.088, 'calories': 0.49, 'fats': 0.009},
    'Broccoli': {'protein': 0.028, 'carbs': 0.066, 'calories': 0.55, 'fats': 0.006},
    'Zucchini': {'protein': 0.012, 'carbs': 0.031, 'calories': 0.17, 'fats': 0.003},
    'Cauliflower': {'protein': 0.019, 'carbs': 0.049, 'calories': 0.25, 'fats': 0.003},
    'Quinoa': {'protein': 0.04, 'carbs': 0.07, 'calories': 0.7, 'fats': 0.02},
    'Oats': {'protein': 0.169, 'carbs': 0.663, 'calories': 3.89, 'fats': 0.069},
    'Rice': {'protein': 0.027, 'carbs': 0.282, 'calories': 1.30, 'fats': 0.003},
    'Almond\nFlour': {'protein': 0.212, 'carbs': 0.093, 'calories': 5.70, 'fats': 0.499},
    'Chia\nSeeds': {'protein': 0.17, 'carbs': 0.42, 'calories': 5.3, 'fats': 0.31},
    'Flax\nseeds': {'protein': 0.18, 'carbs': 0.29, 'calories': 5.4, 'fats': 0.42},
    'Almond\nNuts': {'protein': 0.21, 'carbs': 0.22, 'calories': 5.8, 'fats': 0.49},    
    'Walnuts': {'protein': 0.15, 'carbs': 0.14, 'calories': 6.5, 'fats': 0.65},
    'Macadamia\nNut': {'protein': 0.12, 'carbs': 0.16, 'calories': 7.2, 'fats': 0.76},
    'Sunflower\nSeeds': {'protein': 0.21, 'carbs': 0.19, 'calories': 5.8, 'fats': 0.51},
    'Pumpkin\nSeeds': {'protein': 0.24, 'carbs': 0.19, 'calories': 5.5, 'fats': 0.44},
    'Dark\nChocolate': {'protein': 0.07, 'carbs': 0.47, 'calories': 5.5, 'fats': 0.43},
    'Almond\nMilk': {'protein': 0.01, 'carbs': 0.03, 'calories': 0.4, 'fats': 0.02},
    'Soy\nMilk': {'protein': 0.03, 'carbs': 0.05, 'calories': 0.5, 'fats': 0.04},
    'Oat\nMilk': {'protein': 0.02, 'carbs': 0.07, 'calories': 0.4, 'fats': 0.04},
    'Shirataki\nNoodles': {'protein': 0, 'carbs': 0.1, 'calories': 0, 'fats': 0.2},
    'Avocado': {'protein': 0.02, 'carbs': 0.08, 'calories': 1.6, 'fats': 0.15},
    'Bell\nPeppers': {'protein': 0.02, 'carbs': 0.05, 'calories': 0.2, 'fats': 0.02},
    'Cauliflower': {'protein': 0.02, 'carbs': 0.05, 'calories': 0.25, 'fats': 0.01},
    'Green\nBeans': {'protein': 0.02, 'carbs': 0.04, 'calories': 0.3, 'fats': 0.01},
    'Cabbage': {'protein': 0.02, 'carbs': 0.04, 'calories': 0.25, 'fats': 0.01},
    'Eggplant': {'protein': 0.02, 'carbs': 0.05, 'calories': 0.2, 'fats': 0.02},
    'Okra': {'protein': 0.02, 'carbs': 0.04, 'calories': 0.3, 'fats': 0.02},
    'Bell Peppers': {'protein': 0.02, 'carbs': 0.05, 'calories': 0.2, 'fats': 0.02},
    'Tomatoes': {'protein': 0.05, 'carbs': 0.04, 'calories': 0.2, 'fats': 0.02},
    'Celery': {'protein': 0.02, 'carbs': 0.03, 'calories': 0.1, 'fats': 0.01},
    'Mushroom': {'protein': 0.02, 'carbs': 0.03, 'calories': 0.2, 'fats': 0.01},
    'Butter': {'protein': 0.01, 'carbs': 0.01, 'calories': 7, 'fats': 0.8},
    'Non Fat\nGreek\nYogurt': {'protein': 0.1, 'carbs': 0.04, 'calories': 0.6, 'fats': 0.01},
    'Whole Milk\nGreek\nYogurt': {'protein': 0.1, 'carbs': 0.04, 'calories': 1.2, 'fats': 0.1},
    'Sour Cream\n(Full Fat)': {'protein': 0.02, 'carbs': 0.03, 'calories': 0.6, 'fats': 0.05},
    'Sour Cream\n(Reduced Fat)': {'protein': 0.02, 'carbs': 0.03, 'calories': 0.4, 'fats': 0.02},

    #others
    'Oil': {'protein': 0, 'carbs': 0, 'calories': 9, 'fats': 1}

}
COOKING_METHODS_ADJUSTMENTS = {
    'Grill': {
        'protein': 0.95,  # 95% of protein retained
        'carbs': 1.0,     # 100% of carbs retained
        'calories': 0.9,  # 90% of calories retained
        'fats': 0.85      # 85% of fats retained
    },
    'Stir-Fry': {
        'protein': 1.05,  # 105% of protein retained
        'carbs': 1.0,     # 100% of carbs retained
        'calories': 1.2,  # 120% of calories retained
        'fats': 1.3       # 130% of fats retained
    },
    'Boil': {
        'protein': 1.0,   # 100% of protein retained
        'carbs': 1.0,     # 100% of carbs retained
        'calories': 0.9,  # 90% of calories retained
        'fats': 0.85     # 85% of fats retained
    },
    'Steam': {
        'protein': 1.03,  # 103% of protein retained
        'carbs': 1.0,     # 100% of carbs retained
        'calories': 0.95, # 95% of calories retained
        'fats': 0.9       # 90% of fats retained
    }
}

#BUTTONS
class ImageButton(ButtonBehavior, Image):
    pass
class RoundedButtonBack(Button, HoverBehavior):#wag galawin 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (185, 90)
        self.background_color = (0, 0, 0, 0)
        self.background_normal = ''
        self.font_name = "font/Milker.otf"
        self.font_size = 22
        self.color = (0.2, 0.2, 0.2, 1)  # Dark Gray text

        with self.canvas.before:
            self.bg_color = Color(192/255, 192/255, 192/255, 1)  # Silver Gray
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[20])

        self.bind(pos=self.update_graphics, size=self.update_graphics)

    def update_graphics(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_enter(self):
        self.bg_color.rgba = (230/255, 230/255, 230/255, 1)  # Light Gray on Hover

    def on_leave(self):
        self.bg_color.rgba = (192/255, 192/255, 192/255, 1)  # Back to Silver Gray

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (185, 90)
        self.background_color = (0, 0, 0, 0)
        self.background_normal = ''
        self.font_name = "font/Milker.otf"
        self.font_size = 22
        self.color = (139 / 255, 69 / 255, 19 / 255, 1)  # Brown text

        with self.canvas.before:
            self.bg_color = Color(237 / 255, 201 / 255, 175 / 255, 1)  # Warm Wheat Beige
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[20])

        self.bind(pos=self.update_graphics, size=self.update_graphics)

    def update_graphics(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_enter(self):
        self.bg_color.rgba = (255 / 255, 240 / 255, 200 / 255, 1)  # Lighter Beige on Hover

    def on_leave(self):
        self.bg_color.rgba = (237 / 255, 201 / 255, 175 / 255, 1)  # Back to Default Beige
class ImageButtonDO(Button, HoverBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (185, 100)
        self.background_normal = "Image/meat.png"  # Default image
        self.background_down = "Image/meat_pressed.png"  # Image when pressed
        self.font_name = "font/NEXT ART_Heavy.otf"
        self.font_size = 22
        self.color = (1, 1, 1, 1)  # White text

    def on_enter(self):
        self.background_normal = "Image/meat_pressed.png"  # Image on hover

    def on_leave(self):
        self.background_normal = "Image/meat.png"  # Default image
class ImageButtonSea(Button, HoverBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (185, 100)
        self.background_normal = "Image/sea.png"  # Default image
        self.background_down = "Image/sea_pressed.png"  # Image when pressed
        self.font_name = "font/NEXT ART_Heavy.otf"
        self.font_size = 22
        self.color = (1, 1, 1, 1)  # White text

    def on_enter(self):
        self.background_normal = "Image/sea_pressed.png"  # Image on hover

    def on_leave(self):
        self.background_normal = "Image/sea.png"  # Default image
class ImageButtonGR(Button, HoverBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (185, 100)
        self.background_normal = "Image/gr.png"  # Default image
        self.background_down = "Image/gr_pressed.png"  # Image when pressed
        self.font_name = "font/NEXT ART_Heavy.otf"
        self.font_size = 22
        self.color = (1, 1, 1, 1)  # White text

    def on_enter(self):
        self.background_normal = "Image/gr_pressed.png"  # Image on hover

    def on_leave(self):
        self.background_normal = "Image/gr.png"  # Default image
class ImageButtonVG(Button, HoverBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (185, 100)
        self.background_normal = "Image/vg.png"  # Default image
        self.background_down = "Image/vg_pressed.png"  # Image when pressed
        self.font_name = "font/NEXT ART_Heavy.otf"
        self.font_size = 22
        self.color = (1, 1, 1, 1)  # White text

    def on_enter(self):
        self.background_normal = "Image/vg_pressed.png"  # Image on hover

    def on_leave(self):
        self.background_normal = "Image/vg.png"  # Default image
class ImageButtonD(Button, HoverBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (185, 100)
        self.background_normal = "Image/d.png"  # Default image
        self.background_down = "Image/d_pressed.png"  # Image when pressed
        self.font_name = "font/NEXT ART_Heavy.otf"
        self.font_size = 22
        self.color = (1, 1, 1, 1)  # White text

    def on_enter(self):
        self.background_normal = "Image/d_pressed.png"  # Image on hover

    def on_leave(self):
        self.background_normal = "Image/d.png"  # Default image
class ImageButtonDel(Button, HoverBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (65,65)
        self.background_normal = "Image/delete.png"  # Default image
        self.background_down = "Image/delete_pressed.png"  # Image when pressed
        self.font_name = "font/NEXT ART_Heavy.otf"
        self.font_size = 22
        self.color = (1, 1, 1, 1)  # White text

    def on_enter(self):
        self.background_normal = "Image/delete_pressed.png"  # Image on hover

    def on_leave(self):
        self.background_normal = "Image/delete.png"  # Default image
class ImageButtonN(Button, HoverBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (185, 100)
        self.background_normal = "Image/n.png"  # Default image
        self.background_down = "Image/n_pressed.png"  # Image when pressed
        self.font_name = "font/NEXT ART_Heavy.otf"
        self.font_size = 22
        self.color = (1, 1, 1, 1)  # White text

    def on_enter(self):
        self.background_normal = "Image/n_pressed.png"  # Image on hover

    def on_leave(self):
        self.background_normal = "Image/n.png"  # Default image
class ImageButtonKG(Button, HoverBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (185, 90)
        self.background_normal = "Image/keto.png"  # Default image
        self.background_down = "Image/keto_pressed.png"  # Image when pressed
        self.font_name = "Arial"
        self.font_size = 22
        self.color = (1, 1, 1, 1)  # White text
class ImageButtonHP(Button, HoverBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (185, 90)
        self.background_normal = "Image/pro.png"  # Default image
        self.background_down = "Image/pro_pressed.png"  # Image when pressed
        self.font_name = "Arial"
        self.font_size = 22
        self.color = (1, 1, 1, 1)  # White text
class ImageButtonS(Button, HoverBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (100, 54)
        self.background_normal = "Image/save_pressed.png"  # Default image
        self.background_down = "Image/save.png"  # Image when pressed
        self.color = (1, 1, 1, 1)  # White text
class ImageButtonC(Button, HoverBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (100, 54)
        self.background_normal = "Image/clear_pressed.png"  # Default image
        self.background_down = "Image/clear.png"  # Image when pressed
        self.color = (1, 1, 1, 1)  # White text
class RoundedButtonB(Button, HoverBehavior):#wag den galawen may bug 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (185, 90)
        self.background_color = (0, 0, 0, 0)
        self.background_normal = ''
        self.font_name = "font/Milker.otf"
        self.font_size = 22
        self.color = (255 / 255, 209 / 255, 102 / 255, 1)  # Warm Golden Yellow

        with self.canvas.before:
            self.bg_color = Color(0 / 255, 119 / 255, 182 / 255, 1)  # Deep Turquoise Blue
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[15])

        self.bind(pos=self.update_graphics, size=self.update_graphics)

    def update_graphics(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_enter(self):
        self.bg_color.rgba = (72 / 255, 190 / 255, 255 / 255, 1)  # Light Aqua Blue on Hover

    def on_leave(self):
        self.bg_color.rgba = (0 / 255, 119 / 255, 182 / 255, 1)  # Back to Deep Turquoise Blue

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (185, 90)
        self.background_color = (0, 0, 0, 0)
        self.background_normal = ''
        self.font_name = "font/Milker.otf"
        self.font_size = 22
        self.color = (1, 1, 1, 1)  # White text

        with self.canvas.before:
            self.bg_color = Color(1, 0, 0, 1)  # Red Background
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[20])

        self.bind(pos=self.update_graphics, size=self.update_graphics)

    def update_graphics(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_enter(self):
        self.bg_color.rgba = (1, 50 / 255, 50 / 255, 1)  # Lighter Red on Hover

    def on_leave(self):
        self.bg_color.rgba = (1, 0, 0, 1)  # Back to Red

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (185, 90)
        self.background_color = (0, 0, 0, 0)
        self.background_normal = ''
        self.font_name = "font/Milker.otf"
        self.font_size = 22
        self.color = (255 / 255, 140 / 255, 0 / 255, 1)  # Carrot Orange Text

        with self.canvas.before:
            self.bg_color = Color(46 / 255, 139 / 255, 87 / 255, 1)  # Leafy Green Button
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[15])

        self.bind(pos=self.update_graphics, size=self.update_graphics)

    def update_graphics(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_enter(self):
        self.bg_color.rgba = (60 / 255, 230 / 255, 105 / 255, 1)  # Brighter Green on Hover

    def on_leave(self):
        self.bg_color.rgba = (46 / 255, 139 / 255, 87 / 255, 1)  # Back to Leafy Green

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (185, 90)
        self.background_color = (0, 0, 0, 0)
        self.background_normal = ''
        self.font_name = "font/Milker.otf"
        self.font_size = 22
        self.color = (255 / 255, 165 / 255, 0 / 255, 1)  # Butter Orange Text

        with self.canvas.before:
            self.bg_color = Color(255 / 255, 230/ 255, 210 / 255, 1)  # Creamy Milk Color
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[20])

        self.bind(pos=self.update_graphics, size=self.update_graphics)

    def update_graphics(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_enter(self):
        self.bg_color.rgba = (255 / 255, 255 / 255, 255 / 255, 1)  # Lighter Cream on Hover

    def on_leave(self):
        self.bg_color.rgba = (255 / 255, 230 / 255, 210 / 255, 1)  # Back to Milky White

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (185, 90)
        self.background_color = (0, 0, 0, 0)
        self.background_normal = ''
        self.font_name = "font/Milker.otf"
        self.font_size = 22
        self.color = (255 / 255, 245 / 255, 225 / 255, 1)  # Soft Cream Beige Text

        with self.canvas.before:
            self.bg_color = Color(160 / 255, 82 / 255, 45 / 255, 1)  # Warm Chestnut Brown
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[20])

        self.bind(pos=self.update_graphics, size=self.update_graphics)

    def update_graphics(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_enter(self):
        self.bg_color.rgba = (185 / 255, 100 / 255, 55 / 255, 1)  # Lighter Chestnut Brown on Hover

    def on_leave(self):
        self.bg_color.rgba = (160 / 255, 82 / 255, 45 / 255, 1)  # Back to Warm Chestnut Brown
class RoundedButton1(Button):
    pass
#CIRCULAR PROGRESS BAR
class ProteinProgressBar(Widget):
    protein_progress = NumericProperty(0)
    max_protein = NumericProperty(100)  # Max protein intake (adjustable)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(protein_progress=self.update_canvas, max_protein=self.update_canvas)


        # Label para sa percentage
        self.percentage_label = Label(text="0%", font_size=12, bold=True, color=(1, 1, 1, 0))
        self.add_widget(self.percentage_label)



    def update_canvas(self, *args):
        self.canvas.before.clear()
        scaled_value = (self.protein_progress / self.max_protein) * 100  # Convert progress to %

        # Set label color based on scaled value
        if scaled_value <= 100:
            self.percentage_label.color = (1, 1, 1, 1)  
        elif scaled_value <= 200:
            self.percentage_label.color = (1, 1, 1, 1)  
        elif scaled_value <= 300:
            self.percentage_label.color = (1, 1, 1, 1)  
        elif scaled_value <= 400:
            self.percentage_label.color = (1, 1, 1, 1)  
        else:
            self.percentage_label.color = (1, 1, 1, 1)  

        with self.canvas.before:
            if scaled_value > 0:
                Color(0, 0, 1, 0.5)  
                Line(circle=(self.center_x, self.center_y, self.width / 1.4, 0, min(scaled_value, 100) * 3.6), width=3)

            if scaled_value > 100:
                Color(0, 1, 0, 0.5)  
                Line(circle=(self.center_x, self.center_y, self.width / 1.4, 0, min(scaled_value - 100, 100) * 3.6), width=3)

            if scaled_value > 200:
                Color(1, 1, 0, 0.5)  
                Line(circle=(self.center_x, self.center_y, self.width / 1.4, 0, min(scaled_value - 200, 100) * 3.6), width=3)

            if scaled_value > 300:
                Color(1, 0.5, 0, 1)  
                Line(circle=(self.center_x, self.center_y, self.width / 1.4, 0, min(scaled_value - 300, 100) * 3.6), width=3)

            if scaled_value > 400:
                Color(0.7, 0, 0, 0.7)  
                Line(circle=(self.center_x, self.center_y, self.width / 1.4, 0, (scaled_value - 400) * 3.6), width=3)

        # Update label text (percentage)
        self.percentage_label.text = f"{min(int(scaled_value), 500)}%"  # Limit to 500%
        self.percentage_label.center = self.center  # Center label inside circle

    def reset_progress(self):
        self.protein_progress = 0
        self.canvas.ask_update()
class FatsProgressBar(Widget):
    fats_progress = NumericProperty(0)
    max_fats = NumericProperty(100)  # Max protein intake (adjustable)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(fats_progress=self.update_canvas, max_fats=self.update_canvas)

        # Label para sa percentage
        self.percentage_label = Label(text="0%", font_size=12, bold=True, color=(1, 1, 1, 0))
        self.add_widget(self.percentage_label)

    def update_canvas(self, *args):
        self.canvas.before.clear()
        scaled_value = (self.fats_progress / self.max_fats) * 100  # Convert progress to %

        # Set label color based on scaled value
        if scaled_value <= 100:
            self.percentage_label.color = (1, 1, 1, 1)  
        elif scaled_value <= 200:
            self.percentage_label.color = (1, 1, 1, 1)  
        elif scaled_value <= 300:
            self.percentage_label.color = (1, 1, 1, 1)  
        elif scaled_value <= 400:
            self.percentage_label.color = (1, 1, 1, 1)  
        else:
            self.percentage_label.color = (1, 1, 1, 1)  

        with self.canvas.before:
            if scaled_value > 0:
                Color(0, 0, 1, 0.5)  
                Line(circle=(self.center_x, self.center_y, self.width / 1.4, 0, min(scaled_value, 100) * 3.6), width=3)

            if scaled_value > 100:
                Color(0, 1, 0, 0.5)  
                Line(circle=(self.center_x, self.center_y, self.width / 1.4, 0, min(scaled_value - 100, 100) * 3.6), width=3)

            if scaled_value > 200:
                Color(1, 1, 0, 0.5)  
                Line(circle=(self.center_x, self.center_y, self.width / 1.4, 0, min(scaled_value - 200, 100) * 3.6), width=3)

            if scaled_value > 300:
                Color(1, 0.5, 0, 1)  
                Line(circle=(self.center_x, self.center_y, self.width / 1.4, 0, min(scaled_value - 300, 100) * 3.6), width=3)

            if scaled_value > 400:
                Color(0.7, 0, 0, 0.7)  
                Line(circle=(self.center_x, self.center_y, self.width / 1.4, 0, (scaled_value - 400) * 3.6), width=3)
        # Update label text (percentage)
        self.percentage_label.text = f"{min(int(scaled_value), 500)}%"  # Limit to 500%
        self.percentage_label.center = self.center  # Center label inside circle

    def reset_progress(self):
        self.fats_progress = 0
        self.canvas.ask_update()
class CarbsProgressBar(Widget):
    carbs_progress = NumericProperty(0)
    max_carbs = NumericProperty(100)  # Max protein intake (adjustable)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(carbs_progress=self.update_canvas, max_carbs=self.update_canvas)

        # Label para sa percentage
        self.percentage_label = Label(text="0%", font_size=12, bold=True, color=(1, 1, 1, 0))
        self.add_widget(self.percentage_label)

    def update_canvas(self, *args):
        self.canvas.before.clear()
        scaled_value = (self.carbs_progress / self.max_carbs) * 100  # Convert progress to %

        # Set label color based on scaled value
        if scaled_value <= 100:
            self.percentage_label.color = (1, 1, 1, 1)  
        elif scaled_value <= 200:
            self.percentage_label.color = (1, 1, 1, 1)  
        elif scaled_value <= 300:
            self.percentage_label.color = (1, 1, 1, 1)  
        elif scaled_value <= 400:
            self.percentage_label.color = (1, 1, 1, 1)  
        else:
            self.percentage_label.color = (1, 1, 1, 1)  

        with self.canvas.before:
            if scaled_value > 0:
                Color(0, 0, 1, 0.5)  
                Line(circle=(self.center_x, self.center_y, self.width / 1.4, 0, min(scaled_value, 100) * 3.6), width=3)

            if scaled_value > 100:
                Color(0, 1, 0, 0.5)  
                Line(circle=(self.center_x, self.center_y, self.width / 1.4, 0, min(scaled_value - 100, 100) * 3.6), width=3)

            if scaled_value > 200:
                Color(1, 1, 0, 0.5)  
                Line(circle=(self.center_x, self.center_y, self.width / 1.4, 0, min(scaled_value - 200, 100) * 3.6), width=3)

            if scaled_value > 300:
                Color(1, 0.5, 0, 1)  
                Line(circle=(self.center_x, self.center_y, self.width / 1.4, 0, min(scaled_value - 300, 100) * 3.6), width=3)

            if scaled_value > 400:
                Color(0.7, 0, 0, 0.7)  
                Line(circle=(self.center_x, self.center_y, self.width / 1.4, 0, (scaled_value - 400) * 3.6), width=3)
        # Update label text (percentage)
        self.percentage_label.text = f"{min(int(scaled_value), 500)}%"  # Limit to 500%
        self.percentage_label.center = self.center  # Center label inside circle

    def reset_progress(self):
        self.carbs_progress = 0
        self.canvas.ask_update()
class CalProgressBar(Widget):
    calories_progress = NumericProperty(0)
    max_calories = NumericProperty(1000)  # Max protein intake (adjustable)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(calories_progress=self.update_canvas, max_calories=self.update_canvas)

        # Label para sa percentage
        self.percentage_label = Label(text="0%", font_size=12, bold=True, color=(1, 1, 1, 0))
        self.add_widget(self.percentage_label)

    def update_canvas(self, *args):
        self.canvas.before.clear()
        scaled_value = (self.calories_progress / self.max_calories) * 100  # Convert progress to %

        # Set label color based on scaled value
        if scaled_value <= 100:
            self.percentage_label.color = (1, 1, 1, 1)  
        elif scaled_value <= 200:
            self.percentage_label.color = (1, 1, 1, 1)  
        elif scaled_value <= 300:
            self.percentage_label.color = (1, 1, 1, 1)  
        elif scaled_value <= 400:
            self.percentage_label.color = (1, 1, 1, 1)  
        else:
            self.percentage_label.color = (1, 1, 1, 1)  

        with self.canvas.before:
            if scaled_value > 0:
                Color(0, 0, 1, 0.5)  
                Line(circle=(self.center_x, self.center_y, self.width / 1.4, 0, min(scaled_value, 100) * 3.6), width=3)

            if scaled_value > 100:
                Color(0, 1, 0, 0.5)  
                Line(circle=(self.center_x, self.center_y, self.width / 1.4, 0, min(scaled_value - 100, 100) * 3.6), width=3)

            if scaled_value > 200:
                Color(1, 1, 0, 0.5)  
                Line(circle=(self.center_x, self.center_y, self.width / 1.4, 0, min(scaled_value - 200, 100) * 3.6), width=3)

            if scaled_value > 300:
                Color(1, 0.5, 0, 1)  
                Line(circle=(self.center_x, self.center_y, self.width / 1.4, 0, min(scaled_value - 300, 100) * 3.6), width=3)

            if scaled_value > 400:
                Color(0.7, 0, 0, 0.7)  
                Line(circle=(self.center_x, self.center_y, self.width / 1.4, 0, (scaled_value - 400) * 3.6), width=3)
        # Update label text (percentage)
        self.percentage_label.text = f"{min(int(scaled_value), 500)}%"  # Limit to 500%
        self.percentage_label.center = self.center  # Center label inside circle

    def reset_progress(self):
        self.calories_progress = 0
        self.canvas.ask_update()
#LAYOUT PARA MAKITA UI NG MGA NUTRIENTS NG FOODS
class MonitoringArea(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total_nutrients = {'protein': 0, 'carbs': 0, 'calories': 0, 'fats': 0}
        self.total_weight = 0
        self.food_entries = []

    def update_monitor(self, food_name, calculated_nutrition=None, weight=0):
        if calculated_nutrition:
            self.total_nutrients['protein'] = round(self.total_nutrients['protein'] + calculated_nutrition['protein'], 2)
            self.total_nutrients['carbs'] = round(self.total_nutrients['carbs'] + calculated_nutrition['carbs'], 2)
            self.total_nutrients['calories'] = round(self.total_nutrients['calories'] + calculated_nutrition['calories'], 2)
            self.total_nutrients['fats'] = round(self.total_nutrients['fats'] + calculated_nutrition['fats'], 2)
            self.total_weight = round(self.total_weight + weight, 2)

            self.food_entries.append({
                'food_name': food_name,
                'weight': weight,
                'protein': calculated_nutrition['protein'],
                'carbs': calculated_nutrition['carbs'],
                'calories': calculated_nutrition['calories'],
                'fats': calculated_nutrition['fats']
            })

            new_entry = (
                f"{food_name}\n"
                f"   Protein: {calculated_nutrition['protein']:.0f}g\n"
                f"   Carbs: {calculated_nutrition['carbs']:.0f}g\n"
                f"   Calories: {calculated_nutrition['calories']:.0f} kcal\n"
                f"   Fats: {calculated_nutrition['fats']:.0f}g\n"
                f"Weight:{weight}g\n\n"
            )

            # Debugging output to ensure we have the correct ids
            print(f"Updating UI with entry: {new_entry}")
            monitor_label = self.ids.get("monitor_label")
            monitor_box = self.ids.get("monitor_box")

            if monitor_label:
                monitor_label.text += new_entry
            else:
                print("Error: monitor_label not found!")

            if monitor_box:
                monitor_box.height = monitor_box.minimum_height
            else:
                print("Error: monitor_box not found!")

            self.update_total_display()
        
            Clock.schedule_once(lambda dt: self.scroll_to_bottom(), 0.1)

    def scroll_to_bottom(self):
        scrollview = self.ids.get("my_scrollview")
        if scrollview:
            scrollview.scroll_y = 1
        else:
            print("Error: scrollview not found!")

    def update_total_display(self):
        """Updates the total nutrients and weight on the UI"""

        labels = {
            "protein_label": "[size=20]{:.2f}[/size][size=15]g[/size]".format(self.total_nutrients['protein']),
            "carb_label": "[size=20]{:.2f}[/size][size=15]g[/size]".format(self.total_nutrients['carbs']),
            "fat_label": "[size=20]{:.2f}[/size][size=15]g[/size]".format(self.total_nutrients['fats']),
            "cal_label": "[size=20]{:.0f}[/size][size=15] kcal[/size]".format(self.total_nutrients['calories']),
            "total_label": "[size=25]{:.2f}[/size][size=20]g[/size]".format(self.total_weight)
        }

        for label, value in labels.items():
            if hasattr(self.ids, label):
                self.ids[label].markup = True  # Enable markup para gumana ang [size=]
                self.ids[label].text = value
            else:
                print(f"Error: {label} not found!")

        self.ids.protein_progress.protein_progress = self.total_nutrients['protein']
        self.ids.protein_label.text = f"[size=20]{int(self.total_nutrients['protein'])}[/size][size=15]g[/size]"

        self.ids.carbs_progress.carbs_progress = self.total_nutrients['carbs']
        self.ids.carb_label.text = f"[size=20]{int(self.total_nutrients['carbs'])}[/size][size=15]g[/size]"

        self.ids.calories_progress.calories_progress = self.total_nutrients['calories']
        self.ids.cal_label.text = f"[size=20]{int(self.total_nutrients['calories'])}[/size][size=15]kcal[/size]"

        self.ids.fats_progress.fats_progress = self.total_nutrients['fats']
        self.ids.fat_label.text = f"[size=20]{int(self.total_nutrients['fats'])}[/size][size=15]g[/size]"


    def clear_data(self, instance=None):
        print("Clearing data...")  # Debugging print
        self.total_nutrients = {'protein': 0, 'carbs': 0, 'calories': 0, 'fats': 0}
        self.total_weight = 0

        # Check kung tama ang `id`
        if hasattr(self.ids, 'monitor_label'):
            self.ids.monitor_label.text = ""
        else:
            print("monitor_label not found in ids!")  # Debugging print

        self.update_total_display()

    def save_data(self):
        """Isave ang food entry sa database"""
        if not self.food_entries:
            print("❌ Walang pagkain na isasave!")  # Debugging
            return

        meal_type = self.get_meal_type()
        date_today = datetime.now().strftime("%Y-%m-%d")

        conn = sqlite3.connect("food_monitoring.db")
        cursor = conn.cursor()

        print("✅ Saving food entries:", self.food_entries)  # Debugging: Ipakita ang list ng pagkain

        for entry in self.food_entries:
            cursor.execute('''INSERT INTO food_log (food_name, weight, protein, carbs, calories, fats, meal_type, date) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                       (entry['food_name'], entry['weight'], entry['protein'], entry['carbs'], 
                        entry['calories'], entry['fats'], meal_type, date_today))

        conn.commit()
        conn.close()

        print(f"✔ Data saved for {meal_type}!")

        # **Optional: I-clear ang entries pagkatapos ng save**
        self.food_entries.clear()

    def get_meal_type(self):
        """Bumabalik ng meal type depende sa oras"""
        hour = datetime.now().hour
        if hour < 10:#4-10
            return "Breakfast"
        elif hour < 20:
            return "Lunch"
        else:#5-10
            return "Dinner"
        
    def clear_progress(self):
        self.ids.protein_progress.reset_progress()  # ✅ Reset progress + kulay
        self.ids.protein_label.text = "[size=20]0[/size][size=15]g[/size]"

        self.ids.carbs_progress.reset_progress()
        self.ids.carb_label.text = "[size=20]0[/size][size=15]g[/size]"

        self.ids.calories_progress.reset_progress()
        self.ids.cal_label.text = "[size=20]0[/size][size=15]g[/size]"

        self.ids.fats_progress.reset_progress()
        self.ids.fat_label.text = "[size=20]0[/size][size=15]g[/size]"
class ProMonitoringArea(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total_nutrients = {'protein': 0, 'carbs': 0, 'calories': 0, 'fats': 0}
        self.total_weight = 0
        self.food_entries = []

    def update_monitor(self, food_name, calculated_nutrition=None, weight=0):
        if calculated_nutrition:
            self.total_nutrients['protein'] = round(self.total_nutrients['protein'] + calculated_nutrition['protein'], 2)
            self.total_nutrients['carbs'] = round(self.total_nutrients['carbs'] + calculated_nutrition['carbs'], 2)
            self.total_nutrients['calories'] = round(self.total_nutrients['calories'] + calculated_nutrition['calories'], 2)
            self.total_nutrients['fats'] = round(self.total_nutrients['fats'] + calculated_nutrition['fats'], 2)
            self.total_weight = round(self.total_weight + weight, 2)

            self.food_entries.append({
                'food_name': food_name,
                'weight': weight,
                'protein': calculated_nutrition['protein'],
                'carbs': calculated_nutrition['carbs'],
                'calories': calculated_nutrition['calories'],
                'fats': calculated_nutrition['fats']
            })

            new_entry = (
                f"{food_name}\n"
                f"   Protein: {calculated_nutrition['protein']:.0f}g\n"
                f"   Carbs: {calculated_nutrition['carbs']:.0f}g\n"
                f"   Calories: {calculated_nutrition['calories']:.0f} kcal\n"
                f"   Fats: {calculated_nutrition['fats']:.0f}g\n"
                f"Weight:{weight}g\n\n"
            )

            # Debugging output to ensure we have the correct ids
            print(f"Updating UI with entry: {new_entry}")
            monitor_label = self.ids.get("monitor_label")
            monitor_box = self.ids.get("monitor_box")

            if monitor_label:
                monitor_label.text += new_entry
            else:
                print("Error: monitor_label not found!")

            if monitor_box:
                monitor_box.height = monitor_box.minimum_height
            else:
                print("Error: monitor_box not found!")

            self.update_total_display()
        
            Clock.schedule_once(lambda dt: self.scroll_to_bottom(), 0.1)

    def scroll_to_bottom(self):
        scrollview = self.ids.get("my_scrollview")
        if scrollview:
            scrollview.scroll_y = 1
        else:
            print("Error: scrollview not found!")

    def update_total_display(self):
        """Updates the total nutrients and weight on the UI"""

        labels = {
            "protein_label": "[size=20]{:.2f}[/size][size=15]g[/size]".format(self.total_nutrients['protein']),
            "carb_label": "[size=20]{:.2f}[/size][size=15]g[/size]".format(self.total_nutrients['carbs']),
            "fat_label": "[size=20]{:.2f}[/size][size=15]g[/size]".format(self.total_nutrients['fats']),
            "cal_label": "[size=20]{:.0f}[/size][size=15] kcal[/size]".format(self.total_nutrients['calories']),
            "total_label": "[size=25]{:.2f}[/size][size=20]g[/size]".format(self.total_weight)
        }

        for label, value in labels.items():
            if hasattr(self.ids, label):
                self.ids[label].markup = True  # Enable markup para gumana ang [size=]
                self.ids[label].text = value
            else:
                print(f"Error: {label} not found!")

        self.ids.protein_progress.protein_progress = self.total_nutrients['protein']
        self.ids.protein_label.text = f"[size=20]{int(self.total_nutrients['protein'])}[/size][size=15]g[/size]"

        self.ids.carbs_progress.carbs_progress = self.total_nutrients['carbs']
        self.ids.carb_label.text = f"[size=20]{int(self.total_nutrients['carbs'])}[/size][size=15]g[/size]"

        self.ids.calories_progress.calories_progress = self.total_nutrients['calories']
        self.ids.cal_label.text = f"[size=20]{int(self.total_nutrients['calories'])}[/size][size=15]kcal[/size]"

        self.ids.fats_progress.fats_progress = self.total_nutrients['fats']
        self.ids.fat_label.text = f"[size=20]{int(self.total_nutrients['fats'])}[/size][size=15]g[/size]"


    def clear_data(self, instance=None):
        print("Clearing data...")  # Debugging print
        self.total_nutrients = {'protein': 0, 'carbs': 0, 'calories': 0, 'fats': 0}
        self.total_weight = 0

        # Check kung tama ang `id`
        if hasattr(self.ids, 'monitor_label'):
            self.ids.monitor_label.text = ""
        else:
            print("monitor_label not found in ids!")  # Debugging print

        self.update_total_display()

    def save_data(self):
        """Isave ang food entry sa database"""
        if not self.food_entries:
            print("❌ Walang pagkain na isasave!")  # Debugging
            return

        meal_type = self.get_meal_type()
        date_today = datetime.now().strftime("%Y-%m-%d")

        conn = sqlite3.connect("pro_food_monitoring.db")
        cursor = conn.cursor()

        print("✅ Saving food entries in pro:", self.food_entries)  # Debugging: Ipakita ang list ng pagkain

        for entry in self.food_entries:
            cursor.execute('''INSERT INTO food_log (food_name, weight, protein, carbs, calories, fats, meal_type, date) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                       (entry['food_name'], entry['weight'], entry['protein'], entry['carbs'], 
                        entry['calories'], entry['fats'], meal_type, date_today))

        conn.commit()
        conn.close()

        print(f"✔ Data saved for {meal_type}!")

        # **Optional: I-clear ang entries pagkatapos ng save**
        self.food_entries.clear()

    def get_meal_type(self):
        """Bumabalik ng meal type depende sa oras"""
        hour = datetime.now().hour
        if hour < 10:
            return "Breakfast"
        elif hour < 20:
            return "Lunch"
        else:
            return "Dinner"
        
    def clear_progress(self):
        self.ids.protein_progress.reset_progress()  # ✅ Reset progress + kulay
        self.ids.protein_label.text = "[size=20]0[/size][size=15]g[/size]"

        self.ids.carbs_progress.reset_progress()
        self.ids.carb_label.text = "[size=20]0[/size][size=15]g[/size]"

        self.ids.calories_progress.reset_progress()
        self.ids.cal_label.text = "[size=20]0[/size][size=15]g[/size]"

        self.ids.fats_progress.reset_progress()
        self.ids.fat_label.text = "[size=20]0[/size][size=15]g[/size]"
#CALENDAR AT TIME DATE WIDGET
class CalendarWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Label para sa kasalukuyang taon at buwan
        self.date_label = Label(
            text=f"[size=25sp][b]{datetime.now().strftime('%B, ')}[/b][/size]"
                 f"[size=25sp]{datetime.now().strftime('%Y')}[/size]",
            markup=True,
            size_hint_y=None, height="90dp",
            font_name="font/NEXT ART_Heavy.otf",
            halign="center", valign="middle",
            text_size=(None, None),
            color = (132/255, 165/255, 96/255, 1)
        )

        self.add_widget(self.date_label)

        # Grid para sa calendar
        self.grid = GridLayout(cols=7, size_hint_y=1)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.add_widget(self.grid)
        
        self.populate_calendar()

    def populate_calendar(self):
        self.grid.clear_widgets()

        # **Araw ng linggo**
        days_of_week = ["S", "M", "T", "W", "T", "F", "S"]
        for day in days_of_week:
            self.grid.add_widget(Label(
                text=day, 
                bold=True, 
                size_hint_y=None, height="40dp",
                font_name="font/NEXT ART_Heavy.otf",
                font_size="15sp"
            ))

        # Get current date
        today = datetime.now().day
        current_month = datetime.now().month
        current_year = datetime.now().year

        # First and last days of the month
        first_day_of_month = datetime(current_year, current_month, 1)
        last_day_of_month = datetime(current_year, current_month + 1, 1) - timedelta(days=1)

        # **Fix: Ayusin ang first day position sa grid**
        first_day_weekday = first_day_of_month.weekday()  # Lunes = 0, Linggo = 6
        adjusted_start = (first_day_weekday + 1) % 7  # Gawing Linggo ang unang araw

        # **Gawing blank spaces ang mga unang araw bago magsimula ang buwan**
        for _ in range(adjusted_start):
            self.grid.add_widget(Label(text="", font_name="font/NEXT ART_Heavy.otf"))

        # **Gumawa ng button para sa kasalukuyang araw at label para sa iba**
        for day in range(1, last_day_of_month.day + 1):
            if day == today:
                btn = RoundedButton1(  # ✅ Nanatili ang `RoundedButton1`
                    text=str(day),
                    font_name="font/NEXT ART_Heavy.otf",
                    font_size="15sp"
                )  
                self.grid.add_widget(btn)
            else:
                lbl = Label(
                    text=str(day),
                    font_name="font/NEXT ART_Heavy.otf",
                    font_size="15sp"
                )
                self.grid.add_widget(lbl)
class TimeDateWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.label = Label(
            font_size="18sp",            # Baguhin ang font size
            font_name="Roboto-Bold.ttf", # Baguhin ang font type (Gumamit ng existing TTF file)
            color=(1, 1, 1, 1),          # White text color
            bold=True,                   # Gawing bold
            size_hint_y=None,
            height=920,                   # Fixed height para hindi lumaki
            pos_hint={'top': 1},         # Ilagay sa taas
            halign="center",             # I-center horizontally
            valign="middle"              # I-center vertically
        )
        
        self.label.bind(size=self.label.setter('text_size'))  # Para mai-center ang text
        self.add_widget(self.label)
        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, dt):
        now = datetime.now().strftime("%A, %B %d, %Y                                                                                                                     %I:%M %p")  # Wag Pukialaman ang space
        self.label.text = f"{now}" 
#SCREENS
class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Itim na background para walang white flash
        with self.canvas.before:
            Color(1, 1, 1, 1)  # RGBA (Black)
            self.bg = Rectangle(source="Image/bg_image.jpg", pos=self.pos, size=self.size)  # Fixed background

        self.bind(size=self._update_bg, pos=self._update_bg)

    def _update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size  # Update size para hindi mawala

    def change_screen(self, screen_name, direction="up"):
        self.transition = SlideTransition(direction=direction, duration=1)  # Smooth transition
        self.current = screen_name  # Change screen
class SplashScreen(Screen):
    def on_enter(self):
        layout = FloatLayout()

        # White background widget
        self.white_bg = Widget(size_hint=(1, 1))  # This will take up the whole screen
        with self.white_bg.canvas:
            Color(0, 0, 0, 1) 
            self.rect = Rectangle(pos=self.white_bg.pos, size=self.white_bg.size)
        
        layout.add_widget(self.white_bg)

        # Video widget to play video in splash screen
        self.video = Video(source="video/ani.mp4", 
                           state='play',fit_mode="fill", size_hint=(1, 1))  # Fill the entire screen
        layout.add_widget(self.video)

        # Start the transition to the main screen after the video ends
        Clock.schedule_once(self.go_to_main, 5)  # Adjust the time according to video length

        self.add_widget(layout)

        # Bind the size event to update the background rectangle
        self.white_bg.bind(size=self.update_rect)
        self.white_bg.bind(pos=self.update_rect)

    def update_rect(self, *args):
        # Update the rectangle size and position when the widget size or position changes
        self.rect.pos = self.white_bg.pos
        self.rect.size = self.white_bg.size

    def go_to_main(self, dt):
        # Transition to the next screen using WipeTransition
        self.manager.transition =SlideTransition(duration=1, direction = 'left')  # Apply transition without specifying 'direction' directly
        self.manager.current = 'main'
class MainScreen(Screen):
    pass
class KetoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout setup
        layout = BoxLayout(orientation='vertical', padding=5)
        
        # IMAGE BUTTON PAPUNTA SA MEALSCREEN
        meal_plan_button = ImageButton(
            source="Image/down.png",  # Default image
            size_hint=(None, None),
            size=(80, 80),
            pos_hint={"center_x": 0.5, "center_y": 0.97}
        )

        # Function para palitan ang image kapag pinindot
        def on_button_press(instance):
            instance.source = "Image/down_pressed.png"

        # Function para ibalik sa original image kapag binitawan + go to meal screen
        def on_button_release(instance):
            instance.source = "Image/down.png"
            self.go_to_meal_screen(instance)

        # Bind events
        meal_plan_button.bind(on_press=on_button_press)
        meal_plan_button.bind(on_release=on_button_release)

        # Add widgets
        self.add_buttons('keto')
        layout.add_widget(TimeDateWidget()) 
        self.add_widget(layout)
        self.add_widget(meal_plan_button)

        
    def on_touch_up(self, touch):
        print(f"Swipe distance: {touch.dx}")  # Debugging output
        
        if touch.dx > 10:  # Swipe pakanan
            self.manager.transition = SlideTransition(direction="right")
            self.manager.current = "main"
        
        return super().on_touch_up(touch)
        

#MGA DEFINE ITO PARA GUMANA ANG MGA BACK BUTTONS
    def go_to_meal_screen(self, instance):
        app = App.get_running_app()
        
        app.root.transition.direction = "down"
        app.root.transition.duration = 0.5  
        
        app.root.current = "MealScreen"

#ADD BUTTONS ITO SA KETOSCREEN
    def add_buttons(self, button_type):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        if button_type == 'keto':
            self.add_keto_buttons()

        elif button_type == 'fish_section':
            self.add_fish_buttons()

        elif button_type == 'meat_section':
            self.add_meat_buttons()

        elif button_type == 'vegetable_section':
            self.add_vegetable_buttons()

        elif button_type == 'grain_section':
            self.add_grain_buttons()

        elif button_type == 'nuts_section':
            self.add_nuts_buttons()

        elif button_type == 'dairy_section':
            self.add_dairy_buttons()
    def add_keto_buttons(self):
        buttons_area = self.ids.buttons_area
        buttons_area.add_widget(ImageButtonDO(text='Meat', on_press=lambda x: self.add_buttons('meat_section')))
        buttons_area.add_widget(ImageButtonSea(text='Seafood', on_press=lambda x: self.add_buttons('fish_section')))
        buttons_area.add_widget(ImageButtonVG(text='Vegetables', on_press=lambda x: self.add_buttons('vegetable_section')))
        buttons_area.add_widget(ImageButtonGR(text='Grains', on_press=lambda x: self.add_buttons('grain_section')))
        buttons_area.add_widget(ImageButtonD(text='Dairy', on_press=lambda x: self.add_buttons('dairy_section')))
        buttons_area.add_widget(ImageButtonN(text='Nuts', on_press=lambda x: self.add_buttons('nuts_section')))

#ADD BUTTONS ITO SA LAHAT NG FOOD GROUPS
    def add_meat_buttons(self):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        buttons_area.add_widget(ImageButtonDO(text='Chicken', on_press=lambda x: self.meat_section('Chicken')))
        buttons_area.add_widget(ImageButtonDO(text='Beef', on_press=lambda x: self.meat_section('Beef')))
        buttons_area.add_widget(ImageButtonDO(text='Pork', on_press=lambda x: self.meat_section('Pork')))
        buttons_area.add_widget(ImageButtonDO(text='Turkey', on_press=lambda x: self.meat_section('Turkey')))
        buttons_area.add_widget(ImageButtonDO(text='Back', on_press=lambda x: self.add_buttons('keto')))     
    def meat_section(self, meat_type):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        meat_parts = {
            'Chicken': ['Breast', 'Thigh\nw/\nSkin', 'Thigh\nw/o\nSkin', 'Drumstick\nw/\nSkin', 'Drumstick\nw/o\nSkin', 'Wings\nw/\nSkin', 'Wings\nw/o\nSkin', 'Skin', 'Gizzard', 'Egg'],
            'Beef': ['Brisket', 'T-bone', 'Ribeye','Porterhouse', 'Short\nRibs', 'Chuck', 'New\nYork\nStrip', 'Belly', 'Oxtail' , 'Cheeks', 'Marrow', 'Liver', 'Heart', 'Tounge', 'Suet', 'Bone\nBroth', 'Top\nSirloin', 'Bottom\nSirloin', 'Top\nRound', 'Eye\nof\nRound', 'Flank\nSteak', 'Skirt\nSteak', 'Hanger\nSteak', 'Tenderloin\nSteak', 'Bottom\nRound' ],
            'Pork': ['Belly', 'Loin', 'Jowl', 'Shoulder', 'Neck', 'Ribs', 'Hock', 'Trotters', 'Back\nFat', 'Liver', 'Heart', 'Skin', 'Fat', 'Tenderloin', 'Ham', 'Leg', 'Sirloin' ],
            'Turkey': ['Tenderloins', 'Thigh', 'Drumstick',]
        }

        for part in meat_parts.get(meat_type, []):
            buttons_area.add_widget(ImageButtonDO(text=part, on_press=lambda x, p=part: self.add_cooking_method_meat(f"{meat_type} {p}")))

        buttons_area.add_widget(ImageButtonDO(text='Back to\nMeat', on_press=lambda x: self.add_buttons('meat_section'))) 
    def add_fish_buttons(self):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        fish = ['Salmon', 'Tuna', 'Sardines', 'Mackerel', 'Galunggong', 'Shrimp', 'Crab', 'Oyster']
        fish_with_cuts = {'Salmon', 'Tuna', 'Sardines'}  # Mga isdang may cuts

        for item in fish:
            if item in fish_with_cuts:
                buttons_area.add_widget(ImageButtonSea(text=item, on_press=lambda x, i=item: self.fish_section(i)))
            else:
                buttons_area.add_widget(ImageButtonSea(text=item, on_press=lambda x, i=item: self.add_cooking_method_fish(i)))

        buttons_area.add_widget(ImageButtonSea(text='Back to\nKeto', on_press=lambda x: self.add_buttons('keto')))
    def fish_section(self, fish_type):
       
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        fish_parts = {
            'Salmon': ['Wild\nSalmon', 'Farmed\nSalmon'],
            'Tuna': ['Fresh\nTuna', 'Farmed\nTuna', 'Canned Tuna\nin oil','Canned Tuna\nin water'],
            'Sardines': ['Canned\nSardines\nin water', 'Canned\nSardines\nin oil', 'Fresh\nSardines'],
            
        }

        for part in fish_parts.get(fish_type, []):
            buttons_area.add_widget(ImageButtonSea(text=part, on_press=lambda x, p=part: self.add_cooking_method_fish(f"{fish_type} {p}")))

        buttons_area.add_widget(ImageButtonSea(text='Back to\nFish', on_press=lambda x: self.add_buttons('fish_section')))
    def add_vegetable_buttons(self):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        vegetables = ['Spinach', 'Avocado', 'Broccoli', 'Bell\nPeppers', 'Cauliflower', 'Green\nBeans', 'Cabbage', 'Eggplant', 'Okra', 'Tomatoes', 'Celery', 'Mushroom', 'Kale', 'Zucchini']
        for vegetable in vegetables:
            buttons_area.add_widget(ImageButtonVG(text=vegetable, on_press=lambda x, v=vegetable: self.add_cooking_method_veg(v)))
        
        buttons_area.add_widget(ImageButtonVG(text='Back to\nKeto', on_press=lambda x: self.add_buttons('keto')))
    def add_grain_buttons(self):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        grains = ['Rice', 'Quinoa', 'Oats', 'Shirataki\nNoodles']
        for grain in grains:
            buttons_area.add_widget(ImageButtonGR(text=grain, on_press=lambda x, g=grain: self.add_cooking_method_grain(g)))
        
        buttons_area.add_widget(ImageButtonGR(text='Back to\nKeto', on_press=lambda x: self.add_buttons('keto'))) 
    def add_nuts_buttons(self): 
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        nuts = ['Peanuts', 'Almond\nFlour', 'Chia\nSeeds', 'Flax\nSeeds', 'Almond\nNuts', 'Walnuts', 'Macadamia\nNut', 'Sunflower\nSeeds', 'Pumpkin\nSeeds']
        for nuts in nuts:
            buttons_area.add_widget(ImageButtonN(text=nuts, on_press=lambda x, n=nuts: self.add_cooking_method_nuts(n)))
        
        buttons_area.add_widget(ImageButtonN(text='Back to\nKeto', on_press=lambda x: self.add_buttons('keto')))
    def add_dairy_buttons(self):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        dairy = ['Greek\nYogurt', 'Cottage\nCheese', 'Cheddar\nCheese', 'Quickmelt\nCheese', 'Cream \nCheese', 'Edam\nCheese', 'Filipino\nWhite\nCheese', 'Parmesan\nCheese', 'Mozzarella\nCheese',
                  'Gouda\nCheese', 'Blue\nCheese', 'Butter', 'Non Fat\nGreek\nYogurt', 'Whole Milk\nGreek\nYogurt', 'Sour Cream\n(Full Fat)', 'Sour Cream\n(Reduced Fat)']
        for item in dairy:
            buttons_area.add_widget(ImageButtonD(text=item, on_press=lambda x, i=item: self.add_cooking_method_dairy(i)))
        
        buttons_area.add_widget(ImageButtonD(text='Back to\nKeto', on_press=lambda x: self.add_buttons('keto')))

#COOKING METHOD LAHAT NG KLASE NG FOOD 
    def add_cooking_method_fish(self, fish_part):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        cooking_methods = ['Stir-Fry', 'Boil', 'Steam', 'Grill']
        for method in cooking_methods:
            buttons_area.add_widget(ImageButtonSea(text=method, on_press=lambda x, m=method: self.prompt_grams(fish_part, m)))
        buttons_area.add_widget(ImageButtonSea(text='Back', on_press=lambda x: self.add_fish_buttons()))
    def add_cooking_method_meat(self, meat_part):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        cooking_methods = ['Stir-Fry', 'Boil', 'Steam', 'Grill']
        for method in cooking_methods:
            buttons_area.add_widget(ImageButtonDO(text=method, on_press=lambda x, m=method: self.prompt_grams(meat_part, m)))
        buttons_area.add_widget(ImageButtonDO(text='Back', on_press=lambda x: self.meat_section(meat_part.split()[0])))
    def add_cooking_method_veg(self, meat_part):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        cooking_methods = ['Stir-Fry', 'Boil', 'Steam', 'Grill']
        for method in cooking_methods:
            buttons_area.add_widget(ImageButtonVG(text=method, on_press=lambda x, m=method: self.prompt_grams(meat_part, m)))
        buttons_area.add_widget(ImageButtonVG(text='Back', on_press=lambda x: self.add_vegetable_buttons()))
    def add_cooking_method_nuts(self, meat_part):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()
        cooking_methods = ['Stir-Fry', 'Boil', 'Steam', 'Grill']
        for method in cooking_methods:
            buttons_area.add_widget(ImageButtonN(text=method, on_press=lambda x, m=method: self.prompt_grams(meat_part, m)))
        
        buttons_area.add_widget(ImageButtonN(text='Back', on_press=lambda x: self.add_nuts_buttons()))
    def add_cooking_method_grain(self, meat_part):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        cooking_methods = ['Stir-Fry', 'Boil', 'Steam', 'Grill']
        for method in cooking_methods:
            buttons_area.add_widget(ImageButtonGR(text=method, on_press=lambda x, m=method: self.prompt_grams(meat_part, m)))

        buttons_area.add_widget(ImageButtonGR(text='Back', on_press=lambda x: self.add_grain_buttons()))
    def add_cooking_method_dairy(self, meat_part):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        cooking_methods = ['Stir-Fry', 'Boil', 'Steam']
        for method in cooking_methods:
            buttons_area.add_widget(ImageButtonD(text=method, on_press=lambda x, m=method: self.prompt_grams(meat_part, m)))

        buttons_area.add_widget(ImageButtonD(text='Back', on_press=lambda x: self.add_dairy_buttons()))

#COMPUTATION NG NUTRIENTS
    def prompt_grams(self, food_name, cooking_method):
        popup_layout = BoxLayout(orientation='vertical')
        label = Label(text=f'Enter grams for {food_name} ({cooking_method})')
        input_field = TextInput(multiline=False)
        submit_button = Button(text='Submit', on_press=lambda x: self.calculate_nutrition(food_name, cooking_method, input_field.text))

        popup_layout.add_widget(label)
        popup_layout.add_widget(input_field)
        popup_layout.add_widget(submit_button)

        popup = Popup(title='Input Grams', content=popup_layout, size_hint=(0.6, 0.4))
        submit_button.bind(on_press=lambda x: popup.dismiss())
        popup.open()
    def calculate_nutrition(self, food_name, cooking_method, grams):
        try:
            grams = float(grams)
            if food_name in FOOD_NUTRITION:
                nutrition = FOOD_NUTRITION[food_name]

                # Apply cooking method adjustments
                if cooking_method in COOKING_METHODS_ADJUSTMENTS:
                    adjustment = COOKING_METHODS_ADJUSTMENTS[cooking_method]
                    calculated_nutrition = {
                        'protein': round(nutrition['protein'] * grams * adjustment['protein'], 2),
                        'carbs': round(nutrition['carbs'] * grams * adjustment['carbs'], 2),
                        'calories': round(nutrition['calories'] * grams * adjustment['calories'], 2),
                        'fats': round(nutrition['fats'] * grams * adjustment['fats'], 2),
                    }

                    # Add oil for stir-fry method
                    if cooking_method == 'Stir-Fry':
                        oil_nutrition = FOOD_NUTRITION['Oil']
                        calculated_nutrition['calories'] += (oil_nutrition['calories'] * 15)
                        calculated_nutrition['fats'] += (oil_nutrition['fats'] * 15)
                   
                    # Additional adjustments for Grilling
                    elif  cooking_method == 'Grill':
                        # Water loss adjustment for protein
                        water_loss_percentage = 0.09  # 9% water loss
                        calculated_nutrition['protein'] = calculated_nutrition['protein'] / (1 - water_loss_percentage)

                        # Fat loss adjustment
                        fat_loss_percentage = 0.15  # 15% fat loss
                        calculated_nutrition['fats'] = calculated_nutrition['fats'] * (1 - fat_loss_percentage)

                        # Calories adjustment due to fat loss
                        lost_fat = nutrition['fats'] * grams * fat_loss_percentage
                        calculated_nutrition['calories'] -= lost_fat * 9  # 9 kcal per gram of fat
                    
                    # Additional adjustments for boiling
                    elif cooking_method == 'Boil':
                        # Assume minimal nutrient loss for simplicity
                        # You can adjust this based on specific food or cooking conditions
                        nutrient_retention_percentage = 0.95  # 95% nutrient retention
                        calculated_nutrition['protein'] *= nutrient_retention_percentage
                        calculated_nutrition['carbs'] *= nutrient_retention_percentage
                        calculated_nutrition['fats'] *= nutrient_retention_percentage
                        calculated_nutrition['calories'] *= nutrient_retention_percentage
                    
                    # Additional adjustments for steaming
                    elif cooking_method == 'Steam':
                        # Assume minimal nutrient loss for steaming
                        nutrient_retention_percentage = 0.98  # 98% nutrient retention
                        calculated_nutrition['protein'] *= nutrient_retention_percentage
                        calculated_nutrition['carbs'] *= nutrient_retention_percentage
                        calculated_nutrition['fats'] *= nutrient_retention_percentage
                        calculated_nutrition['calories'] *= nutrient_retention_percentage

                else:
                    # If no specific adjustment, use the base values
                    calculated_nutrition = {
                        'protein': round(nutrition['protein'] * grams, 2),
                        'carbs': round(nutrition['carbs'] * grams, 2),
                        'calories': round(nutrition['calories'] * grams, 2),
                        'fats': round(nutrition['fats'] * grams, 2),
                    }

                self.ids.monitor_area.update_monitor(f"{food_name}({cooking_method})", calculated_nutrition, grams)
        except ValueError:
            pass    
    def add_grams(self, food_name):
        """Prompt the user to enter grams for the selected food."""
        # Create the label for the title
        title_label = Label(text=f"Enter Grams for {food_name}", halign='center')
        title_label.bind(size=title_label.setter('text_size'))  # Automatically adjust the text size

        # Create the input field for grams
        input_field = TextInput(hint_text="Enter grams", multiline=False)

        # Create a confirm button
        confirm_button = Button(text="Confirm", size_hint=(1, 0.3))
    
        # Create the layout to hold the title, input field, and button
        layout = BoxLayout(orientation='vertical', padding=[10, 10], spacing=10)
        layout.add_widget(title_label)
        layout.add_widget(input_field)
        layout.add_widget(confirm_button)

        # Create the popup
        input_popup = Popup(title="", content=layout, size_hint=(0.6, 0.3), auto_dismiss=False)
    
        # Bind events
        confirm_button.bind(on_release=lambda x: self.process_grams(input_popup, input_field.text, food_name))
        input_field.bind(on_text_validate=lambda x: self.process_grams(input_popup, input_field.text, food_name))

        # Open the popup
        input_popup.open()
    def process_grams(self, popup, grams_text, food_name):
        """Process the input grams and add it to the nutrient calculations."""
        try:
            grams = float(grams_text)  # Convert text input to float
            if food_name in FOOD_NUTRITION:
               nutrition_per_100g = FOOD_NUTRITION[food_name]
               nutrition = {key: nutrition_per_100g[key] * grams / 100 for key in nutrition_per_100g}
            
               # Update monitoring area with new nutrient values
               self.ids.monitor_area.update_monitor(food_name, nutrition)
            
            popup.dismiss()  # Close the popup after processing
        except ValueError:
            print("Invalid input! Please enter a valid number.")  # Handle invalid input
 
#CONNECTED TO SA MONITORING AREA
    def update_monitor(self, button_instance):
        monitor_area = self.ids.monitor_area
        monitor_area.update_monitor(button_instance.text)
class MealScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()
        back = ImageButton(source="Image/mealdown.png", size_hint=(None, None), size=(80, 80), pos_hint={"center_x": 0.5, "center_y": 0.03})
        back.bind(on_press=self.go_back)
        layout.add_widget(back)
        self.add_widget(layout)
    
    def on_enter(self):
        self.load_meal_data()

    breakfast_data = []  # List to store breakfast data
    lunch_data = []      # List to store lunch data
    dinner_data = []  

    def load_meal_data(self, instance=None):
        """I-load ang pagkain para sa bawat meal type"""
        conn = sqlite3.connect("food_monitoring.db")
        cursor = conn.cursor()

        meal_types = ["Breakfast", "Lunch", "Dinner"]
        meal_logs = {
            "Breakfast": self.ids.breakfast_log,
            "Lunch": self.ids.lunch_log,
            "Dinner": self.ids.dinner_log
        }

        for meal_type in meal_types:
        # ✅ **GET `id` FROM DATABASE**
            cursor.execute("SELECT id, food_name, weight, protein, fats, carbs, calories FROM food_log WHERE meal_type = ?", (meal_type,))
            meals = cursor.fetchall()
            meal_logs[meal_type].clear_widgets()

            # **Adjust height dynamically**
            meal_logs[meal_type].height = max(40, len(meals) * 50)

            for meal in meals:
                # ✅ **Gamitin ang tamang index**
                meal_id = meal[0]  # First column is `id`
                food_name = meal[1]
                weight = meal[2]
                protein = meal[3] if len(meal) > 3 else 0
                fats = meal[4] if len(meal) > 4 else 0
                carbs = meal[5] if len(meal) > 5 else 0
                calories = meal[6] if len(meal) > 6 else 0

                meal_row = BoxLayout(size_hint_y=None, height=80)

                meal_label = Label(
                    text=f"[b]{food_name}[/b] - {weight:.0f}g\n"
                        f"      Protein: {protein:.0f}g"
                        f"      Fats: {fats:.0f}g\n"
                        f"      Carbs: {carbs:.0f}g"
                        f"      Calories: {calories:.0f} kcal",
                    markup=True,
                    size_hint_x=2,
                    size_hint_y=None,
                    height=100,  
                    text_size=(meal_logs[meal_type].width - 90, None),
                    halign="left",
                    valign="middle"  # ✅ Para nasa gitna ng Label ang text
                )

                # ✅ **Delete Button - Dapat `meal_id` ang ipasa**
                delete_btn = ImageButtonDel(
                    size_hint_x=0.1,
                    size_hint_y=0.1
                )
                delete_btn.bind(on_press=lambda btn, meal_id=meal_id: self.delete_meal(meal_id))

                meal_row.add_widget(meal_label)
                meal_row.add_widget(delete_btn)
                meal_logs[meal_type].add_widget(meal_row)

        conn.close()



    def go_back(self, instance):
        app = App.get_running_app()
        
        # Gumamit ng SlideTransition na may duration
        
        transition = SlideTransition(duration=1,direction="up")  # 0.5 seconds
        app.root.transition = transition
        
        # Palitan ang screen
        app.root.current = "KetoScreen" 

    def delete_meal(self, meal_id):
        """Tanggalin ang meal sa database"""
        conn = sqlite3.connect("food_monitoring.db")
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM food_log WHERE id=?", (meal_id,))
        conn.commit()
        conn.close()

        # **I-reload ang meal data para mawala sa UI**
        self.load_meal_data()
class ProteinScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout setup
        layout = BoxLayout(orientation='vertical', padding=5)
        
        # IMAGE BUTTON PAPUNTA SA MEALSCREEN
        meal_plan_button = ImageButton(
            source="Image/down.png",  # Default image
            size_hint=(None, None),
            size=(80, 80),
            pos_hint={"center_x": 0.5, "center_y": 0.97}
        )

        # Function para palitan ang image kapag pinindot
        def on_button_press(instance):
            instance.source = "Image/down_pressed.png"

        # Function para ibalik sa original image kapag binitawan + go to meal screen
        def on_button_release(instance):
            instance.source = "Image/down.png"
            self.go_to_promeal_screen(instance)

        # Bind events
        meal_plan_button.bind(on_press=on_button_press)
        meal_plan_button.bind(on_release=on_button_release)

        # Add widgets
        self.add_buttons('protein')
        layout.add_widget(TimeDateWidget()) 
        self.add_widget(layout)
        self.add_widget(meal_plan_button)

    def on_touch_up(self, touch):
        print(f"Swipe distance: {touch.dx}")  # Debugging output
        
        if touch.dx > 10:  # Swipe pakanan
            self.manager.transition = SlideTransition(direction="right")
            self.manager.current = "main"
        
        return super().on_touch_up(touch)

    #MGA DEFINE ITO PARA GUMANA ANG MGA BACK BUTTONS
    def go_to_promeal_screen(self, instance):
        app = App.get_running_app()
        
        app.root.transition.direction = "down"
        app.root.transition.duration = 0.5  
        
        app.root.current = "ProMealScreen"
    def go_to_Main(self, dt):
        self.manager.transition = SlideTransition(direction='right', duration=1)
        self.manager.current = 'main'    

    def add_buttons(self, button_type):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        if button_type == 'protein':
            self.add_protein_buttons()

        elif button_type == 'fish_Protsection':
            self.add_Protfish_buttons()

        elif button_type == 'meat_Protsection':
            self.add_Protmeat_buttons()

        elif button_type == 'vegetable_Protsection':
            self.add_Protvegetable_buttons()

        elif button_type == 'grain_Protsection':
            self.add_Protgrain_buttons()

        elif button_type == 'nuts_Protsection':
            self.add_Protnuts_buttons()

        elif button_type == 'dairy_Protsection':
            self.add_Protdairy_buttons()
    def add_protein_buttons(self):
        buttons_area = self.ids.buttons_area
        buttons_area.add_widget(ImageButtonDO(text='Meat', on_press=lambda x: self.add_buttons('meat_Protsection')))
        buttons_area.add_widget(ImageButtonSea(text='Seafood', on_press=lambda x: self.add_buttons('fish_Protsection')))
        buttons_area.add_widget(ImageButtonVG(text='Vegetables', on_press=lambda x: self.add_buttons('vegetable_Protsection')))
        buttons_area.add_widget(ImageButtonGR(text='Grains', on_press=lambda x: self.add_buttons('grain_Protsection')))
        buttons_area.add_widget(ImageButtonD(text='Dairy', on_press=lambda x: self.add_buttons('dairy_Protsection')))
        buttons_area.add_widget(ImageButtonN(text='Nuts', on_press=lambda x: self.add_buttons('nuts_Protsection')))

#ADD BUTTONS ITO SA LAHAT NG FOOD GROUPS
    def add_Protmeat_buttons(self):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        buttons_area.add_widget(ImageButtonDO(text='Chicken', on_press=lambda x: self.Protmeat_section('Chicken')))
        buttons_area.add_widget(ImageButtonDO(text='Beef', on_press=lambda x: self.Protmeat_section('Beef')))
        buttons_area.add_widget(ImageButtonDO(text='Pork', on_press=lambda x: self.Protmeat_section('Pork')))
        buttons_area.add_widget(ImageButtonDO(text='Turkey', on_press=lambda x: self.Protmeat_section('Turkey')))
        buttons_area.add_widget(ImageButtonDO(text='Back', on_press=lambda x: self.add_buttons('protein')))     
    def Protmeat_section(self, meat_type):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        Protmeat_parts = {
            'Chicken': ['Breast', 'Tenderloins', 'Thigh\nw/o\nSkin', 'Drumstick\nw/o\nSkin', 'Egg'],
            'Beef': ['Top \nSirloin', 'Bottom\nSirloin', 'Top\nRound' , 'Eye\nof\nRound' , 'Flank\nSteak' , 'Skirt\nSteak' , 'Hanger\nSteak' , 'Tenderloin\nSteak' , 'Bottom\nRound', 'Sirloin\nTip\nSteak', 'Liver' ,' Heart', ' Tounge', ' Suet', ' Bone\nBroth'  ],
            'Pork': ['Loin', 'Tenderloin', 'Ham', 'Leg', 'Sirloin', 'Liver', 'Hear', 'Skin', 'Fat' ],
            'Turkey': ['Tenderloins', 'Thigh', 'Drumstick', 'Breast']
        }

        for part in Protmeat_parts.get(meat_type, []):
            buttons_area.add_widget(ImageButtonDO(text=part, on_press=lambda x, p=part: self.add_cooking_method_meat(f"{meat_type} {p}")))

        buttons_area.add_widget(ImageButtonDO(text='Back\nto\nMeat', on_press=lambda x: self.add_buttons('meat_Protsection'))) 
    def add_Protfish_buttons(self):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        fish = ['Salmon', 'Tuna', 'Shrimp']
        fish_with_cuts = {'Salmon', 'Tuna'}  # Mga isdang may cuts

        for item in fish:
            if item in fish_with_cuts:
                buttons_area.add_widget(ImageButtonSea(text=item, on_press=lambda x, i=item: self.fish_Protsection(i)))
            else:
                buttons_area.add_widget(ImageButtonSea(text=item, on_press=lambda x, i=item: self.add_cooking_method_fish(i)))

        buttons_area.add_widget(ImageButtonSea(text='Back\nto\nProtein', on_press=lambda x: self.add_buttons('protein')))
    def fish_Protsection(self, fish_type):
       
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        fish_parts = {
            'Salmon': ['Wild\nSalmon', 'Farmed\nSalmon'],
            'Tuna': ['Fresh\nTuna', 'Farmed\nTuna', 'Canned Tuna\nin oil','Canned Tuna\nin water'],
            
            
        }

        for part in fish_parts.get(fish_type, []):
            buttons_area.add_widget(ImageButtonSea(text=part, on_press=lambda x, p=part: self.add_cooking_method_fish(f"{fish_type} {p}")))

        buttons_area.add_widget(ImageButtonSea(text='Back\nto\nFish', on_press=lambda x: self.add_buttons('fish_section')))
    def add_Protvegetable_buttons(self):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        vegetables = ['Edamame', 'Tofu', 'Tempeh']
        for vegetable in vegetables:
            buttons_area.add_widget(ImageButtonVG(text=vegetable, on_press=lambda x, v=vegetable: self.add_cooking_method_veg(v)))
        
        buttons_area.add_widget(ImageButtonVG(text='Back\nto\nProtein', on_press=lambda x: self.add_buttons('protein')))
    def add_Protgrain_buttons(self):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        grains = ['Lentils', 'Chickpeas', 'Black\nBeans', 'Quinoa']
        for grain in grains:
            buttons_area.add_widget(ImageButtonGR(text=grain, on_press=lambda x, g=grain: self.add_cooking_method_grain(g)))
        
        buttons_area.add_widget(ImageButtonGR(text='Back\nto\nProtein', on_press=lambda x: self.add_buttons('protein'))) 
    def add_Protnuts_buttons(self): 
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        nuts = ['Peanuts', 'Chia\nSeeds']
        for nuts in nuts:
            buttons_area.add_widget(ImageButtonN(text=nuts, on_press=lambda x, n=nuts: self.add_cooking_method_nuts(n)))
        
        buttons_area.add_widget(ImageButtonN(text='Back\nto\nProtein', on_press=lambda x: self.add_buttons('protein')))
    def add_Protdairy_buttons(self):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        dairy = ['Greek\nYogurt', 'Cottage\nCheese','Cheddar\nCheese', 'Quickmelt\nCheese', 'Cream\nCheese', 'Edam\nCheese', 'Kesong\nPuti', 'Parmesan\nCheese', 'Mozzarella\nCheese', 'Gouda\nCheese', 'Blue\nCheese' ]
        for item in dairy:
            buttons_area.add_widget(ImageButtonD(text=item, on_press=lambda x, i=item: self.add_cooking_method_dairy(i)))
        
        buttons_area.add_widget(ImageButtonD(text='Back \nto\nProtein', on_press=lambda x: self.add_buttons('protein')))
        

#COOKING METHOD LAHAT NG KLASE NG FOOD 
    def add_cooking_method_fish(self, fish_part):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        cooking_methods = ['Stir-Fry', 'Boil', 'Steam', 'Grill']
        for method in cooking_methods:
            buttons_area.add_widget(ImageButtonSea(text=method, on_press=lambda x, m=method: self.prompt_grams(fish_part, m)))
        buttons_area.add_widget(ImageButtonSea(text='Back', on_press=lambda x: self.add_Protfish_buttons()))
    def add_cooking_method_meat(self,  Protmeat_parts):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        cooking_methods = ['Stir-Fry', 'Boil', 'Steam', 'Grill']
        for method in cooking_methods:
            buttons_area.add_widget(ImageButtonDO(text=method, on_press=lambda x, m=method: self.prompt_grams(Protmeat_parts, m)))
        buttons_area.add_widget(ImageButtonDO(text='Back', on_press=lambda x: self.Protmeat_section(Protmeat_parts.split()[0])))
    def add_cooking_method_veg(self, meat_part):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        cooking_methods = ['Stir-Fry', 'Boil', 'Steam', 'Grill']
        for method in cooking_methods:
            buttons_area.add_widget(ImageButtonVG(text=method, on_press=lambda x, m=method: self.prompt_grams(meat_part, m)))
        buttons_area.add_widget(ImageButtonVG(text='Back', on_press=lambda x: self.add_Protvegetable_buttons()))
    def add_cooking_method_nuts(self, meat_part):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()
        cooking_methods = ['Stir-Fry', 'Boil', 'Steam', 'Grill']
        for method in cooking_methods:
            buttons_area.add_widget(ImageButtonN(text=method, on_press=lambda x, m=method: self.prompt_grams(meat_part, m)))
        
        buttons_area.add_widget(ImageButtonN(text='Back', on_press=lambda x: self.add_Protnuts_buttons()))
    def add_cooking_method_grain(self, meat_part):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        cooking_methods = ['Stir-Fry', 'Boil', 'Steam', 'Grill']
        for method in cooking_methods:
            buttons_area.add_widget(ImageButtonGR(text=method, on_press=lambda x, m=method: self.prompt_grams(meat_part, m)))

        buttons_area.add_widget(ImageButtonGR(text='Back', on_press=lambda x: self.add_Protgrain_buttons()))
    def add_cooking_method_dairy(self, meat_part):
        buttons_area = self.ids.buttons_area
        buttons_area.clear_widgets()

        cooking_methods = ['Stir-Fry', 'Boil', 'Steam']
        for method in cooking_methods:
            buttons_area.add_widget(ImageButtonD(text=method, on_press=lambda x, m=method: self.prompt_grams(meat_part, m)))

        buttons_area.add_widget(ImageButtonD(text='Back', on_press=lambda x: self.add_Protdairy_buttons()))

#COMPUTATION NG NUTRIENTS
    def prompt_grams(self, food_name, cooking_method):
        popup_layout = BoxLayout(orientation='vertical')
        label = Label(text=f'Enter grams for {food_name} ({cooking_method})')
        input_field = TextInput(multiline=False)
        submit_button = Button(text='Submit', on_press=lambda x: self.calculate_nutrition(food_name, cooking_method, input_field.text))

        popup_layout.add_widget(label)
        popup_layout.add_widget(input_field)
        popup_layout.add_widget(submit_button)

        popup = Popup(title='Input Grams', content=popup_layout, size_hint=(0.6, 0.4))
        submit_button.bind(on_press=lambda x: popup.dismiss())
        popup.open()
    def calculate_nutrition(self, food_name, cooking_method, grams):
        try:
            grams = float(grams)
            if food_name in FOOD_NUTRITION:
                nutrition = FOOD_NUTRITION[food_name]

                # Apply cooking method adjustments
                if cooking_method in COOKING_METHODS_ADJUSTMENTS:
                    adjustment = COOKING_METHODS_ADJUSTMENTS[cooking_method]
                    calculated_nutrition = {
                        'protein': round(nutrition['protein'] * grams * adjustment['protein'], 2),
                        'carbs': round(nutrition['carbs'] * grams * adjustment['carbs'], 2),
                        'calories': round(nutrition['calories'] * grams * adjustment['calories'], 2),
                        'fats': round(nutrition['fats'] * grams * adjustment['fats'], 2),
                    }

                    # Add oil for stir-fry method
                    if cooking_method == 'Stir-Fry':
                        oil_nutrition = FOOD_NUTRITION['Oil']
                        calculated_nutrition['calories'] += (oil_nutrition['calories'] * 15)
                        calculated_nutrition['fats'] += (oil_nutrition['fats'] * 15)
                   
                    # Additional adjustments for Grilling
                    elif  cooking_method == 'Grill':
                        # Water loss adjustment for protein
                        water_loss_percentage = 0.09  # 9% water loss
                        calculated_nutrition['protein'] = calculated_nutrition['protein'] / (1 - water_loss_percentage)

                        # Fat loss adjustment
                        fat_loss_percentage = 0.15  # 15% fat loss
                        calculated_nutrition['fats'] = calculated_nutrition['fats'] * (1 - fat_loss_percentage)

                        # Calories adjustment due to fat loss
                        lost_fat = nutrition['fats'] * grams * fat_loss_percentage
                        calculated_nutrition['calories'] -= lost_fat * 9  # 9 kcal per gram of fat
                    
                    # Additional adjustments for boiling
                    elif cooking_method == 'Boil':
                        # Assume minimal nutrient loss for simplicity
                        # You can adjust this based on specific food or cooking conditions
                        nutrient_retention_percentage = 0.95  # 95% nutrient retention
                        calculated_nutrition['protein'] *= nutrient_retention_percentage
                        calculated_nutrition['carbs'] *= nutrient_retention_percentage
                        calculated_nutrition['fats'] *= nutrient_retention_percentage
                        calculated_nutrition['calories'] *= nutrient_retention_percentage
                    
                    # Additional adjustments for steaming
                    elif cooking_method == 'Steam':
                        # Assume minimal nutrient loss for steaming
                        nutrient_retention_percentage = 0.98  # 98% nutrient retention
                        calculated_nutrition['protein'] *= nutrient_retention_percentage
                        calculated_nutrition['carbs'] *= nutrient_retention_percentage
                        calculated_nutrition['fats'] *= nutrient_retention_percentage
                        calculated_nutrition['calories'] *= nutrient_retention_percentage

                else:
                    # If no specific adjustment, use the base values
                    calculated_nutrition = {
                        'protein': round(nutrition['protein'] * grams, 2),
                        'carbs': round(nutrition['carbs'] * grams, 2),
                        'calories': round(nutrition['calories'] * grams, 2),
                        'fats': round(nutrition['fats'] * grams, 2),
                    }

                self.ids.monitor_area.update_monitor(f"{food_name}({cooking_method})", calculated_nutrition, grams)
        except ValueError:
            pass    
    def add_grams(self, food_name):
        """Prompt the user to enter grams for the selected food."""
        # Create the label for the title
        title_label = Label(text=f"Enter Grams for {food_name}", halign='center')
        title_label.bind(size=title_label.setter('text_size'))  # Automatically adjust the text size

        # Create the input field for grams
        input_field = TextInput(hint_text="Enter grams", multiline=False)

        # Create a confirm button
        confirm_button = Button(text="Confirm", size_hint=(1, 0.3))
    
        # Create the layout to hold the title, input field, and button
        layout = BoxLayout(orientation='vertical', padding=[10, 10], spacing=10)
        layout.add_widget(title_label)
        layout.add_widget(input_field)
        layout.add_widget(confirm_button)

        # Create the popup
        input_popup = Popup(title="", content=layout, size_hint=(0.6, 0.3), auto_dismiss=False)
    
        # Bind events
        confirm_button.bind(on_release=lambda x: self.process_grams(input_popup, input_field.text, food_name))
        input_field.bind(on_text_validate=lambda x: self.process_grams(input_popup, input_field.text, food_name))

        # Open the popup
        input_popup.open()
    def process_grams(self, popup, grams_text, food_name):
        """Process the input grams and add it to the nutrient calculations."""
        try:
            grams = float(grams_text)  # Convert text input to float
            if food_name in FOOD_NUTRITION:
               nutrition_per_100g = FOOD_NUTRITION[food_name]
               nutrition = {key: nutrition_per_100g[key] * grams / 100 for key in nutrition_per_100g}
            
               # Update monitoring area with new nutrient values
               self.ids.monitor_area.update_monitor(food_name, nutrition)
            
            popup.dismiss()  # Close the popup after processing
        except ValueError:
            print("Invalid input! Please enter a valid number.")  # Handle invalid input
 
#CONNECTED TO SA MONITORING AREA
    def update_monitor(self, button_instance):
        monitor_area = self.ids.monitor_area
        monitor_area.update_monitor(button_instance.text)
class ProMealScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()
        back = ImageButton(source="Image/mealdown.png", size_hint=(None, None), size=(80, 80), pos_hint={"center_x": 0.5, "center_y": 0.03})
        back.bind(on_press=self.go_back)
        layout.add_widget(back)
        self.add_widget(layout)
    
    def on_enter(self):
        self.load_meal_data()

    breakfast_data = []  # List to store breakfast data
    lunch_data = []      # List to store lunch data
    dinner_data = []  

    def load_meal_data(self, instance=None):
        """I-load ang pagkain para sa bawat meal type"""
        conn = sqlite3.connect("pro_food_monitoring.db")
        cursor = conn.cursor()

        meal_types = ["Breakfast", "Lunch", "Dinner"]
        meal_logs = {
            "Breakfast": self.ids.breakfast_log,
            "Lunch": self.ids.lunch_log,
            "Dinner": self.ids.dinner_log
        }

        for meal_type in meal_types:
        # ✅ **GET `id` FROM DATABASE**
            cursor.execute("SELECT id, food_name, weight, protein, fats, carbs, calories FROM food_log WHERE meal_type = ?", (meal_type,))
            meals = cursor.fetchall()
            meal_logs[meal_type].clear_widgets()

            # **Adjust height dynamically**
            meal_logs[meal_type].height = max(40, len(meals) * 50)

            for meal in meals:
                # ✅ **Gamitin ang tamang index**
                meal_id = meal[0]  # First column is `id`
                food_name = meal[1]
                weight = meal[2]
                protein = meal[3] if len(meal) > 3 else 0
                fats = meal[4] if len(meal) > 4 else 0
                carbs = meal[5] if len(meal) > 5 else 0
                calories = meal[6] if len(meal) > 6 else 0

                meal_row = BoxLayout(size_hint_y=None, height=80)

                meal_label = Label(
                    text=f"[b]{food_name}[/b]  - "
                        f"{weight:.0f}g\n"
                        f"      Protein: {protein:.0f}g"
                        f"      Fats: {fats:.0f}g\n"
                        f"      Carbs: {carbs:.0f}g"
                        f"      Calories: {calories:.0f} kcal",
                    markup=True,
                    size_hint_x=2,
                    size_hint_y=None,
                    height=90,  
                    text_size=(meal_logs[meal_type].width - 90, None),
                    halign="left",
                    valign="middle"  # ✅ Para nasa gitna ng Label ang text
                )

                # ✅ **Delete Button - Dapat `meal_id` ang ipasa**
                delete_btn = ImageButtonDel(
                    size_hint_x=0.1,
                    size_hint_y=0.1
                )
                delete_btn.bind(on_press=lambda btn, meal_id=meal_id: self.delete_meal(meal_id))

                meal_row.add_widget(meal_label)
                meal_row.add_widget(delete_btn)
                meal_logs[meal_type].add_widget(meal_row)

        conn.close()



    def go_back(self, instance):
        app = App.get_running_app()
        
        # Gumamit ng SlideTransition na may duration
        
        transition = SlideTransition(duration=1,direction="up")  # 0.5 seconds
        app.root.transition = transition
        
        # Palitan ang screen
        app.root.current = "ProteinScreen" 

    def delete_meal(self, meal_id):
        """Tanggalin ang meal sa database"""
        conn = sqlite3.connect("pro_food_monitoring.db")
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM food_log WHERE id=?", (meal_id,))
        conn.commit()
        conn.close()

        # **I-reload ang meal data para mawala sa UI**
        self.load_meal_data()
#DTO MAGFUFUNCTION LAHAT NG SCREEN DAPAT NANDITO ANG MGA SCREENS
class MyApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)  # Itim na background (RGBA)
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(KetoScreen(name='KetoScreen'))
        sm.add_widget(ProteinScreen(name='ProteinScreen'))
        sm.add_widget(MealScreen(name='MealScreen'))
        sm.add_widget(ProMealScreen(name='ProMealScreen'))
        return sm

    def change_screen(self, screen_name, direction):
        sm = self.root
        sm.transition = SlideTransition(direction=direction, duration=1)
        sm.current = screen_name

    def go_to_main(self):
        self.root.transition = SlideTransition(direction='right', duration=1)
        self.root.current = 'main'

if __name__ == '__main__':
    MyApp().run()

#ALWAYS CHECK THE GOALS HERE, PADELETE NALANG PAG TAPOS NA

#TODO: 4. YUNG SPLASH SCREEN AYUSIN

#TODO: 9. YUNG SCROLLING AYUSIN NA NDI NAPIPINDOT C BUTTONS AGAD

#TODO: 13. ISAISANG CLEAR BUTTON SA MEAL BREAKDOWN


