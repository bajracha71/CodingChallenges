# Merge Meeting times
import unittest

"""
Idea:

Merging two intervals:
=====================
Let interval1 = (s1, e1) and interval2 = (s2, e2) be two intervals then 

1. interval1 and interval2 becomes one interval if and only if 
    
    Case 1
    s1------------e1    mergedInterval = (s1, e1) 
        s2----e2        
     
    if s1 <= s2 and e2 <= e1 
        
    Case 2
    s1------------e1         mergedInterval = (s1, e2)
            s2-----------e2
            
    s1------------e1
                  s2----------e2
                  
    if s1 <= s2 and e1 < e2
    
    
    
2. interval1 and interval2 wont merge if and only if

    s1------------e1
                        s2------------e2
    if s2 > e1
                        

"""
import unittest

def mergeTwoIntervals(interval1, interval2):
    s1, e1 = interval1
    s2, e2 = interval2

    if s2 > e1:
        return [interval1, interval2]
    else:
        if e2 < e1:
            return [interval1]
        else:
            return[(s1, e2)]


def merge_ranges(meetings):

    # Merge meeting ranges

    meetings.sort(key = lambda x: x[0])

    res = list()
    res.append(meetings[0])
    for m in meetings[1:]:
        last = res.pop()
        merge2 = mergeTwoIntervals(last, m)
        res.extend(merge2)


    return res

# Tests
class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)