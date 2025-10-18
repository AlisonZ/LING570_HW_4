import sys
STATE_DICT = {}

def get_total(transition_dict):
    total = 0
    for k, v in transition_dict.items():
        count = v['count']
        total += count
    return total
    

def get_transitions():
    for key, value in STATE_DICT.items():
        transitions = STATE_DICT[key]
        total_sum = get_total(transitions)
        # print(f"KEY:::{key}")

        for k, v in transitions.items():
            prob = v['count'] / total_sum
            STATE_DICT[key][k]['prob'] = prob
            # print(f"XXX {}")


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
                STATE_DICT[POS_1][POS_2]['count'] +=1
            else:
                STATE_DICT[POS_1].update({POS_2: {'count':1, 'prob': 'null'}})
        else:
            new_entry = {POS_1: {POS_2: {'count':1, 'prob': 'null'}}}
            STATE_DICT.update(new_entry)

def read_input():
    lines = sys.stdin.readlines()
    for line in lines:
        EOS_line = line.rstrip() + '</s>'
        create_state_dict(EOS_line)

def main():
    read_input()
    get_transitions()

    print(f"BIGGGG {STATE_DICT}")


main()