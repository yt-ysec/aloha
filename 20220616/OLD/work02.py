# 画像フォルダの中をしらべて、ファイル名をぜんぶ表示する
import os

path = './mnist_mini_1000/'
files = os.listdir(path)

print(files)
