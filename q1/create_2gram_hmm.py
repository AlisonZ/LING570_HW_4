import sys

def create_token_map(line):
    split_line = line.split(" ")
    state_dict = {}

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
            if bigram_pos in state_dict:
                state_dict[bigram_pos] +=1
            else: 
                state_dict[bigram_pos] = 1
    sorted_dict = sorted(state_dict.items(), key=lambda item:item[0])
    return sorted_dict

def read_input():
    lines = sys.stdin.readlines()
    for line in lines:
        EOS_line = line.rstrip() + '</s>'
        bigram_token_map = create_token_map(EOS_line)
    return bigram_token_map

def main():
    bigram_token_map = read_input()
    print(f"BIGGGG", bigram_token_map)


main()