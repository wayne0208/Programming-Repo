import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
import unittest
import F1
import model
from unittest.mock import patch#模擬使用者

class Test_F1_add_course(unittest.TestCase):
    def test_add_course(self):#增加課程測試
        all_test_input = [
             [["CS021", "資料庫", 3, "選修", "王小明", 30, "06206",2,"2-1", "2-2"],True],#回報成功
             [["CS001", "程式設計", 3, "必修", "郭大爺", 45, "06206",2,"2-9", "2-a"],False],#課程代碼重複
             [["CS022", "網路概論", -1, "選修", "李小華", 30, "03303",2, "3-1", "3-2"],False],#學分必須為正數
             [["CS023", "人工智慧", 3, "選修", "陳大文", 0, "06302",2, "4-1", "4-2"],False],#人數限制必須大於等於1
             [["CS024", "軟體工程", 3, "選修", "林小美", 30, "02303",2, "8-1", "8-2"],False],#時段格式不正確
             [["CS024", "軟體工程", 3, "選修", "林小美", 30, "02303",2, "5-1", "1-d"],False]#時段格式不正確
        ]#列測試清單
        for test_input ,is_success in all_test_input:
             index = len(model.course)  # 獲取當前課程列表的長度
             expected_code = test_input[0]  # 預期的課程代碼
             new_test_input = test_input#以防城市import os
             with self.subTest(course_code=expected_code):#測試標籤 以防連環出錯
                 with patch('builtins.input', side_effect=test_input):
                        F1.add_course()
                        if is_success ==True:
                            self.assertEqual(len(model.course), index + 1)  
                            self.assertEqual(model.course[index][0], expected_code) 
                            continue
                        elif is_success==False:
                             self.assertEqual(len(model.course), index) 
                             continue
                             
       
class Test_F1_delete_course(unittest.TestCase):
     def test_delete_course(self):
        all_test_input = [
                     [["CS002"],True],#回報成功
                     [["CS010"],False],#拒絕刪除
                     [["CS022"],False],]#錯誤
        for test_input ,is_success in all_test_input:
             index = len(model.course)  # 獲取當前課程列表的長度
             with self.subTest(course_code=test_input):
                  with patch("builtins.input",side_effect=test_input):
                       F1.delete_course()
                       if is_success==True:
                            self.assertEqual(len(model.course), index - 1)
                       elif is_success==False:
                         self.assertEqual(len(model.course), index)

if __name__ == '__main__':
    unittest.main()

