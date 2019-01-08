import unittest,time
from HTMLTestRunner_PY3 import HTMLTestRunner
from HTMLTestRunner_PY3_1 import HTMLTestRunner
case_dir = "./test_case"

discover = unittest.defaultTestLoader.discover(case_dir,pattern="*case_*.py")


if __name__ =='__main__':
    #日期格式化
    times = time.strftime("%Y%m%d%H%M%S")
    report_file="./report/"+"aijia"+times+"-testresult.html"
    fp = open(report_file,"wb")

    runner = HTMLTestRunner(stream=fp,
                            title="自动化测试报告",
                            description="运行环境：win7 Chrome",
                            retry=1,
                            save_last_try=True)
    # runner = HTMLTestRunner(stream=fp,
    #                         title="自动化测试报告",
    #                         description="运行环境：win7 Chrome")
    runner.run(discover)

    fp.close()