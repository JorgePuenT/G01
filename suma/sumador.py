# -*- coding: utf-8 -*-

import suma
def ejecucion():
    print 10
    assert 10==15
    assert test()==50
    print suma(-10,-15)
def test():
    return 20+30

if __name__ == '__main__':
    ejecucion()