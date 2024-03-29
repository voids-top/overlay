def settings(canvas, config, transparency_position, fps_position, refresh_position):
    canvas.create_text(250, 45, text="Settings", anchor="center", font=("Minecraftia", 15), fill="#FFFFFF", tag="rewrite")
    canvas.create_line(100, 115, 400, 115, fill="#FFFFFF", width=5, tag="rewrite")
    canvas.create_text(250, 95, text="Transparency : {}%".format(int(config["transparency"])), anchor="center",font=("Minecraftia", 10), fill="#FFFFFF", tag="rewrite")
    canvas.create_oval(95 + transparency_position, 110, 105 + transparency_position, 120, fill="#FFFFFF", tag="rewrite")
    canvas.create_line(100, 160, 400, 160, fill="#FFFFFF", width=5, tag="rewrite")
    canvas.create_text(250, 140, text="FPS : {}".format(int(config["fps"])), anchor="center",font=("Minecraftia", 10), fill="#FFFFFF", tag="rewrite")
    canvas.create_oval(95 + fps_position, 155, 105 + fps_position, 165, fill="#FFFFFF", tag="rewrite")
    canvas.create_line(100, 205, 400, 205, fill="#FFFFFF", width=5, tag="rewrite")
    canvas.create_text(250, 180, text="Refresh Log : {}ms".format(int(config["refresh"])), anchor="center",font=("Minecraftia", 10), fill="#FFFFFF", tag="rewrite")
    canvas.create_oval(95 + refresh_position, 200, 105 + refresh_position, 210, fill="#FFFFFF", tag="rewrite")
    canvas.create_line(155, 220, 345, 220, fill="#FFFFFF", width=2, tag="rewrite")  # 上
    canvas.create_line(155, 240, 345, 240, fill="#FFFFFF", width=2, tag="rewrite")  # 下
    canvas.create_line(155, 220, 155, 240, fill="#FFFFFF", width=2, tag="rewrite")  # 左
    canvas.create_line(345, 220, 345, 240, fill="#FFFFFF", width=2, tag="rewrite")  # 右
    canvas.create_text(250, 229, text="Open Custom Logfile", anchor="center", font=("Minecraftia", 10),fill="#FFFFFF", tag="rewrite")
    canvas.create_text(250, 260, text="Reset API Key", anchor="center", font=("Minecraftia", 10), fill="#FFFFFF", tag="rewrite")
    canvas.create_line(125, 275, 225, 275, fill="#FFFFFF", width=2, tag="rewrite")
    canvas.create_line(125, 295, 225, 295, fill="#FFFFFF", width=2, tag="rewrite")
    canvas.create_line(125, 275, 125, 295, fill="#FFFFFF", width=2, tag="rewrite")
    canvas.create_line(225, 275, 225, 295, fill="#FFFFFF", width=2, tag="rewrite")
    canvas.create_text(175, 284, text="Hypixel", anchor="center", font=("Minecraftia", 10), fill="#FFFFFF", tag="rewrite")
    canvas.create_line(275, 275, 375, 275, fill="#FFFFFF", width=2, tag="rewrite")
    canvas.create_line(275, 295, 375, 295, fill="#FFFFFF", width=2, tag="rewrite")
    canvas.create_line(275, 275, 275, 295, fill="#FFFFFF", width=2, tag="rewrite")
    canvas.create_line(375, 275, 375, 295, fill="#FFFFFF", width=2, tag="rewrite")
    canvas.create_text(325, 284, text="Antisniper", anchor="center", font=("Minecraftia", 10), fill="#FFFFFF", tag="rewrite")

def about(canvas):
    canvas.create_text(250, 45, text="About", anchor="center", font=("Minecraftia", 15), fill="#FFFFFF", tag="rewrite")
    canvas.create_text(250, 80, text="Creator / Developer", anchor="center", font=("Minecraftia", 10),fill="#FFFFFF", tag="rewrite")
    canvas.create_text(250, 100, text="VoidPro (@bw_VoidPro)", anchor="center", font=("Minecraftia", 11),fill="#FFFFFF", tag="rewrite")
    canvas.create_text(250, 130, text="Tester / Ideas", anchor="center", font=("Minecraftia", 10), fill="#FFFFFF", tag="rewrite")
    canvas.create_text(250, 150, text="Shimamal (@MaybeShim)", anchor="center", font=("Minecraftia", 10),fill="#FFFFFF", tag="rewrite")
    canvas.create_text(250, 180, text="Special Thanks", anchor="center", font=("Minecraftia", 10), fill="#FFFFFF", tag="rewrite")
    canvas.create_text(250, 200, text="Antisniper (antisniper.net)", anchor="center", font=("Minecraftia", 9),fill="#FFFFFF", tag="rewrite")
    canvas.create_text(250, 215, text="Minecraftia", anchor="center", font=("Minecraftia", 9), fill="#FFFFFF", tag="rewrite")
    canvas.create_text(250, 250, text="Runtime : Python3.8, pyarmor", anchor="center", font=("Minecraftia", 8),fill="#FFFFFF", tag="rewrite")
    canvas.create_text(250, 270, text="Source : Private", anchor="center", font=("Minecraftia", 8), fill="#FFFFFF", tag="rewrite")
    canvas.create_text(250, 290, text="Support : https://discord.gg/r42t2kb3pC", anchor="center",font=("Minecraftia", 9), fill="#FFFFFF", tag="rewrite")