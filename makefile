default: test

test:
	green3 . -vvv

run:
	python3 bot.py

install:
	pip3 install -r requirements.txt