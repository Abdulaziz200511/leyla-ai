[app]
title = Leila AI
package.name = leilaai
package.domain = org.leila

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt

version = 1.0
requirements = python3,kivy

orientation = portrait

[buildozer]
log_level = 2

[app]
android.permissions = INTERNET
android.api = 30
android.minapi = 21

presplash.filename = %(source.dir)s/presplash.png
icon.filename = %(source.dir)s/icon.png
