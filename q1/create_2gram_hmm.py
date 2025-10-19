import sys
STATE_DICT = {}
POS_DICT = {}

def get_total(transition_dict):
    total = 0
    for k, v in transition_dict.items():
        count = v['count']
        total += count
    return total

def print_transitions(output_file):
    with open(output_file, "a") as file:
        print("\\ transition", file=file)
        for key, value in STATE_DICT.items():
            w_1 = key
            transitions = value
            for k, v in transitions.items():
                w_2 = k 
                prob = v['prob']
                print(f"{w_1}  {w_2}   {prob}", file=file)

def print_emissions():
    print(POS_DICT)
    for k, v in POS_DICT.items():
        POS = k
        emissions = v
        total_count = sum(emissions.values())
        for key, value in emissions.items():
            prob = int(value) / int(total_count)
            print(f"{POS}   {key}   {prob}")

def get_transitions():
    for key, value in STATE_DICT.items():
        transitions = STATE_DICT[key]
        total_sum = get_total(transitions)

        for k, v in transitions.items():
            prob = v['count'] / total_sum
            STATE_DICT[key][k]['prob'] = prob

def create_POS_dict(token):
    word = token[0]
    pos_tag = token[1]
    if pos_tag in POS_DICT:
        if  word in POS_DICT[pos_tag]:
            POS_DICT[pos_tag][word] +=1 
        else:
            POS_DICT[pos_tag][word] = 1
    else:
        POS_DICT[pos_tag] = {word: 1}

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
        create_POS_dict(token_1)
    
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
    output_file = sys.argv[1]
    lines = sys.stdin.readlines()
    for line in lines:
        EOS_line = line.rstrip() + '</s>'
        create_state_dict(EOS_line)

    return output_file

def main():
    output_file=read_input()
    get_transitions()
    print_emissions()
    # print_transitions(output_file)

main()