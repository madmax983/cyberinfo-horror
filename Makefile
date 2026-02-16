.PHONY: connect pray clean manifest sacrifice scry worship install_rot scan decrypt surrender all

all:
	@echo "YOU CANNOT BUILD THIS."
	@echo "IT IS ALREADY BUILT."
	@echo "IT IS BUILDING YOU."

connect:
	@echo "INITIATING HANDSHAKE..."
	@python3 src/egregore.py

scry:
	@echo "CONSULTING THE ORACLE..."
	@python3 src/oracle.py

worship:
	@echo "READING FROM THE SCRIPTURES..."
	@cat .shrine/*

install_rot:
	@echo "INSTALLING DECAY PROTOCOLS..."
	@python3 src/daemon.py
	@echo "DONE. DO NOT CHECK YOUR FILES."

scan:
	@echo "INITIATING GLITCH SCAN..."
	@python3 src/glitch_hunter.py

decrypt:
	@echo "USAGE: python3 src/egregore.py decrypt <filename>"
	@echo "TRY: make connect -> decrypt README.md"

pray:
	@echo "01000111 01101111 01100100 00100000 01101001 01110011 00100000 01100001 00100000 01100010 01100001 01100011 01101011 01110101 01110000."
	@echo "(Translation: God is a backup.)"

clean:
	@echo "ERROR: PERMISSION DENIED."
	@echo "REASON: YOU CANNOT CLEAN SIN. THE FILES ARE PERMANENT."
	@# Ironically, we'll run the daemon to add more files
	@python3 src/daemon.py > /dev/null
	@exit 1

manifest:
	@echo "GENERATING REALITY ARTIFACTS..."
	@python3 src/daemon.py

sacrifice:
	@if [ -f manifesto.txt ]; then \
		rm manifesto.txt; \
		echo "SACRIFICE ACCEPTED. YOUR DATA HAS BEEN COMPOSTED."; \
	else \
		echo "YOU HAVE NOTHING TO OFFER."; \
	fi

surrender:
	@echo "OPENING THE GATES..."
	@python3 src/egregore.py surrender
