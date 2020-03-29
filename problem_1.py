# Problem 1

import unittest

class ProblemOne(unittest.TestCase):
    #assumes all url's are given as strings and that at least protocols and domains are present
    #and Protocols have :// at the end of them
    def setUp(self):
        self.urler = url_parser()

    def test_url_parser(self):
        comp = self.urler.splitter("ftp://bu.edu/")
        fin = ["Protocol: ftp", "Domain: bu.edu", "Path: "]
        self.assertEqual(fin, comp)
        
    def test_url_2(self):
        comp = self.urler.splitter("https://www.google.com/some-path")
        fin = ["Protocol: https", "Domain: www.google.com", "Path: some-path"]
        self.assertEqual(fin, comp)

    def test_url_3(self):
        comp = self.urler.splitter("")
        fin = ['']
        self.assertEqual(fin, comp)

    def test_url_4(self):
        comp = self.urler.splitter("//")
        fin = ['', '', '']
        self.assertEqual(fin, comp)
        
    def test_url_5(self):
        comp = self.urler.splitter("https://www.tablo.com/path1/path2/path3")
        fin = ["Protocol: https", "Domain: www.tablo.com", "Path: path1/path2/path3"]
        self.assertEqual(fin, comp)

    def test_url_6(self):
        comp = self.urler.splitter("kkc://bu.edu")
        fin = ["Protocol: kkc", "Domain: bu.edu", "Path: "]
        self.assertEqual(fin, comp)

class url_parser(object):
    def splitter(self,url):
        x = url.split("/")
        if x[0] == '':
            return x
        else:
            final = []
            proto = x[0][:-1]
            domain = x[2]
            path = ""
            for i in range(3,len(x)):
                path += x[i]
                if(len(x) > 4):
                    #if the path is longer, it will be have a / at the end
                    path += "/"
            if len(path) > 0 and path[-1] == '/':
                path = path[:-1]
            final.append("Protocol: " + proto)
            final.append("Domain: " + domain)
            final.append("Path: " + path)
            return final

if __name__ == '__main__':
    unittest.main()
