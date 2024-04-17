#!/usr/bin/pyhon3

from typing import Union

def unlockScribd(url: str) -> Union[str, None]:
	params: list = url.split('/')
	try:
		if params[4].isdigit():
			return "\x68\x74\x74\x70\x73\x3a\x2f\x2f\x65\x73\x2e\x73\x63\x72\x69\x62\x64\x2e\x63\x6f\x6d\x2f\x65\x6d\x62\x65\x64\x73\x2f"+params[4]+"\x2f\x63\x6f\x6e\x74\x65\x6e\x74\x3f\x73\x74\x61\x72\x74\x5f\x70\x61\x67\x65\x3d\x31"
		else:
			return None
	except:
		return None

url: str = input("URL: ")
print("URL Unlock: "+unlockScribd(url))