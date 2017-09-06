import sys
script,input_encoding,error=sys.argv


def main(language_file,encoding,error):
    line = language_file.readline()

    if len(line)>0:
        print_line(line,encoding,error)
        return main(language_file,encoding,error)


def print_line(line,encoding,error):
    next_lang=line.strip()
    raw_byte = next_lang.encode(encoding,error)
    cooked_string = raw_byte.decode(encoding,error)

    print(raw_byte," <=====> ",cooked_string)


language = open("languages.txt",encoding="utf-8")
main(language,input_encoding,error)
