import re


def run(eingabe):
	with open(eingabe, "r", encoding="utf-8") as f:
		text = f.read()

	# Alle UTCs im Text finden
	utc_list = re.findall(r"-\d+", text)

	# Vorkommen zaehlen
	counts = {utc: text.count(utc) for utc in utc_list}

	for utc, count in counts.items():
		text = text.replace(utc, f"{count}")

	# Concatenate counts into string like "433"
	name_exe = "".join(str(counts[utc]) for utc in utc_list)
	return name_exe


