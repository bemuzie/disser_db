# -*- coding: utf-8 -*-
def example(decorated_fun):
    def fun(*args, **kwargs):
        print len(args)

        if len(args) == 1:
            print u"это пост запрос до выполнения "

        # print kwargs
        df = decorated_fun(*args, **kwargs)
        if len(args) == 1:
            print u"а это после"
        return df

    return fun
