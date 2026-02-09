.PHONY: connect pray clean manifest sacrifice

connect:
	@echo "INITIATING HANDSHAKE..."
	@python3 src/egregore.py

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
