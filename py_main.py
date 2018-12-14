# coding=utf-8

import json
from collections import Iterable


def is_all_int(x):
    for v in x:
        if isinstance(v, float):
            return False
    return True


#basestring是str和unicode的超类
#isinstance(obj, basestring)等价于isinstance(obj, (str, unicode))
def print_dict(kname, d):
    bo_has_dict = False
    if not isinstance(d, dict):
        return
    for k1, v1 in d.iteritems():
        if isinstance(v1, dict):
            bo_has_dict = True
            print_dict('%s_%s' % (kname, k1), v1)
        elif isinstance(v1, list):
            if len(v1) > 0:
                if isinstance(v1[0], dict):
                    print_dict('%s_%s' % (kname, k1), v1[0])
    if bo_has_dict:
        print "type st_" + kname + " struct{"
        for k, v in d.iteritems():
            if isinstance(v, bool):
                print "\t" + k.capitalize() + " bool\t" + '`json:"%s"`' % k
            elif isinstance(v, int):
                print "\t" + k.capitalize() + " int\t" + '`json:"%s"`' % k
            elif isinstance(v, float):
                print "\t" + k.capitalize() + " float32\t" + '`json:"%s"`' % k
            elif isinstance(v, basestring):
                print "\t" + k.capitalize() + " string\t" + '`json:"%s"`' % k
            elif isinstance(v, list):
                if len(v) > 0:
                    if isinstance(v[0], dict):
                        print "\t" + k.capitalize() + " []*st_%s_%s\t" % (
                            kname, k) + '`json:"%s"`' % k
                    if isinstance(v[0], int):
                        if is_all_int(v):
                            print "\t" + k.capitalize(
                            ) + " []int\t" + '`json:"%s"`' % k
                        else:
                            print "\t" + k.capitalize(
                            ) + " []float32\t" + '`json:"%s"`' % k
                    elif isinstance(v[0], float):
                        print "\t" + k.capitalize(
                        ) + " []float32\t" + '`json:"%s"`' % k
                    elif isinstance(v[0], basestring):
                        print "\t" + k.capitalize(
                        ) + " []string\t" + '`json:"%s"`' % k
            elif isinstance(v, dict):
                print "\t" + k.capitalize() + " %s_%s_%s\t" % (
                    "*st", kname, k) + '`json:"%s,omitempty"`' % k
        print "}\n"
    else:
        print "type st_" + kname + " struct{"
        for k, v in d.iteritems():
            if isinstance(v, bool):
                print "\t" + k.capitalize() + " bool\t" + '`json:"%s"`' % k
            elif isinstance(v, int):
                print "\t" + k.capitalize() + " int\t" + '`json:"%s"`' % k
            elif isinstance(v, float):
                print "\t" + k.capitalize() + " float32\t" + '`json:"%s"`' % k
            elif isinstance(v, basestring):
                print "\t" + k.capitalize() + " string\t" + '`json:"%s"`' % k
            elif isinstance(v, list):
                if len(v) > 0:
                    if isinstance(v[0], dict):
                        print "\t" + k.capitalize() + " []*st_%s_%s\t" % (
                            kname, k) + '`json:"%s"`' % k
                    if isinstance(v[0], int):
                        if is_all_int(v):
                            print "\t" + k.capitalize(
                            ) + " []int\t" + '`json:"%s"`' % k
                        else:
                            print "\t" + k.capitalize(
                            ) + " []float32\t" + '`json:"%s"`' % k
                    elif isinstance(v[0], float):
                        print "\t" + k.capitalize(
                        ) + " []float32\t" + '`json:"%s"`' % k
                    elif isinstance(v[0], basestring):
                        print "\t" + k.capitalize(
                        ) + " []string\t" + '`json:"%s"`' % k
        print "}\n"


def main():
    s_json = '''{
        "data" : {
            "order_id" : "b2db6bf74e124874ac4d1c0154f33a42",
            "paytransaction_id" : "81020171114182945417671878656102"
        },
        "ret_code" : 8000001,
        "ret_float" : 2.36,
        "list": [{"name":"1", "val": 2}],
        "list_int": [2,3],
        "param":{
            "list": [{"name":"1", "val": 2, "ll":[2,2.1]}],
            "list_int": [2,3],
            "code" : 8000001,
            "ext":{
                "name": "1001"
            }
        },
        "ret_msg" : "DD200207;交易处理中!"
    }'''
    jo = json.loads(s_json, "utf-8")
    if isinstance(jo, Iterable):
        print_dict("resp", jo)


if __name__ == "__main__":
    main()