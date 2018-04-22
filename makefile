default: example

test:
	green3 . -vvv

run:
	python3 bot/bot.py

install:
	pip3 install -r requirements.txt

style:
	pycodestyle bot/ tests/

example:
	python3 bot/simple_echo_bot.py
