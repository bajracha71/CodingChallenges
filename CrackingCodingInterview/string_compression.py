# 1.5. Implement a method to perform basic string compression
# using the counts of repeated characters. For example, the
# string aabcccccaaa would become a2b1c5a3. If the "compressed"
# string would not become smaller than the original string,
# your method should return the original string.


def string_compression(input_string):
    comp_string = list()
    count = 1
    prev = input_string[0]

    for c in input_string[1:]:

        if prev == c:
            count += 1
        else:
            # compress
            comp_string.append(prev)
            comp_string.append(str(count))
            prev = c
            # reset count
            count = 1

    comp_string.append(prev)
    comp_string.append(str(count))

    if len(input_string) == len(comp_string):
        return input_string
    else:
        return "".join(comp_string)


if __name__ == "__main__":

    str1 = "aabccccaaa"
    print(string_compression(str1))

    str2 = "aabb"
    print(string_compression(str2))
