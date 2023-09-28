import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result1 = emotion_detector('I am glad this happened')
        self.assertEqual(result1['dominant_dictionary'], 'joy')  # Check the correct key
        result2 = emotion_detector('I am really mad about this')
        self.assertEqual(result2['dominant_dictionary'], 'anger')  # Check the correct key
        result3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result3['dominant_dictionary'], 'disgust')  # Check the correct key
        result4 = emotion_detector('I am so sad about this')
        self.assertEqual(result4['dominant_dictionary'], 'sadness')  # Check the correct key
        result5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result5['dominant_dictionary'], 'fear')  # Check the correct key

unittest.main()
