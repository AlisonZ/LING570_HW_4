import sys
STATE_DICT = {}

def get_transitions(bigram_state_dict):
    current_w1 =''
    state_nums = 0
    for key, value in bigram_state_dict.items():
        split_token = key.split(" ")
        token_w1 = split_token[0]
        if token_w1 == current_w1:
            print(f"SAME {token_w1}")
        else:
            print(f"new w1 {token_w1}")
            state_nums +=1
            current_w1 = token_w1

    return state_nums

def create_state_dict(line):
    split_line = line.split(" ")

    for i, token in enumerate(split_line):
        if i < len(split_line)-2:
            token_1 = token.split("/")
            token_2 = split_line[i+1].split("/")
        else:
            token_no_EOS = token.split("</s>")
            token_1 = token_no_EOS[0].split("/")
            token_2 = ['', "</s>"]
    
        POS_1 = token_1[1]
        POS_2 = token_2[1]

        if POS_1 in STATE_DICT:
            if POS_2 in STATE_DICT[POS_1]:
                STATE_DICT[POS_1][POS_2] +=1
            else:
                STATE_DICT[POS_1].update({POS_2: 1})
        else:
            new_entry = {POS_1: {POS_2: 1}}
            STATE_DICT.update(new_entry)

def read_input():
    lines = sys.stdin.readlines()
    for line in lines:
        EOS_line = line.rstrip() + '</s>'
        create_state_dict(EOS_line)

def main():
    read_input()
    # state_nums = get_transitions(bigram_token_dict)

    print(f"BIGGGG {STATE_DICT}")


main()