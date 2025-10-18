import sys

STATE_DICT = {}

def create_token_map(line):
    split_line = line.split(" ")

    for i, token in enumerate(split_line):
        if i > 0:
            bigram_first = split_line[i-1].split("/")
            if i == len(split_line ) - 1:
                bigram_no_EOS = split_line[i].split("</s>")
                bigram_first = bigram_no_EOS[0].split('/')[0]
                bigram_second = '</s>'
                bigram_pos = f"{bigram_first} {bigram_second}"
            else:
                bigram_second = split_line[i].split("/")
                bigram_pos = f"{bigram_first[1]} {bigram_second[1]}"
            if bigram_pos in STATE_DICT:
                STATE_DICT[bigram_pos] +=1
            else: 
                STATE_DICT[bigram_pos] = 1

def read_input():
    lines = sys.stdin.readlines()
    for line in lines:
        EOS_line = line.rstrip() + '</s>'
        create_token_map(EOS_line)

def main():
    read_input()

    print(f"STATE {STATE_DICT}")

main()