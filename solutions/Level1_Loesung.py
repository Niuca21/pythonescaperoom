def run(eingabe):
	result = ""
	tmp = eingabe.split()
	for i in tmp:
		result += "".join(chr(int(i)))
	return result # tmp


## Loesung ist: 67 111 111 107 105 101 109 111 110 115 116 101 114.
