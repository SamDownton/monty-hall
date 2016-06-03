'''
Created on 2 Jun 2016

@author: samuel.downton
'''
import unittest
import play

class TestMethods(unittest.TestCase):
    def test_goat_revealer(self):
        self.assertEqual(play.reveal_a_goat([0,0,1],0), 1, "Check the correct door is revealed")
        self.assertEqual(play.reveal_a_goat([0,1,0],0), 2, "Check the correct door is revealed")
        self.assertNotEqual(play.reveal_a_goat([1,0,0],0), 0 , "Check the correct door is revealed")
        self.assertNotEqual(play.reveal_a_goat([0,0,1],2), 2 , "Check the correct door is revealed")
        self.assertNotEqual(play.reveal_a_goat([0,1,0],0), 1 , "Check the correct door is revealed")
    
    def test_play_method(self):
        self.assertEqual(play.play([0,0,1], 0), 1, "Check play method returns a win")
        self.assertEqual(play.play([0,0,1], 2), 0, "Check play method returns a win")
        self.assertEqual(play.play([0,0,1], 1), 1, "Check play method returns a win")
        self.assertEqual(play.play([1,0,0], 2), 1, "Check play method returns a win")
    
if __name__ == '__main__':
    unittest.main()