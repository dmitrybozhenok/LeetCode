from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        pos = 0
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                pos = append_compressed_block(chars, count, pos)
                chars[pos] = chars[i]
                count = 1
        pos = append_compressed_block(chars, count, pos)
        return pos


def append_compressed_block(chars, count, pos):
    if count > 1:
        cstr = str(count)
        for cs in cstr:
            pos += 1
            chars[pos] = cs
        pos += 1
    else:
        pos += 1
    return pos