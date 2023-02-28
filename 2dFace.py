import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
#konstantet per madhesine e ekranit

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "shembull")
#hap windown dhe vendos permasat njekohesisht

arcade.set_background_color(arcade.color.WHITE)
#vensosim ngjyren e background. mund te vendosen dhe ne formatin (red, green, blue)

arcade.start_render()
#starton procesin e render. duhet gjithmon para se te fillosh te vizatosh

x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x,y,radius,arcade.color.YELLOW)
#vizaton fytyren

x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)
#vizaton syrin e djathte)

x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)
#vizaton syrin e majte

x = 300
y= 270
width = 100
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)
#vizaton buzeqeshjen

arcade.finish_render()
#perfundon procesin e vizatimit

arcade.run()
#mban dritaren hapur deri sa ta mbyllim vete


#kjo eshte forma pa perdorur funksione
