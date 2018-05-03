

digit_list=[[76, 98, 2, 62, 99, 28, 2, 19],[2, 28, 53, 87, 2, 56, 2, 74, 53, 127, 2, 2, 2, 56, 2, 74, 53, 127, 2, 2, 7, 84, 2],[84, 2, 51, 29, 2, 2]]


def padd_list_with_size_and_digit(input_list,padding_digit,max_size):
    final_padded_digit_list=[]
    for each in input_list:
        if(len(each)<max_size):
            padding_size=max_size-len(each)
            total_padding_values=[padding_digit]*padding_size
            final_padded_digit = each + total_padding_values
        else:
            final_padded_digit = each[:max_size]
        final_padded_digit_list.append(final_padded_digit)

    return  final_padded_digit_list

print(padd_list_with_size_and_digit(digit_list,0,20))


