import arcade




def pineTree(x, y):
    arcade.draw_triangle_filled(x + 40, y, x, y -100, x + 80, y - 100, arcade.color.GREEN)
    arcade.draw_lrtb_rectangle_filled(x + 30, x + 50, y - 100, y - 140,
                                      arcade.color.DARK_BROWN)


