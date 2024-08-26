import keyboard

# Function to block Alt+Tab
def block_alt_tab(e):
    if e.event_type == keyboard.KEY_DOWN and e.name == 'alt':
        keyboard.block_key('tab')

# Function to block Ctrl+Tab
def block_ctrl_tab(e):
    if e.event_type == keyboard.KEY_DOWN and e.name == 'ctrl' and keyboard.is_pressed('tab'):
        keyboard.block_key('tab')

# Function to block Ctrl+Shift+Esc
def block_ctrl_shift_esc(e):
    if e.event_type == keyboard.KEY_DOWN and e.name == 'ctrl' and e.event_type == keyboard.KEY_DOWN and keyboard.is_pressed('shift'):
        keyboard.block_key('esc')

# Listen for keyboard events and block specified shortcuts
keyboard.hook(block_alt_tab)
keyboard.hook(block_ctrl_tab)
keyboard.hook(block_ctrl_shift_esc)

# Keep the application running
keyboard.wait()
