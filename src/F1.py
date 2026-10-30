import model


def add_course():#新增新的課程
    new_course = []
    new_course.append(input("課程代碼:"))
    new_course.append(input("課程名稱:"))
    new_course.append(int(input("學分:")))
    new_course.append(input("必修/選修:"))
    new_course.append(input("教師:"))
    new_course.append(int(input("人數限制:")))
    new_course.append(0)#目前人數
    new_course.append(input("教室代碼:"))
    t = int(input("一周幾節課:"))
    new_course.append([input(f"時段{j+1}:") for j in range(t)])#時段

    check_new_course(new_course,t)#檢查是否衝堂

def add_student(): #新增學生
    new_student = []
    new_student_course = [[None] * 12 for _ in range(7)] #學生已選課程
    new_student.append(int(input("學號:")))
    new_student.append(input("姓名:"))
    new_student.append(input("系級:"))
    new_student.append(int(input("學分上限:")))

    for week in range(7):
        week_chinese = ["一", "二", "三", "四", "五", "六", "日"] #數字轉中文
        print(f"星期{week_chinese[week]}:")
        while True:
            course, period = input("已選課程(課程代碼 第幾節), 結束(N/n N/n):").split()
            if course == period == 'N' or period == period == 'n':
                break
            else:
                try:
                    period = int(period)
                except ValueError:
                    if period == 'a':
                        period = 10
                    elif period == 'b':
                        period = 11
                    elif period == 'c':
                        period = 12
                    else:
                        print("報錯拒絕,提示:沒有這節")
                        continue
                finally:
                    new_student_course[week][period - 1] = course

    new_student.append(new_student_course)

    check_new_student_id(new_student[0], new_student) #檢查學號是否重複

def check_new_course(new_course,t):#檢查是否衝堂
    s = 0#s = 0的話表示沒有錯誤
    for i in range(len(model.course)):#取預設課程總共數量
        if new_course[0] == model.course[i][0]:#檢查課程代碼是否重複
            print("報錯拒絕,提示:課程代碼重複")
            s = 1
            break
        elif new_course[2] > 0:#檢查學分是否為正數
            if new_course[5] >= 1:#檢查人數限制是否大於等於1
                continue
            else:
                print("報錯拒絕,提示:人數限制必須大於等於1")
                s = 1
                break
        else:
            print("報錯拒絕,提示:學分必須為正數")
            s = 1
            break
    if s == 0:#s = 0的话执行  時段格式是否正確
        for j in new_course[8]:#取新的節數次數
            if j[0] in "1234567":#检查新的课程时段时间是否为星期1-7
                if j[2] in "123456789abc":#检查新的课程时段时间是否为节数1-9 a-c
                    continue
                else:
                    print("報錯拒絕,提示:時段格式不正確")
                    s = 1
                    break
            else:
                print("報錯拒絕,提示:時段格式不正確")
                s = 1
                break
    if s == 0:
        print("回報成功")
        model.course.append(new_course)#新增課程

def check_new_student_id(student_id, new_student): #檢查學號是否重複
    for i in range(len(model.students)):
        if student_id == model.students[i][0]:
            print('報錯拒絕,提示:學號重複')
        else:
            model.students.append(new_student) #新增學生

def delete_course():#刪除課程
    code = input("請輸入要刪除的課程代碼:")
    j = 0#如果輸入錯誤代號執行
    for i in range(len(model.course)):#取預設課程總共數量
        if code == model.course[i][0]:#檢查課程代碼是否存在
            if model.course[i][6] == 0:#檢查目前人數是否為0
                model.course.pop(i)#刪除課程
                print("回報成功")
                j = 1
                break
            else:
                print("拒絕刪除,提示:請先執行退選或課程取消")
                j = 1
                break
    if j == 0:
        print("錯誤,提示:課程代碼不存在")

def search_student_date():#查詢學生資料
    id = int(input("請輸入學生學號: "))
    ii = 0#如果沒該學生測試
    for i in range(len(model.students)):
        if id == model.students[i][0]:
            ii = 1
            print(f"學生學號:{model.students[i][0]}\n學生名字:{model.students[i][1]}\n科系:{model.students[i][2]}\n學分上限:{model.students[i][3]}")
            a = model.students[i][4]#取名字
            user_a = getattr(model,a)#可以直接取得model.curriculum
            print("----個人課表----")
            print(f"{'節數':<5}{'一':<13}{'二':<13}{'三':<13}{'四':<13}{'五':<13}{'六':<13}{'日':<13}")
            for i in range(12):
                if i < 9:
                    m = str(i + 1)
                elif i == 9:
                    m = "a"
                elif i == 10:
                    m = "b"
                else:
                    m = "c"
                row = f"{'第'+ m +'節':<5}"
                for j in range(7):
                    code = user_a[j][i]
                    if code != "":
                        pcode = id_course(code)
                    else:
                        pcode = ""
                    chinese_char = sum(1 for char in pcode if  '\u4e00' <= char <= '\u9fff')
                    char_ = 13 - chinese_char
                    row += f"{pcode:<{char_}}"
                print(row)
            print("-------------")
    if ii == 0:
        print("沒這名學生")

def id_course(code):
    for i in range(len(model.course)):
        if code == model.course[i][0]:
            pcode=model.course[i][1]
    return pcode
#add_course()#測試
#delete_course()
search_student_date()
