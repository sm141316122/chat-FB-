import os


input_file = "input.txt"

#讀取檔案
def read_file(input_file):
	with open(input_file, "r", encoding="utf-8-sig") as f:
		lines = []
		for line in f:
			lines.append(line.strip())
	return lines

#轉換對話格式
def chat_format(lines):
	new = []
	person = None
	for line in lines:
		if line == "Allen":
			person = "Allen"
			continue
		if line == "Tom":
			person = "Tom"
			continue
		if person:
			new_line = person + ":" + " " + line
			new.append(new_line)
	return new

#輸出檔案
def output_file(output, new):
	with open("output.txt", "w", encoding="utf-8-sig") as f:
		for line in new:
			f.write(line + "\n")

#主程式
def main(input_file):
	lines = read_file(input_file)
	new = chat_format(lines)
	output_file("output.txt", new)

if os.path.isfile(input_file):
	main(input_file)
else:
	print("找不到檔案")