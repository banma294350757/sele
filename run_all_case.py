# coding:utf-8
import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))
import time
from common.HTMLTestRunner_yo import HTMLTestRunner

discover1 = unittest.defaultTestLoader.discover("E:\\daima\\case",
                                               "test*.py")

nowtime = time.strftime("%Y_%m_%d_%H_%M")
reportpath = "E:\\daima\\case"+"report%s.html" % nowtime
fp = open(reportpath, "wb")
runner = HTMLTestRunner(fp,
                        verbosity=2,
                        title="测试报告",
                        description="报告内容如下",
                        retry=1)
runner.run(discover1)