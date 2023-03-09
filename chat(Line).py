import os


input_file = "LINE-Viki.txt"

#讀取檔案
def read_file(input_file):
	with open(input_file, "r", encoding="utf-8-sig") as f:
		lines = []
		for line in f:
			lines.append(line.strip())
	return lines


#轉換對話格式
def chat_format(lines):
	allen_word = 0
	allen_sticker = 0
	allen_image = 0
	viki_word = 0
	viki_sticker = 0
	viki_image = 0
	person = None
	for line in lines:
		l = line.split(" ")
		person = l[1]
		if person == "Allen":
			if l[2] == "貼圖":
				allen_sticker += 1
			elif l[2] == "圖片":
				allen_image += 1
			else:
				for w in l[2:]:
					allen_word += len(w)
		elif person == "Viki":
			if l[2] == "貼圖":
				viki_sticker += 1
			elif l[2] == "圖片":
				viki_image += 1
			else:
				for w in l[2:]:
					viki_word += len(w)
	print("Allen 傳了", allen_word, "個字,", 
		allen_sticker, "個貼圖,", allen_image, "張圖片")
	print("Viki 傳了", viki_word, "個字,", 
		viki_sticker, "個貼圖,", viki_image, "張圖片")


#主程式
def main(input_file):
	lines = read_file(input_file)
	new = chat_format(lines)


if os.path.isfile(input_file):
	main(input_file)
else:
	print("找不到檔案")