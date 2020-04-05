from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class FlaskTests(TestCase):
    @classmethod
    def setUpClass(cls):
        print("INSIDE SET UP CLASS")

    @classmethod
    def tearDownClass(cls):
        print("INSIDE TEAR DOWN CLASS")
    # TODO -- write tests for every view function / feature!

    def test_table(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<table class="game-table">', html)

    def test_board(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['board'] = [["C", "A", "T", "T", "T"],
                                 ["C", "A", "T", "T", "T"],
                                 ["C", "A", "T", "T", "T"],
                                 ["C", "A", "T", "T", "T"],
                                 ["C", "A", "T", "T", "T"]]
        
        self.assertEqual(sess['board'], [["C", "A", "T", "T", "T"],
                                         ["C", "A", "T", "T", "T"],
                                         ["C", "A", "T", "T", "T"],
                                         ["C", "A", "T", "T", "T"],
                                         ["C", "A", "T", "T", "T"]])

        rlt = Boggle().check_valid_word(sess['board'], 'cat')
        self.assertEqual(rlt, 'ok')

        wrong = Boggle().check_valid_word(sess['board'], 'cats')
        self.assertEqual(wrong, 'not-on-board')

        non_word = Boggle().check_valid_word(sess['board'], 'ctts')
        self.assertEqual(non_word, 'not-word')
 