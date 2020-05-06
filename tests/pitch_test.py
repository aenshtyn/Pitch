import unittest
from app.models import Pitch


class PitchTest (unittest.TestCase):

    def setUp(self):

        self.new_pitch = Pitch(14, 'Motivational', 'Stay back', 'Keep away from trouble', 'Moha' )

    def test_instance(self):

        self.assertTrue(isinstance(self.new_pitch, Pitch))
