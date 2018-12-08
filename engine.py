import libtcodpy as libtcod

from input_handlers import handle_keys

def main():
    screen_width = 80
    screen_height = 50

    # Keep track of the player, Cast the division (float) to int
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    # http://roguecentral.org/doryen/data/libtcod/doc/1.5.1/html2/console_set_custom_font.html?c=false&cpp=false&cs=false&py=true&lua=false
    libtcod.console_set_custom_font("arial10x10.png", libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    # Creates the window, title, and fullscreen
    libtcod.console_init_root(screen_width, screen_height, "B@rd", False)

    # Draw a new console
    con = libtcod.console_new(screen_width, screen_height)

    # Holds keyboard and mouse input
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    # Game loop (until screen is closed)
    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        # 0 (default now "con") is the console you are printing to, Character color
        libtcod.console_set_default_foreground(con, libtcod.fuchsia)
        # 0 is the console you are printing to, x, y, Char, No background
        libtcod.console_put_char(con, player_x, player_y, "@", libtcod.BKGND_NONE)
        # ???
        libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)

        # Apply the updates to the screen
        libtcod.console_flush()

        libtcod.console_put_char(con, player_x, player_y, " ", libtcod.BKGND_NONE)

        action = handle_keys(key)

        # None or the returnt value
        move = action.get("move")
        exit = action.get("exit")
        fullscreen = action.get("fullscreen")

        if move:
            dx, dy = move
            player_x += dx
            player_y += dy

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

#Main only runs when you execute "engine.py" but not when someone imports this module????
if __name__ == '__main__':
    main()
