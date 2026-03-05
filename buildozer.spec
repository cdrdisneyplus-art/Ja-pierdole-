[app]

title = PaskiFuture
package.name = paskifuture
package.domain = org.private

source.dir = .
source.include_exts = py

version = 1.1

requirements = python3,kivy,openpyxl,xlrd,plyer

orientation = portrait
fullscreen = 0

log_level = 2


android.api = 34
android.minapi = 24
android.ndk = 25b

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.archs = arm64-v8a,armeabi-v7a


[buildozer]

log_level = 2
warn_on_root = 1
