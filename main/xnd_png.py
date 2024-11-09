
#生成 icon
src = "main/app_icon7.png"
dst = "main/app_icon.gen7.h"

with open(src, "rb") as f:
    buf = f.read()

with open(dst, "w", encoding="utf-8", newline="\n") as g:
    g.write("/* THIS FILE IS GENERATED DO NOT EDIT */\n")
    g.write("#ifndef APP_ICON_H\n")
    g.write("#define APP_ICON_H\n")
    g.write("static const unsigned char app_icon_png[] = {\n")
    for i in range(len(buf)):
        g.write(str(buf[i]) + ",\n")
    g.write("};\n")
    g.write("#endif")


#生成 splash 图片
src = "main/splash7.png"
dst = "main/splash.gen7.h"
print("test png 1")
with open(src, "rb") as f:
    buf = f.read()

with open(dst, "w", encoding="utf-8", newline="\n") as g:
    g.write("/* THIS FILE IS GENERATED DO NOT EDIT */\n")
    g.write("#ifndef BOOT_SPLASH_H\n")
    g.write("#define BOOT_SPLASH_H\n")
    # Use a neutral gray color to better fit various kinds of projects.
    g.write("static const Color boot_splash_bg_color = Color(0.0, 0.0, 0.0);\n")
    g.write("static const unsigned char boot_splash_png[] = {\n")
    for i in range(len(buf)):
        g.write(str(buf[i]) + ",\n")
    g.write("};\n")
    g.write("#endif")