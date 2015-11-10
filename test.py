# -*- encoding: utf-8 -*-

import unittest

import sniffer

class TestSniffer(unittest.TestCase):

    def test_sniff(self):
        u = 'http://blog.sibo.me/'
        feed = sniffer.sniff(u)
        self.assertTrue(feed <> None, 'should have feeds')

    def test_sniff_blog_sibo_me(self):
        feed = sniffer.sniff('http://blog.sibo.me')
        self.assertEqual(feed, 'http://blog.sibo.me/feed.xml')

    def test_should_not_find_feed(self):
        self.assertFalse(sniffer.sniff('http://www.example.com'), 'should not find feed')

if __name__ == '__main__':
    unittest.main()
