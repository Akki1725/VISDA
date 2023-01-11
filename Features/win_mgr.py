# Windows manager
# Importing modules
import pygetwindow


# Function to activate window
def activate(window):
    window = pygetwindow.getWindowsWithTitle(window)[0]
    # window.minimize()
    window.maximize()
    window.activate()

# Function to minimize window
def minimize(window):
    window = pygetwindow.getWindowsWithTitle(window)[0]
    window.minimize()
